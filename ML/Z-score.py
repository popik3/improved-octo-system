import numpy as np
import pandas as pd

def detect_outliers_zscore(data, threshold=3):
    """
    Обнаружение выбросов с использованием Z-score.

    Parameters:
        data (array-like или pd.Series): одномерный набор данных.
        threshold (float): порог для Z-score (обычно 3).

    Returns:
        pd.Series: Булева маска, где True соответствует выбросам.
    """
    series = pd.Series(data)
    mean = series.mean()
    #Используем ddof=0, чтобы соответствовать повеению np.std по умолчанию
    std = series.std(ddof=0)
    z_scores = np.abs((series - mean) / std)
    outlier_mask = z_scores > threshold
    return outlier_mask

data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -(10**5), 10**10])
print(detect_outliers_zscore(data))