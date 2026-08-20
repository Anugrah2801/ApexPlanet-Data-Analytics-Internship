# Data Dictionary — ApexPlanet Sales Dataset

| Column | Data Type | Description |
|---|---|---|
| Order_ID | String | Identifier associated with an order; an order may contain multiple line items. |
| Order_Date | Date | Date on which the order was placed. |
| Customer_ID | String | Unique identifier assigned to the customer. |
| Customer_Name | String | Name/label of the customer. |
| Age | Numeric | Age of the customer. |
| Gender | Categorical | Gender of the customer. |
| City | Categorical | City associated with the customer/order. |
| Product | Categorical | Product purchased by the customer. |
| Category | Categorical | Product category associated with the purchased product. |
| Quantity | Integer | Number of units purchased in the order record. |
| Unit_Price | Numeric | Price of one unit of the purchased product. |
| Total_Sales | Numeric | Total sales value for the order record, calculated as Quantity × Unit_Price. |
| Order_Month | Period (Month) | Month extracted from Order_Date for monthly analysis. |

## Data Quality Notes

- Original dataset contains 1,000 rows and 12 columns.
- 20 Age values were missing and were filled using the median age.
- 13 City values were missing and were filled using the mode.
- No complete duplicate rows were found.
- No invalid Order_Date values were detected.
- Total_Sales was validated against Quantity × Unit_Price with 0 mismatches.
- 19 potential Total_Sales outliers were identified using the IQR method. These were retained for further analysis rather than removed.
- Order_Month was created as a derived feature during data preparation.
- Final cleaned dataset contains 1,000 rows, 13 columns, and no remaining missing values.