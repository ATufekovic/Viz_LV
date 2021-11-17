import pandas as pd

data = pd.read_csv("I_ZupanijeEgradjani.csv")
print(data)

data.to_json("I_ZupanijeEgradjani_clean.json")