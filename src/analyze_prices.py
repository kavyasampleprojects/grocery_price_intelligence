import pandas as pd

DATA_PATH = "data/processed/grocery_prices_sample.csv"

df = pd.read_csv(DATA_PATH)

print("\nDataset Preview:")
print(df.head())

print("\nCheapest price for each product:")
cheapest = df.loc[df.groupby("product")["price_eur"].idxmin()]
print(cheapest[["product", "supermarket", "brand", "price_eur"]])

print("\nAverage price by supermarket:")
avg_price = df.groupby("supermarket")["price_eur"].mean().sort_values()
print(avg_price)