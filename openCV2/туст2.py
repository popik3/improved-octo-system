import cv2
import numpy as np
import os
import time
import mss
import asyncio
from concurrent.futures import ThreadPoolExecutor
from collections import deque

# Конфигурация
TEMPLATES_DIR = "C:/autocs2/templates"
THRESHOLD = 0.8
METHOD = cv2.TM_CCOEFF_NORMED
NMS_THRESHOLD = 0.3
FPS = 5
MONITOR = {"top": 0, "left": 0, "width": 1920, "height": 1080}
MAX_QUEUE_SIZE = 5  # Максимальная очередь кадров в RAM

# Глобальные переменные для хранения в RAM
templates = []
frame_queue = deque(maxlen=MAX_QUEUE_SIZE)
latest_processed_frame = None
processing_lock = asyncio.Lock()

def load_templates():
    """Загрузка шаблонов в RAM"""
    loaded = []
    for filename in os.listdir(TEMPLATES_DIR):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            img = cv2.imread(os.path.join(TEMPLATES_DIR, filename))
            if img is not None:
                loaded.append((filename, img))
    return loaded

def non_max_suppression(boxes, scores, threshold):
    """Оптимизированная NMS реализация"""
    if len(boxes) == 0:
        return []
    
    boxes = np.array(boxes)
    x1, y1, x2, y2 = boxes[:, 0], boxes[:, 1], boxes[:, 2], boxes[:, 3]
    areas = (x2 - x1 + 1) * (y2 - y1 + 1)
    indices = np.argsort(scores)[::-1]
    
    keep = []
    while len(indices) > 0:
        i = indices[0]
        keep.append(i)
        
        xx1 = np.maximum(x1[i], x1[indices[1:]])
        yy1 = np.maximum(y1[i], y1[indices[1:]])
        xx2 = np.minimum(x2[i], x2[indices[1:]])
        yy2 = np.minimum(y2[i], y2[indices[1:]])
        
        w = np.maximum(0, xx2 - xx1 + 1)
        h = np.maximum(0, yy2 - yy1 + 1)
        overlap = (w * h) / areas[indices[1:]]
        
        indices = indices[np.where(overlap <= threshold)[0] + 1]
    
    return boxes[keep]

async def capture_frames(sct):
    """Асинхронный захват кадров в RAM"""
    global frame_queue
    while True:
        try:
            # Захват в RAM без сохранения на диск
            sct_img = sct.grab(MONITOR)
            frame = np.array(sct_img)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)
            
            async with processing_lock:
                if len(frame_queue) < MAX_QUEUE_SIZE:
                    frame_queue.append(frame)
            
            await asyncio.sleep(1/FPS)  # Точный контроль FPS
            
        except Exception as e:
            print(f"Capture error: {e}")
            break

async def process_frames(executor):
    """Асинхронная обработка кадров из RAM"""
    global latest_processed_frame
    
    while True:
        try:
            # Берем последний кадр из очереди
            async with processing_lock:
                if not frame_queue:
                    await asyncio.sleep(0.001)
                    continue
                frame = frame_queue[-1].copy()  # Копируем для thread safety
            
            # Параллельная обработка шаблонов
            tasks = []
            for name, template in templates:
                task = asyncio.get_event_loop().run_in_executor(
                    executor,
                    process_template,
                    frame, template, name
                )
                tasks.append(task)
            
            # Собираем результаты
            results = await asyncio.gather(*tasks)
            all_boxes = []
            all_scores = []
            
            for boxes, scores in results:
                all_boxes.extend(boxes)
                all_scores.extend(scores)
            
            # Применяем NMS и рисуем результат
            if len(all_boxes) > 0:
                boxes = non_max_suppression(all_boxes, all_scores, NMS_THRESHOLD)
                for (x1, y1, x2, y2) in boxes:
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)
            
            # Обновляем последний обработанный кадр
            latest_processed_frame = frame
            
        except Exception as e:
            print(f"Processing error: {e}")

def process_template(frame, template, template_name):
    """Обработка одного шаблона (выполняется в потоке)"""
    h, w = template.shape[:2]
    res = cv2.matchTemplate(frame, template, METHOD)
    loc = np.where(res >= THRESHOLD)
    
    boxes = []
    scores = []
    for pt in zip(*loc[::-1]):
        boxes.append([pt[0], pt[1], pt[0] + w, pt[1] + h])
        scores.append(res[pt[1], pt[0]])
    
    return boxes, scores

async def display_frames():
    """Отображение кадров из RAM"""
    while True:
        try:
            if latest_processed_frame is not None:
                cv2.imshow('Real-Time Detection', latest_processed_frame)
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
                
            await asyncio.sleep(1/FPS)
            
        except Exception as e:
            print(f"Display error: {e}")
            break

async def main():
    global templates
    templates = load_templates()
    if not templates:
        print("❌ No templates loaded!")
        return
    
    # Настройка параллелизма
    executor = ThreadPoolExecutor(max_workers=os.cpu_count())
    sct = mss.mss()
    
    # Запуск задач
    capture_task = asyncio.create_task(capture_frames(sct))
    processing_task = asyncio.create_task(process_frames(executor))
    display_task = asyncio.create_task(display_frames())
    
    try:
        await asyncio.gather(capture_task, processing_task, display_task)
    except KeyboardInterrupt:
        pass
    finally:
        cv2.destroyAllWindows()
        sct.close()
        executor.shutdown()

if __name__ == "__main__":
    asyncio.run(main())
    
print(f"Queue size: {len(frame_queue)}")  # Мониторинг заполненности очереди