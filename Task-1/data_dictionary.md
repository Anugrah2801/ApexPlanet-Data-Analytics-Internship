# Data Dictionary — ApexPlanet Sales Dataset

| Column | Data Type | Description | Business Relevance |
|---|---|---|---|
| Order_ID | String | Identifier associated with an order; an order may contain multiple line items. | Used to identify and track individual orders. |
| Order_Date | Date | Date on which the order was placed. | Enables time-based sales analysis and trend identification. |
| Customer_ID | String | Unique identifier assigned to the customer. | Used to identify customers and support customer-level analysis. |
| Customer_Name | String | Name/label of the customer. | Provides customer-level identification for reporting and analysis. |
| Age | Numeric | Age of the customer. | Supports customer demographic analysis and segmentation. |
| Gender | Categorical | Gender of the customer. | Enables demographic comparisons and customer segmentation. |
| City | Categorical | City associated with the customer/order. | Supports geographic analysis of customers and sales. |
| Product | Categorical | Product purchased by the customer. | Helps identify product-level sales performance and demand. |
| Category | Categorical | Product category associated with the purchased product. | Enables category-level performance comparison. |
| Quantity | Integer | Number of units purchased in the order record. | Measures product demand and sales volume. |
| Unit_Price | Numeric | Price of one unit of the purchased product. | Helps evaluate pricing and revenue contribution. |
| Total_Sales | Numeric | Total sales value for the order record, calculated as Quantity × Unit_Price. | Key measure for evaluating revenue and sales performance. |
| Order_Month | Period (Month) | Month extracted from Order_Date for monthly analysis. | Enables monthly sales trend and seasonality analysis. |

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