import pandas as pd
import os

url = "https://api.slingacademy.com/v1/sample-data/files/employees.csv"

os.makedirs("data", exist_ok=True)

df = pd.read_csv(url)
df.to_csv("data/web_data.csv", index=False)

print("Web dataset κατέβηκε στο data/web_data.csv")
print(df.head())