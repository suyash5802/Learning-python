import pandas as pd
import json
import os


# 3. Updated CSV (with our new total column)

df = pd.read_csv('data/sales.csv')
print(df)
print(f"\nShape: {df.shape[0]} rows , {df.shape[1]} col")

df['dis_price']= df["price"] +df["price"]*0.10;

print(df)

df.to_csv("output/new_sales_price.csv")
df.to_excel('output/sales_data.xlsx', index=False)
df.to_json('output/sales_data.json', orient='records', indent=2)


print("\nFiles saved:")
print("- output/sales_data.json")
print("- output/sales_data.xlsx") 
print("- output/sales_with_totals.csv")