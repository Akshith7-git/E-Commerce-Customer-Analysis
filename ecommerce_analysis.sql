USE ecommerce_db;

-- 1. View first 10 records
SELECT * FROM orders LIMIT 10;

-- 2. Total records
SELECT COUNT(*) AS Total_Records
FROM orders;

-- 3. Total orders
SELECT COUNT(DISTINCT Order_ID) AS Total_Orders
FROM orders;

-- 4. Total revenue
SELECT SUM(Total_Amount_INR) AS Total_Revenue
FROM orders;

-- 5. Total customers
SELECT COUNT(DISTINCT Customer_ID) AS Total_Customers
FROM orders;

-- 6. Average order value
SELECT ROUND(AVG(Total_Amount_INR), 2) AS Average_Order_Value
FROM orders;

-- 7. Revenue by category
SELECT Category, SUM(Total_Amount_INR) AS Revenue
FROM orders
GROUP BY Category
ORDER BY Revenue DESC;

-- 8. Top 10 customers
SELECT Customer_ID, SUM(Total_Amount_INR) AS Total_Spending
FROM orders
GROUP BY Customer_ID
ORDER BY Total_Spending DESC
LIMIT 10;

-- 9. Top-selling products
SELECT Product_Name, SUM(Quantity) AS Total_Quantity
FROM orders
GROUP BY Product_Name
ORDER BY Total_Quantity DESC;

-- 10. Monthly revenue
SELECT MONTHNAME(Order_Date) AS Month,
       SUM(Total_Amount_INR) AS Revenue
FROM orders
GROUP BY MONTH(Order_Date), MONTHNAME(Order_Date)
ORDER BY MONTH(Order_Date);

-- 11. Revenue by city
SELECT City, SUM(Total_Amount_INR) AS Revenue
FROM orders
GROUP BY City
ORDER BY Revenue DESC;

-- 12. Payment method analysis
SELECT Payment_Method,
       COUNT(*) AS Total_Orders,
       SUM(Total_Amount_INR) AS Revenue
FROM orders
GROUP BY Payment_Method
ORDER BY Revenue DESC;

-- 13. Gender analysis
SELECT Gender,
       COUNT(DISTINCT Customer_ID) AS Customers,
       SUM(Total_Amount_INR) AS Revenue
FROM orders
GROUP BY Gender;