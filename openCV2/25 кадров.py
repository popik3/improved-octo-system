import os
import time
import cv2
import numpy as np
import mss
from concurrent.futures import ThreadPoolExecutor  # Для асинхронного сохранения

# Настройки
FPS = 25
OUTPUT_DIR = "C:/autocs2/input_images"  # Папка для сохранения
os.makedirs(OUTPUT_DIR, exist_ok=True)  # Создаем папку, если её нет

def save_frame(frame, frame_id):
    """Сохраняет кадр в папку в отдельном потоке"""
    filename = os.path.join(OUTPUT_DIR, f"frame_{frame_id:06d}.png")
    cv2.imwrite(filename, frame)
    print(f"Сохранено: {filename}")

def capture_and_save():
    with mss.mss() as sct:
        monitor = sct.monitors[1]  # Весь экран
        frame_count = 0
        delay = 1.0 / FPS
        
        # Пул потоков для асинхронного сохранения
        with ThreadPoolExecutor(max_workers=4) as executor:
            while True:
                start_time = time.perf_counter()
                
                # Захват кадра
                frame = np.array(sct.grab(monitor))
                frame_bgr = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)
                
                # Сохраняем в отдельном потоке (не блокируем основной цикл)
                executor.submit(save_frame, frame_bgr, frame_count)
                frame_count += 1
                
                # Поддержание FPS
                elapsed = time.perf_counter() - start_time
                time.sleep(max(0, delay - elapsed))

if __name__ == "__main__":
    try:
        capture_and_save()
    except KeyboardInterrupt:
        print("Скриншоты сохранены в папку:", OUTPUT_DIR)