import cv2
import numpy as np
import tensorflow as tf
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.preprocessing.image import img_to_array

def load_image(image_path):
    """
    Загружает и предварительно обрабатывает изображение для модели.
    """
    img = cv2.imread(image_path)
    img = cv2.resize(img, (268, 268))  # Размер, ожидаемый моделью MobileNetV2
    img = img_to_array(img)
    img = np.expand_dims(img, axis=0)
    img = tf.keras.applications.mobilenet_v2.preprocess_input(img)
    return img

def initialize_model():
    """
    Создаёт и инициализирует модель MobileNetV2.
    """
    model = MobileNetV2(include_top=True, weights='imagenet')
    return model

def predict_image(model, img_path):
    """
    Прогнозирует класс изображения и возвращает результат.
    """
    img = load_image(img_path)
    prediction = model.predict(img)
    decoded = tf.keras.applications.imagenet_utils.decode_predictions(prediction, top=1)[0][0]
    return decoded

if __name__ == '__main__':
    model = initialize_model()
    image_path = '"E:\python\i (19).jpg"'  # Замените на путь к вашему изображению
    result = predict_image(model, image_path)
    print(f"На изображении: {result[1]} с вероятностью {result[2]:.2%}")
