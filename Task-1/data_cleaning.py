import pandas as pd
import numpy as np
from pathlib import Path

# ============================================================
# 1. LOAD DATASET
# ============================================================

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "Data"

input_path = DATA_DIR / "ApexPlanet_DataAnalytics_Dataset.xlsx"
output_path = DATA_DIR / "cleaned_sales_dataset.csv"

df = pd.read_excel(input_path)

print("Dataset loaded successfully.")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])


# ============================================================
# 2. INITIAL DATA QUALITY ASSESSMENT
# ============================================================

print("\n--- Data Types ---")
print(df.dtypes)

print("\n--- Missing Values ---")
print(df.isnull().sum())

print("\n--- Duplicate Rows ---")
print(df.duplicated().sum())

print("\n--- Statistical Summary ---")
print(df.describe())


# ============================================================
# 3. DATA QUALITY CHECKS
# ============================================================

# Check Product-Category consistency
product_category_check = df.groupby("Product")["Category"].unique()

print("\n--- Product-Category Mapping ---")
print(product_category_check)


# Check Total_Sales calculation
calculated_sales = df["Quantity"] * df["Unit_Price"]

sales_mismatch = ~np.isclose(
    df["Total_Sales"],
    calculated_sales,
    rtol=1e-05,
    atol=0.01
)

print("\n--- Total_Sales Consistency ---")
print("Total_Sales mismatches:", sales_mismatch.sum())


# Check for invalid dates
parsed_dates = pd.to_datetime(df["Order_Date"], errors="coerce")

print("\n--- Order_Date Validation ---")
print("Invalid dates:", parsed_dates.isna().sum())
print("Minimum date:", parsed_dates.min())
print("Maximum date:", parsed_dates.max())


# Identify potential Total_Sales outliers using IQR
Q1 = df["Total_Sales"].quantile(0.25)
Q3 = df["Total_Sales"].quantile(0.75)
IQR = Q3 - Q1

upper_bound = Q3 + 1.5 * IQR
lower_bound = Q1 - 1.5 * IQR

outliers = df[
    (df["Total_Sales"] < lower_bound) |
    (df["Total_Sales"] > upper_bound)
]

print("\n--- Outlier Assessment ---")
print("Number of potential Total_Sales outliers:", len(outliers))

# The identified high-value transactions were reviewed and
# found to be mathematically consistent with Quantity × Unit_Price.
# Therefore, they are retained as legitimate transactions.


# ============================================================
# 4. DATA CLEANING
# ============================================================

# Create a copy so that the original dataset remains unchanged.
cleaned_df = df.copy()


# Handle missing Age values using the median.
age_median = cleaned_df["Age"].median()
cleaned_df["Age"] = cleaned_df["Age"].fillna(age_median)


# Handle missing City values using the most frequent city.
city_mode = cleaned_df["City"].mode()[0]
cleaned_df["City"] = cleaned_df["City"].fillna(city_mode)


# Standardize Order_Date to datetime format.
cleaned_df["Order_Date"] = pd.to_datetime(
    cleaned_df["Order_Date"],
    format="%Y-%m-%d"
)


# ============================================================
# 5. FEATURE ENGINEERING
# ============================================================

# Extract month from Order_Date for monthly analysis.
cleaned_df["Order_Month"] = cleaned_df["Order_Date"].dt.to_period("M")


# ============================================================
# 6. FINAL VALIDATION
# ============================================================

print("\n--- Final Dataset Validation ---")

print("Rows:", cleaned_df.shape[0])
print("Columns:", cleaned_df.shape[1])

print("\nRemaining Missing Values:")
print(cleaned_df.isnull().sum())

print("\nDuplicate Rows:", cleaned_df.duplicated().sum())

print("\nFinal Data Types:")
print(cleaned_df.dtypes)


# ============================================================
# 7. EXPORT CLEANED DATASET
# ============================================================

cleaned_df.to_csv(output_path, index=False)

print("\nCleaned dataset saved successfully.")
print("Output file:", output_path)