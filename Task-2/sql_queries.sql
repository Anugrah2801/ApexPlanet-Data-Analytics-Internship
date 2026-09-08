USE sales_analysis;


-- ============================================================
-- TASK 2: SQL FOR BUSINESS QUESTIONS
-- Database: sales_analysis
-- Table: sales_data
-- ============================================================


-- ============================================================
-- Q1. Which product categories generate the highest total sales?
-- ============================================================

SELECT
    Category,
    SUM(Total_Sales) AS total_sales
FROM sales_data
GROUP BY Category
ORDER BY total_sales DESC;


-- ============================================================
-- Q2. What are the top 5 products by total sales?
-- ============================================================

SELECT
    Product,
    SUM(Total_Sales) AS total_sales
FROM sales_data
GROUP BY Product
ORDER BY total_sales DESC
LIMIT 5;


-- ============================================================
-- Q3. How do sales change month by month?
-- ============================================================

SELECT
    Order_Month,
    SUM(Total_Sales) AS total_sales
FROM sales_data
GROUP BY Order_Month
ORDER BY Order_Month;


-- ============================================================
-- Q4. Which cities generate the highest total sales?
-- ============================================================

SELECT
    City,
    SUM(Total_Sales) AS total_sales
FROM sales_data
GROUP BY City
ORDER BY total_sales DESC;


-- ============================================================
-- Q5. What is the average sales value per record in each category?
-- ============================================================

SELECT
    Category,
    AVG(Total_Sales) AS average_sales_per_record
FROM sales_data
GROUP BY Category
ORDER BY average_sales_per_record DESC;


-- ============================================================
-- Q6. How are customers distributed across age segments?
-- ============================================================

SELECT
    CASE
        WHEN Age < 30 THEN 'Young Adult'
        WHEN Age BETWEEN 30 AND 49 THEN 'Adult'
        ELSE 'Senior'
    END AS customer_segment,
    COUNT(*) AS record_count,
    SUM(Total_Sales) AS total_sales
FROM sales_data
GROUP BY customer_segment
ORDER BY total_sales DESC;


-- ============================================================
-- Q7. Are there products with high sales volume but
--     relatively low revenue?
--
-- High sales volume = above-average total quantity
-- Low revenue = below-average total sales
-- Both conditions must be satisfied.
-- ============================================================

SELECT
    Product,
    SUM(Quantity) AS total_quantity,
    SUM(Total_Sales) AS total_sales
FROM sales_data
GROUP BY Product
HAVING SUM(Quantity) > (
    SELECT AVG(total_quantity)
    FROM (
        SELECT
            SUM(Quantity) AS total_quantity
        FROM sales_data
        GROUP BY Product
    ) AS product_totals
)
AND SUM(Total_Sales) < (
    SELECT AVG(total_sales)
    FROM (
        SELECT
            SUM(Total_Sales) AS total_sales
        FROM sales_data
        GROUP BY Product
    ) AS sales_totals
)
ORDER BY total_quantity DESC;