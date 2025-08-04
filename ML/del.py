import pandas as pd
import numpy as np

def remove_missing_values(df, subset=None, how='any'):
 # Проверка корректности параметра how
    if how not in ['any', 'all']:
        raise ValueError("Параметр how должен быть либо 'any', либо 'all'")
    
    # Если subset не указан, используем все столбцы
    if subset is None:
        subset = df.columns
    
    # Применяем фильтрацию
    return df.dropna(subset=subset, how=how)