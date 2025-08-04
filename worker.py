import pandas as pd

def baseline_median(data):
    return data(columns='feature').median()