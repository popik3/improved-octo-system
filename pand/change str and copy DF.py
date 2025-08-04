import pandas as pd

data = {"Имя": ["Анна", "Михаил", "Алиса"],
        "Возраст": [29, 35, 1]
}
df = pd.DataFrame(data)
new_row = pd.Series({"Имя": "Василий", "Возраст": 5},
                    name=len(df))
"""
print(new_row)
print("\n")
print(new_row.to_frame().T)
"""
df = pd.concat([df, new_row.to_frame().T])
#print(df)

df.loc[len(df)] = ["Тимофей", 8]
df = df.drop(df.index[3])
print(df)


df_copy = df.copy