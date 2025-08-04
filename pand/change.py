import pandas as pd

data = {"Имя": ["Анна", "Михаил", "Алиса"],
        "Возраст": [29, 35, 1]
}
df = pd.DataFrame(data)
#добавления нового столбца
df["СИСИ"] = [True, False, True]
#удаление столбца
df = df.drop("Возраст", axis=1)
#переименование столбцов
df = df.rename(columns={"Имя": "Name"})
#перестановка мест столбцов
df = df[ ["СИСИ", "Name"] ]




print(df)
