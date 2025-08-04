import numpy as np
import pandas as pd

def detected_outliers_iqr(data, multiplier=1.5):
    """
    Обнаружение выбросов с помощью метода IQR
    
    parameters:
        data (array-like или pd.Series): одномерный набор данных
        multiplier (float): коэфицент для определения границ выбросов (обычно 1.5)
        
    Returns:
        pd.Series: Булевая маска, где True соответствует выбросам
    """
    # приводим данные к сериас для удобства
    series = pd.Series(data)
    
    Q1 = series.quantile(0.25)
    Q3 = series.quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - multiplier * IQR
    upper_bound = Q3 + multiplier * IQR
    
    outlier_mask = (series < lower_bound) | (series > upper_bound)
    return outlier_mask

data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10**5, 10**10])
print(detected_outliers_iqr(data))
data = data[~detected_outliers_iqr(data)]
print(data)