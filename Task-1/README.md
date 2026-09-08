# ApexPlanet Data Analytics Internship

A data analytics project completed as part of the ApexPlanet Data Analytics Internship.

The project focuses on preparing and validating a sales dataset using Python and Pandas, with emphasis on data quality assessment, cleaning, validation, feature engineering, and reproducible data preparation.

## Project Overview

The dataset contains sales transaction records with information about orders, customers, products, quantities, prices, and sales values.

The data preparation workflow includes:

- Initial dataset inspection
- Data type assessment
- Missing value analysis and treatment
- Duplicate row detection
- Product-category consistency checks
- Total sales validation
- Date validation
- Outlier assessment using the IQR method
- Data type conversion
- Feature engineering using `Order_Month`
- Final dataset validation
- Export of the cleaned dataset to CSV

## Dataset

The original dataset contains:

- **1,000 rows**
- **12 columns**
- Sales transaction and customer-related information

The cleaned dataset contains:

- **1,000 rows**
- **13 columns**
- No remaining missing values

The additional column, `Order_Month`, was created from `Order_Date` for monthly analysis.

## Data Quality Findings

During the initial assessment:

- 20 `Age` values were missing and were filled using the median age.
- 13 `City` values were missing and were filled using the mode.
- No complete duplicate rows were found.
- No invalid `Order_Date` values were detected.
- `Total_Sales` was validated against `Quantity × Unit_Price` with 0 mismatches.
- 19 potential `Total_Sales` outliers were identified using the IQR method.
- Potential outliers were retained for further analysis rather than automatically removed.

## Project Structure

```text
ApexPlanet-Data-Analytics-Internship/
│
├── Data/
│   ├── ApexPlanet_DataAnalytics_Dataset.xlsx
│   └── cleaned_sales_dataset.csv
│
├── data_cleaning.py
├── data_dictionary.md
├── .gitignore
└── README.md
```

## Tools & Technologies

- Python
- Pandas
- NumPy
- Excel
- CSV
- Git & GitHub

## How to Run

Make sure Python and the required Python libraries are installed.

Install the required libraries:

```bash
pip install pandas numpy openpyxl
```

Run the data cleaning script:

```bash
python data_cleaning.py
```

The script reads the original Excel dataset from the `Data` folder and generates the cleaned CSV dataset in the same folder.

## Documentation

The complete column-level documentation and data quality notes are available in:

`data_dictionary.md`

## Project Outcome

The final output is a validated and cleaned sales dataset containing 1,000 rows and 13 columns, ready for further exploratory data analysis and business-focused analysis.
