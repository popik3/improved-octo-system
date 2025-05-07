import numpy as np
import cv2

# Загрузка изображений (скриншот и шаблон врага)
img = cv2.imread('openCV2/image 2/Screenshot_16.png')  # Цветной скриншот
template = cv2.imread('openCV2/image 2/image.png')  # Шаблон врага (например, голова или силуэт)

# Проверка, что изображения загружены
if img is None or template is None:
    print("Ошибка загрузки изображений!")
    exit()

h, w = template.shape[:2]

# Методы сравнения (можно перебирать)
methods = [
    ('TM_CCOEFF_NORMED', cv2.TM_CCOEFF_NORMED),
    ('TM_SQDIFF', cv2.TM_SQDIFF),
    ('TM_CCORR_NORMED', cv2.TM_CCORR_NORMED)
]

threshold = 0.9  # Начни с 0.7 и регулируй

for name, method in methods:
    result = cv2.matchTemplate(img, template, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc  # Для SQDIFF минимум = лучший результат
        current_val = min_val
    else:
        top_left = max_loc
        current_val = max_val

    print(f"{name}: Лучшее совпадение = {current_val:.2f}")

    if current_val >= threshold:
        bottom_right = (top_left[0] + w, top_left[1] + h)
        cv2.rectangle(img, top_left, bottom_right, (0, 0, 255), 2)
        print(f"Враг найден! Метод: {name}")

cv2.imshow('Result', img)
cv2.waitKey(0)
cv2.destroyAllWindows()