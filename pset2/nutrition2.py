import pandas as pd

df = pd.read_csv('pset2/data.csv')
# print(df.to_string())

df.set_index("Fruits", inplace = True)

item = input("Item: ").lower()

print(df.loc[item]["calories"])

