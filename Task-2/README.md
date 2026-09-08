# Task 2: Exploratory Data Analysis, SQL & Dashboard

## Project Overview

This project was completed as part of the ApexPlanet Data Analytics Internship.

The objective of this task is to analyze sales data, identify meaningful patterns and trends, answer business questions using SQL, and present key insights through a static dashboard mock-up.

## Objective

The main objectives of this task are:

- Perform descriptive statistics and univariate analysis.
- Identify sales patterns across categories, products, cities, and customer segments.
- Answer business questions using SQL.
- Analyze relationships between numerical variables.
- Perform correlation analysis using heatmaps and pair plots.
- Create a static dashboard mock-up to present important KPIs and business insights.

## Dataset

The analysis was performed using the cleaned sales dataset prepared during Task 1.

The dataset contains:

- 1,000 sales records
- Customer information
- Product and category details
- Quantity and unit price
- Total sales
- Order dates
- City and gender information

## Tools & Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- MySQL
- Excel
- PowerPoint

## Section 1: Descriptive Statistics & Univariate Analysis

The following analyses were performed:

- Numerical summary statistics
- Categorical distributions
- Histograms
- Category-wise sales analysis
- Monthly sales trend analysis
- Product-wise sales analysis
- City-wise sales analysis
- Gender-wise sales analysis
- Age-group analysis

These analyses helped understand the distribution of sales, customer information, and product performance.

## Section 2: SQL for Business Questions

SQL queries were used to answer business-focused questions involving filtering, aggregation, grouping, sorting, and conditional logic.

### Business Questions

1. Which product categories generate the highest total sales?
2. What are the top 5 products by total sales?
3. How do sales change month by month?
4. Which cities generate the highest total sales?
5. What is the average sales value per dataset record?
6. How are customers distributed across age segments?
7. Are there products with high sales volume but relatively low revenue?

### Key Findings

#### Category-wise Sales

Electronics recorded the highest total sales, followed by Education.

#### Top 5 Products

Laptop was the highest-selling product among the top five products, followed closely by Mobile and Book.

#### Monthly Sales

March 2025 recorded the highest monthly sales in the dataset.

The monthly analysis also includes January 2026, which is a partial month in the available data.

#### City-wise Sales

Patna recorded the highest total sales among the cities in the dataset.

#### Average Sales per Record

The average `Total_Sales` value across the dataset was approximately ₹1.39 lakh per record.

#### High Volume but Low Revenue

No product satisfied both conditions used in the query:

- Higher-than-average sales quantity
- Lower-than-average total sales

This indicates that the selected criteria did not identify a product with simultaneously high volume and relatively low revenue.

## Section 3: Multivariate Analysis & Correlation

The following visualizations were created:

- Scatter plots
- Correlation matrix
- Correlation heatmap
- Pair plot

### Correlation Insights

- `Quantity` and `Total_Sales` show a moderate positive relationship.
- `Unit_Price` and `Total_Sales` also show a moderate positive relationship.
- `Age` has almost no correlation with `Total_Sales`.
- `Age` and `Quantity` show almost no relationship.
- The pair plot provides a combined visual view of the numerical variables.

### Conclusion from Correlation Analysis

Sales are more closely related to `Quantity` and `Unit_Price` than to `Age` in this dataset.

## Section 4: Static Dashboard Mock-up

A static dashboard mock-up was created using PowerPoint.

The dashboard presents important KPIs and sales insights, including:

- Total Sales
- Total Records
- Total Quantity
- Average Sales per Record
- Category-wise Sales
- Top 5 Products by Sales

### Dashboard KPIs

| KPI | Value |
|---|---:|
| Total Sales | ₹13.94 Cr |
| Total Records | 1,000 |
| Total Quantity | 5,435 |
| Average Sales per Record | ₹1.39 L |

## Overall Conclusion

The analysis shows that Electronics is the strongest-performing category, while Laptop is the highest-selling product among the top five products.

Sales are more closely associated with Quantity and Unit_Price than with customer Age.

The combination of Python, SQL, and dashboarding helped convert the sales dataset into meaningful business insights.

## Project Files

- `eda_analysis.py` — Python-based exploratory data analysis
- `sql_queries.sql` — SQL business questions and queries
- `sql_setup.sql` — SQL database and table setup and data verification queries
- `EDA_Report.md` — Detailed EDA report with analysis findings and visualizations
- `Images/` — Saved EDA visualizations
- `dashboard.html` — HTML dashboard reference
- `ApexPlanet_Task_2_Sales_Analysis_Dashboard.pptx` — Static dashboard mock-up
- `cleaned_sales_dataset.csv` — Cleaned dataset used for analysis

## How to Run

Install the required Python libraries:

    pip install pandas numpy openpyxl matplotlib seaborn

Run the EDA script:

    python eda_analysis.py

The database and table setup queries are available in `sql_setup.sql`. The cleaned CSV dataset was imported into MySQL Workbench using the Table Data Import Wizard.

The SQL queries can be executed in MySQL Workbench using the imported `sales_data` table.

The static dashboard mock-up is available in the PowerPoint file.