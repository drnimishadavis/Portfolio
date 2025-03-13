-- 1. Combine the menu-items and order-details tables into a single table
SELECT * FROM menu_items;
SELECT * FROM order_details;

SELECT *
FROM order_details od LEFT JOIN menu_items mi
ON od.item_id=mi.menu_item_id;

-- 2. What were the least and most ordered items?
SELECT item_name,COUNT(order_details_id) AS num_purchases
FROM order_details od LEFT JOIN menu_items mi
ON od.item_id=mi.menu_item_id
GROUP BY item_name
ORDER BY num_purchases LIMIT 1;

SELECT item_name,COUNT(order_details_id) AS num_purchases
FROM order_details od LEFT JOIN menu_items mi
ON od.item_id=mi.menu_item_id
GROUP BY item_name
ORDER BY num_purchases DESC LIMIT 1;
-- Hamburger is the most ordered item. so must keep in menu.

-- what categoris were they in?
SELECT item_name,category,COUNT(order_details_id) AS num_purchases
FROM order_details od LEFT JOIN menu_items mi
ON od.item_id=mi.menu_item_id
GROUP BY item_name,category
ORDER BY num_purchases LIMIT 1;

SELECT item_name,category,COUNT(order_details_id) AS num_purchases
FROM order_details od LEFT JOIN menu_items mi
ON od.item_id=mi.menu_item_id
GROUP BY item_name,category
ORDER BY num_purchases DESC LIMIT 1;

-- 3. What were the top 5 orders that spentthe most money?
SELECT order_id,SUM(price) AS total_spend
FROM order_details od LEFT JOIN menu_items mi
ON od.item_id=mi.menu_item_id
GROUP BY order_id
ORDER BY total_spend DESC
LIMIT 5;

-- 4. View the details of the highest spend order.
SELECT *
FROM order_details od LEFT JOIN menu_items mi
ON od.item_id=mi.menu_item_id
WHERE order_id=440;
-- what insights can you gather from the result?
SELECT category,COUNT(item_id) AS num_items
FROM order_details od LEFT JOIN menu_items mi
ON od.item_id=mi.menu_item_id
WHERE order_id=440
GROUP BY category;
-- eventhough italian items not popular in menu.. but most highest spend order is italian items.so it should be on menu

-- 5. Bonus: view the details of the top 5 highest spend orders,what insights can you gather from thre result?
SELECT category,COUNT(item_id) AS num_items
FROM order_details od LEFT JOIN menu_items mi
ON od.item_id=mi.menu_item_id
WHERE order_id IN (440,2075,1957,330,2675)
GROUP BY category;
-- in TOP 5 highest spend order... italian items is more
SELECT order_id,category,COUNT(item_id) AS num_items
FROM order_details od LEFT JOIN menu_items mi
ON od.item_id=mi.menu_item_id
WHERE order_id IN (440,2075,1957,330,2675)
GROUP BY order_id,category;