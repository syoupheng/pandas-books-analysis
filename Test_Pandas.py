import numpy as np
import pandas as pd
from sqlalchemy import create_engine, exc
from sqlalchemy.types import String

engine = create_engine("mysql://syoupheng:spd75013@localhost/testPandas")

loc = ("Fruit_Prices.xlsx")
df = pd.read_excel(loc, sheet_name="Feuil1")
# Removes empty rows and columns
df = df.dropna(axis=1, how="all")
df = df.dropna(how="all")
print(df)
fruits_df = df.iloc[ : , [0, 1]].dropna(how="all")
fruits_df = fruits_df.rename(columns=fruits_df.iloc[0])
fruits_df = fruits_df.iloc[1: ]
fruits_df.loc[8, 'Prix'] = 45
print(fruits_df)
employees_df = df.iloc[:, 2:].dropna(how="all")
employees_df = employees_df.rename(columns=employees_df.iloc[0])
employees_df = employees_df.iloc[1:]
print(employees_df)
employees_df[employees_df.isnull()] = 25
print(employees_df)
try:
    fruits_df.to_sql("Fruits", engine, if_exists="append", index=False, dtype={"Fruits":String(length=255)})
    employees_df.to_sql("Employees", engine, if_exists="append", index=False, dtype={"Nom":String(length=45), "Prénom":String(length=45)})
except (exc.IntegrityError, exc.OperationalError) as err:
    print(err)