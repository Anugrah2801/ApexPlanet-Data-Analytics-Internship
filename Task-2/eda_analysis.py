import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path


# ============================================================
# TASK 2: EXPLORATORY DATA ANALYSIS
# Sections 1 and 3
# ============================================================


# ============================================================
# 1. LOAD CLEANED DATASET
# ============================================================

# Locate the cleaned dataset.
# This supports running the script from either the project
# root folder or the Task-2 folder.

project_root = Path(__file__).resolve().parent.parent
dataset_path = project_root / "Data" / "cleaned_sales_dataset.csv"

df = pd.read_csv(dataset_path)

print("\n============================================================")
print("TASK 2: EXPLORATORY DATA ANALYSIS")
print("============================================================")

print("\n--- Dataset Loaded Successfully ---")
print(f"Number of rows: {df.shape[0]}")
print(f"Number of columns: {df.shape[1]}")


# ============================================================
# 2. BASIC DATASET INSPECTION
# ============================================================

print("\n--- Dataset Columns ---")
print(df.columns.tolist())

print("\n--- Dataset Data Types ---")
print(df.dtypes)

print("\n--- Dataset Shape ---")
print(df.shape)


# ============================================================
# SECTION 1:
# DESCRIPTIVE STATISTICS & UNIVARIATE ANALYSIS
# ============================================================


# ------------------------------------------------------------
# 1.1 Categorical Data Distribution
# ------------------------------------------------------------

print("\n============================================================")
print("SECTION 1: DESCRIPTIVE STATISTICS & UNIVARIATE ANALYSIS")
print("============================================================")

print("\n--- Gender Distribution ---")
print(df["Gender"].value_counts())

print("\n--- City Distribution ---")
print(df["City"].value_counts())

print("\n--- Product Distribution ---")
print(df["Product"].value_counts())

print("\n--- Category Distribution ---")
print(df["Category"].value_counts())


# ------------------------------------------------------------
# 1.2 Categorical Distribution Visualizations
# ------------------------------------------------------------

# Gender Distribution

gender_counts = df["Gender"].value_counts()

gender_counts.plot(kind="bar")

plt.title("Gender Distribution")
plt.xlabel("Gender")
plt.ylabel("Number of Records")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


# City Distribution

city_counts = df["City"].value_counts()

city_counts.plot(kind="bar")

plt.title("City Distribution")
plt.xlabel("City")
plt.ylabel("Number of Records")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# Product Distribution

product_counts = df["Product"].value_counts()

product_counts.plot(kind="bar")

plt.title("Product Distribution")
plt.xlabel("Product")
plt.ylabel("Number of Records")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# Category Distribution

category_counts = df["Category"].value_counts()

category_counts.plot(kind="bar")

plt.title("Category Distribution")
plt.xlabel("Category")
plt.ylabel("Number of Records")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# ------------------------------------------------------------
# 1.3 Numerical Descriptive Statistics
# ------------------------------------------------------------

print("\n--- Numerical Descriptive Statistics ---")

print(
    df[
        ["Age", "Quantity", "Unit_Price", "Total_Sales"]
    ].describe()
)


# ------------------------------------------------------------
# 1.4 Numerical Data Distribution Visualizations
# ------------------------------------------------------------

# Age Distribution

plt.figure()

df["Age"].plot(kind="hist", bins=10)

plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()


# Quantity Distribution

plt.figure()

df["Quantity"].plot(kind="hist", bins=10)

plt.title("Quantity Distribution")
plt.xlabel("Quantity")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()


# Unit Price Distribution

plt.figure()

df["Unit_Price"].plot(kind="hist", bins=10)

plt.title("Unit Price Distribution")
plt.xlabel("Unit Price")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()


# Total Sales Distribution

plt.figure()

df["Total_Sales"].plot(kind="hist", bins=10)

plt.title("Total Sales Distribution")
plt.xlabel("Total Sales")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()


# ------------------------------------------------------------
# 1.5 One-Variable Sales Analysis
# ------------------------------------------------------------


# Category-wise Total Sales

print("\n--- Category-wise Total Sales ---")

category_sales = (
    df.groupby("Category")["Total_Sales"]
    .sum()
    .sort_values(ascending=False)
)

print(category_sales)

category_sales.plot(kind="bar")

plt.title("Category-wise Total Sales")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("Images/category_wise_sales.png", dpi=300, bbox_inches="tight")
plt.show()


# ------------------------------------------------------------
# Monthly Sales Trend
# ------------------------------------------------------------

print("\n--- Monthly Sales Analysis ---")

monthly_sales = (
    df.groupby("Order_Month")["Total_Sales"]
    .sum()
    .sort_index()
)

print(monthly_sales)

plt.figure(figsize=(10, 5))

monthly_sales.plot(kind="line", marker="o")

plt.title("Monthly Sales Trend")
plt.xlabel("Order Month")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("Images/monthly_sales_trend.png", dpi=300, bbox_inches="tight")
plt.show()


# Product-wise Total Sales

print("\n--- Product-wise Total Sales ---")

product_sales = (
    df.groupby("Product")["Total_Sales"]
    .sum()
    .sort_values(ascending=False)
)

print(product_sales)

product_sales.plot(kind="bar")

plt.title("Product-wise Total Sales")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# City-wise Total Sales

print("\n--- City-wise Total Sales ---")

city_sales = (
    df.groupby("City")["Total_Sales"]
    .sum()
    .sort_values(ascending=False)
)

print(city_sales)

city_sales.plot(kind="bar")

plt.title("City-wise Total Sales")
plt.xlabel("City")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# Gender-wise Total Sales

print("\n--- Gender-wise Total Sales ---")

gender_sales = (
    df.groupby("Gender")["Total_Sales"]
    .sum()
    .sort_values(ascending=False)
)

print(gender_sales)

gender_sales.plot(kind="bar")

plt.title("Gender-wise Total Sales")
plt.xlabel("Gender")
plt.ylabel("Total Sales")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


# Age Group-wise Total Sales

df["Age_Group"] = pd.cut(
    df["Age"],
    bins=[0, 18, 25, 35, 45, 55, 100],
    labels=["<18", "18-25", "26-35", "36-45", "46-55", "56+"]
)

age_group_sales = (
    df.groupby("Age_Group", observed=False)["Total_Sales"]
    .sum()
)

print("\n--- Age Group-wise Total Sales ---")
print(age_group_sales)

age_group_sales.plot(kind="bar")

plt.title("Age Group-wise Total Sales")
plt.xlabel("Age Group")
plt.ylabel("Total Sales")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


# ============================================================
# SECTION 3:
# MULTIVARIATE ANALYSIS & CORRELATION
# ============================================================


print("\n============================================================")
print("SECTION 3: MULTIVARIATE ANALYSIS & CORRELATION")
print("============================================================")


# ------------------------------------------------------------
# 3.1 Quantity vs Total Sales
# ------------------------------------------------------------

print("\n--- Quantity vs Total Sales Correlation ---")

quantity_sales_corr = (
    df["Quantity"].corr(df["Total_Sales"])
)

print(quantity_sales_corr)


plt.figure()

plt.scatter(
    df["Quantity"],
    df["Total_Sales"]
)

plt.title("Quantity vs Total Sales")
plt.xlabel("Quantity")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig("Images/quantity_vs_total_sales.png", dpi=300, bbox_inches="tight")
plt.show()

# ------------------------------------------------------------
# 3.2 Unit Price vs Total Sales
# ------------------------------------------------------------

print("\n--- Unit Price vs Total Sales Correlation ---")

unit_price_sales_corr = (
    df["Unit_Price"].corr(df["Total_Sales"])
)

print(unit_price_sales_corr)


plt.figure()

plt.scatter(
    df["Unit_Price"],
    df["Total_Sales"]
)

plt.title("Unit Price vs Total Sales")
plt.xlabel("Unit Price")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig("Images/unit_price_vs_total_sales.png", dpi=300, bbox_inches="tight")
plt.show()


# ------------------------------------------------------------
# 3.3 Correlation Matrix
# ------------------------------------------------------------

numerical_columns = [
    "Age",
    "Quantity",
    "Unit_Price",
    "Total_Sales"
]

correlation_matrix = df[numerical_columns].corr()

print("\n--- Correlation Matrix ---")
print(correlation_matrix)


# ------------------------------------------------------------
# 3.4 Correlation Heatmap
# ------------------------------------------------------------

plt.figure(figsize=(8, 6))

sns.heatmap(
    correlation_matrix,
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)

plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig("Images/correlation_heatmap.png", dpi=300, bbox_inches="tight")
plt.show()


# ------------------------------------------------------------
# 3.5 Pair Plot
# ------------------------------------------------------------

pair_plot = sns.pairplot(
    df[numerical_columns]
)

pair_plot.savefig("Images/pair_plot.png", dpi=300, bbox_inches="tight")
plt.show()


# ============================================================
# SECTION 3: CORRELATION INSIGHTS
# ============================================================

# 1. Quantity and Total_Sales show a moderate positive
#    relationship.
#    Higher quantities generally lead to higher total sales.

# 2. Unit_Price and Total_Sales also show a moderate positive
#    relationship.
#    Products with higher unit prices generally contribute
#    more to total sales.

# 3. Age has almost no correlation with Total_Sales.
#    Customer age does not appear to strongly influence sales
#    in this dataset.

# 4. Age and Quantity show almost no relationship.
#    Customer age does not strongly affect the quantity purchased.

# 5. The pair plot provides a combined visual view of the
#    numerical variables.
#    It helps confirm the relationships observed in the
#    correlation matrix and scatter plots.


# ============================================================
# FINAL CONCLUSION
# ============================================================

# Sales are more closely related to Quantity and Unit_Price
# than to Age in this dataset.

print("\n============================================================")
print("EDA ANALYSIS COMPLETED SUCCESSFULLY")
print("============================================================")