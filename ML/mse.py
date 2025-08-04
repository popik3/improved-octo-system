import numpy as np

def r2(y_pred, y_test):
    """
    Вычисляет коэффициент детерминации R² с учётом крайних значений.
    
    Параметры:
        y_pred (np.array): Предсказанные значения.
        y_test (np.array): Истинные значения.
    
    Возвращает:
        float: R² в диапазоне (-∞, 1], с обработкой крайних случаев.
    """
    # Проверка на идентичность массивов (R² = 1)
    if np.array_equal(y_pred, y_test):
        return 1.0
    
    # Проверка, что все истинные значения одинаковы (SS_tot = 0 → деление на 0)
    if np.all(y_test == y_test[0]):
        return 0.0  # или np.nan, в зависимости от требований
    
    # Основной расчёт
    ss_res = np.sum((y_test - y_pred) ** 2)
    ss_tot = np.sum((y_test - np.mean(y_test)) ** 2)
    r_squared = 1 - (ss_res / ss_tot)
    
    return r_squared