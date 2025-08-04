import pandas as pd
import openpyxl

data = {
    "Date": ["2024-01-01", "2024-01-01", "2024-01-01", "2024-01-02", "2024-01-02", "2024-01-02"],
    "City": ["Москва", "Владивосток", "Казань", "Москва", "Владивосток", "Казань"],
    "Temperature": [32, 15, 25, 33, 18, 26],
}

df3 = pd.DataFrame(data)
print(df3, "//n")
#используем метод pivot для изменения формы данных
pivot_df3 = df3.pivot(index="Date", columns="City",
                      values="Temperature")
print(pivot_df3)
pivot_table3 = pd.pivot_table(df3, values="Temperature", index="City",
                              columns="Date")
print(pivot_table3)
pivot_table3.to_excel("Сводная по городам.csv")