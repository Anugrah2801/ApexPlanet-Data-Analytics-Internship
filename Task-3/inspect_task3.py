import pandas as pd
from pathlib import Path

# Load the cleaned dataset
file_path = Path("../Data/cleaned_sales_dataset.csv")
df = pd.read_csv(file_path)

print("\n--- DATASET SHAPE ---")
print(df.shape)

print("\n--- COLUMN NAMES ---")
print(df.columns.tolist())

print("\n--- DATA TYPES ---")
print(df.dtypes)

print("\n--- MISSING VALUES ---")
print(df.isnull().sum())

print("\n--- SAMPLE DATA ---")
print(df.head())

print("\n--- UNIQUE VALUES IN SEGMENT COLUMNS ---")
for col in ["Age", "City", "Category"]:
    if col in df.columns:
        print(f"\n{col}:")
        print(sorted(df[col].dropna().unique().tolist()))