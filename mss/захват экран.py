import mss
import mss.tools

with mss.mss() as sct:
    # Захватываем весь экран (или конкретный монитор)
    monitor = sct.monitors[1]  # 1 — это основной монитор
    screenshot = sct.grab(monitor)  # Получаем скриншот
    
    # Сохраняем в PNG
    mss.tools.to_png(screenshot.rgb, screenshot.size, output="screenshot.png")