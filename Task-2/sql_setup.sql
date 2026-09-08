USE sales_analysis;

-- ============================================================
-- SQL SETUP
-- ============================================================

-- Create the sales_data table
CREATE TABLE sales_data (
    Order_ID VARCHAR(20),
    Order_Date DATE,
    Customer_ID VARCHAR(20),
    Customer_Name VARCHAR(100),
    Age DECIMAL(5,2),
    Gender VARCHAR(20),
    City VARCHAR(50),
    Product VARCHAR(50),
    Category VARCHAR(50),
    Quantity INT,
    Unit_Price DECIMAL(12,2),
    Total_Sales DECIMAL(14,2),
    Order_Month VARCHAR(7)
);

-- Verify table creation
SHOW TABLES;
DESC sales_data;

-- Verify imported data
SELECT COUNT(*) AS total_records
FROM sales_data;

SELECT *
FROM sales_data
LIMIT 5;