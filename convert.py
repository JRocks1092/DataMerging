from os import access
import pandas as pd
 
df = pd.read_csv("dwarf_stars.csv")
df = df.dropna()
df.drop(["Unnamed: 0"], axis=1,inplace=True)

df["Radius"] = 0.102763 * df["Radius"]
df["Mass"] = df["Mass"].apply(lambda x:x.replace(",", "")).astype("float")
df["Mass"] = df["Mass"] * 0.000954588
df.reset_index(drop=True, inplace=True)

print(df.head())

df.to_csv("dwarf_converted.csv")