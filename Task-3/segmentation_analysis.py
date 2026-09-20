import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# --------------------------------------------------
# 1. PATHS AND DATA LOADING
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR.parent / "Data" / "cleaned_sales_dataset.csv"
OUTPUT_DIR = BASE_DIR / "outputs"
CHART_DIR = OUTPUT_DIR / "charts"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
CHART_DIR.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(DATA_PATH)

print("=" * 60)
print("APEXPLANET TASK-3: SALES SEGMENTATION ANALYSIS")
print("=" * 60)

# --------------------------------------------------
# 2. BASIC VALIDATION
# --------------------------------------------------

required_columns = [
    "Age", "City", "Category",
    "Quantity", "Total_Sales"
]

missing_columns = [
    col for col in required_columns
    if col not in df.columns
]

if missing_columns:
    raise ValueError(
        f"Missing required columns: {missing_columns}"
    )

if df[required_columns].isnull().any().any():
    raise ValueError(
        "Missing values found in required columns."
    )

# --------------------------------------------------
# 3. AGE GROUP SEGMENTATION
# Business-rule groups for this analysis:
# 18–29, 30–44, 45–65
# --------------------------------------------------

df["Age_Group"] = pd.cut(
    df["Age"],
    bins=[17, 29, 44, 65],
    labels=["18-29", "30-44", "45-65"],
    right=True,
    include_lowest=True
)

if df["Age_Group"].isnull().any():
    raise ValueError(
        "Some ages fall outside the defined age groups."
    )

# --------------------------------------------------
# 4. CORE KPIs
# --------------------------------------------------

total_sales = df["Total_Sales"].sum()
total_quantity = df["Quantity"].sum()
total_records = len(df)

average_sales_per_record = (
    df["Total_Sales"].mean()
)

unique_customers = (
    df["Customer_ID"].nunique()
    if "Customer_ID" in df.columns
    else None
)

kpi_summary = pd.DataFrame({
    "KPI": [
        "Total Sales",
        "Total Quantity",
        "Total Records",
        "Average Sales per Record",
        "Unique Customers"
    ],
    "Value": [
        total_sales,
        total_quantity,
        total_records,
        average_sales_per_record,
        unique_customers
    ]
})

print("\n--- CORE KPIs ---")
print(kpi_summary.to_string(index=False))

kpi_summary.to_csv(
    OUTPUT_DIR / "core_kpis.csv",
    index=False
)

# --------------------------------------------------
# 5. REUSABLE SEGMENT SUMMARY FUNCTION
# --------------------------------------------------

def summarize_segment(data, segment_column):
    summary = (
        data.groupby(
            segment_column,
            observed=True
        )
        .agg(
            Total_Sales=("Total_Sales", "sum"),
            Total_Quantity=("Quantity", "sum"),
            Record_Count=("Total_Sales", "size"),
            Average_Sales_Per_Record=("Total_Sales", "mean")
        )
        .reset_index()
    )

    summary["Sales_Contribution_Pct"] = (
        summary["Total_Sales"] / total_sales * 100
    )

    summary = summary.sort_values(
        "Total_Sales",
        ascending=False
    )

    return summary


# --------------------------------------------------
# 6. AGE, CITY AND CATEGORY SEGMENTATION
# --------------------------------------------------

age_summary = summarize_segment(df, "Age_Group")
city_summary = summarize_segment(df, "City")
category_summary = summarize_segment(df, "Category")

print("\n--- AGE GROUP ANALYSIS ---")
print(age_summary.to_string(index=False))

print("\n--- CITY ANALYSIS ---")
print(city_summary.to_string(index=False))

print("\n--- CATEGORY ANALYSIS ---")
print(category_summary.to_string(index=False))

age_summary.to_csv(
    OUTPUT_DIR / "age_group_analysis.csv",
    index=False
)

city_summary.to_csv(
    OUTPUT_DIR / "city_analysis.csv",
    index=False
)

category_summary.to_csv(
    OUTPUT_DIR / "category_analysis.csv",
    index=False
)

print("\n--- SALES TOTAL CHECK ---")
print("DataFrame Total:", df["Total_Sales"].sum())
print("KPI Total:", total_sales)
print("Age Groups Total:", age_summary["Total_Sales"].sum())
print("Cities Total:", city_summary["Total_Sales"].sum())
print("Categories Total:", category_summary["Total_Sales"].sum())


# --------------------------------------------------
# 7. COMBINED AGE GROUP + CATEGORY ANALYSIS
# --------------------------------------------------

age_category_summary = (
    df.groupby(
        ["Age_Group", "Category"],
        observed=True
    )
    .agg(
        Total_Sales=("Total_Sales", "sum"),
        Total_Quantity=("Quantity", "sum"),
        Record_Count=("Total_Sales", "size")
    )
    .reset_index()
)

age_category_summary["Sales_Contribution_Pct"] = (
    age_category_summary["Total_Sales"]
    / total_sales * 100
)

print("Age × Category Total:", age_category_summary["Total_Sales"].sum())

age_category_summary.to_csv(
    OUTPUT_DIR / "age_category_analysis.csv",
    index=False
)

print("\n--- AGE GROUP × CATEGORY ANALYSIS ---")
print(age_category_summary.to_string(index=False))

# --------------------------------------------------
# 8. CHART 1: SALES BY AGE GROUP
# --------------------------------------------------

age_plot = age_summary.sort_values("Age_Group")

plt.figure(figsize=(9, 5))
plt.bar(
    age_plot["Age_Group"].astype(str),
    age_plot["Total_Sales"]
)

plt.title("Total Sales by Age Group")
plt.xlabel("Age Group")
plt.ylabel("Total Sales")
plt.grid(axis="y", alpha=0.3)
plt.tight_layout()

plt.savefig(
    CHART_DIR / "sales_by_age_group.png",
    dpi=300
)
plt.close()

# --------------------------------------------------
# 9. CHART 2: SALES BY CITY
# --------------------------------------------------

city_plot = city_summary.sort_values(
    "Total_Sales",
    ascending=True
)

plt.figure(figsize=(10, 6))
plt.barh(
    city_plot["City"],
    city_plot["Total_Sales"]
)

plt.title("Total Sales by City")
plt.xlabel("Total Sales")
plt.ylabel("City")
plt.grid(axis="x", alpha=0.3)
plt.tight_layout()

plt.savefig(
    CHART_DIR / "sales_by_city.png",
    dpi=300
)
plt.close()

# --------------------------------------------------
# 10. CHART 3: SALES BY CATEGORY
# --------------------------------------------------

category_plot = category_summary.sort_values(
    "Total_Sales",
    ascending=False
)

plt.figure(figsize=(10, 6))
plt.bar(
    category_plot["Category"],
    category_plot["Total_Sales"]
)

plt.title("Total Sales by Product Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.xticks(rotation=25, ha="right")
plt.grid(axis="y", alpha=0.3)
plt.tight_layout()

plt.savefig(
    CHART_DIR / "sales_by_category.png",
    dpi=300
)
plt.close()

# --------------------------------------------------
# 11. KEY FINDINGS
# --------------------------------------------------

print("\n--- KEY FINDINGS ---")

top_age = age_summary.iloc[0]
top_city = city_summary.iloc[0]
top_category = category_summary.iloc[0]

print(
    f"Highest-sales age group: "
    f"{top_age['Age_Group']} "
    f"({top_age['Sales_Contribution_Pct']:.2f}% "
    f"of total sales)"
)

print(
    f"Highest-sales city: "
    f"{top_city['City']} "
    f"({top_city['Sales_Contribution_Pct']:.2f}% "
    f"of total sales)"
)

print(
    f"Highest-sales category: "
    f"{top_category['Category']} "
    f"({top_category['Sales_Contribution_Pct']:.2f}% "
    f"of total sales)"
)

print("\n--- OUTPUTS SAVED ---")
print(f"Reports: {OUTPUT_DIR}")
print(f"Charts:  {CHART_DIR}")

print("\nAnalysis completed successfully!") 