-- 1. View the order_details table.
SELECT * FROM order_details ;

-- 2. whats the date range of the table?
SELECT MIN(order_date),MAX(order_date) FROM order_details;

-- 3. How many orders were made within the date range?
SELECT COUNT(DISTINCT order_id) FROM order_details;

-- 4. howmany items were ordered within this daterange?
SELECT COUNT(*) FROM order_details;

-- 5. Which orders had the most number of items?
SELECT order_id ,COUNT(item_id) AS num_items
FROM order_details
GROUP BY order_id
ORDER BY num_items DESC;

-- Which orders had the most number of items - LIST ONLY HIGHEST NUMBERS
SELECT order_id, COUNT(item_id) AS num_items
FROM order_details
GROUP BY order_id
HAVING COUNT(item_id) = (
    SELECT MAX(num_items) 
    FROM (SELECT order_id, COUNT(item_id) AS num_items
          FROM order_details
          GROUP BY order_id) AS subquery
);


-- 6. How many orders had more than 12 items?
SELECT order_id ,COUNT(item_id) AS num_items
FROM order_details
GROUP BY order_id
HAVING num_items > 12;

-- count the number of rows 
SELECT COUNT(*) FROM 
(SELECT order_id ,COUNT(item_id) AS num_items
FROM order_details
GROUP BY order_id
HAVING num_items > 12) AS num_orders;