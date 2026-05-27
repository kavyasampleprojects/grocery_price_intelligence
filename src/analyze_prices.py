import pandas as pd

DATA_PATH = "data/processed/grocery_prices_sample.csv"

df = pd.read_csv(DATA_PATH)

# Calculate standardized price

def calculate_standard_price(row):

    if row["unit"] == "kg":
        return row["price_eur"]

    if row["unit"] == "liter":
        return row["price_eur"]

    if row["unit"] == "g":
        return row["price_eur"] / (row["quantity"] / 1000)

    return None


df["price_per_standard_unit"] = df.apply(calculate_standard_price,axis=1)

print("\nDataset with standardized prices:\n")

print(
    df[
        [
            "product",
            "supermarket",
            "quantity",
            "unit",
            "price_eur",
            "price_per_standard_unit"
        ]
    ]
)

print("\nCheapest supermarket by standardized price:\n")

cheapest = df.loc[
    df.groupby("product")["price_per_standard_unit"].idxmin()
]

print(
    cheapest[
        [
            "product",
            "supermarket",
            "price_per_standard_unit"
        ]
    ]
)