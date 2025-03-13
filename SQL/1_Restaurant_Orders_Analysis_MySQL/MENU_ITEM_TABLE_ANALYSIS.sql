USE restaurant_db;

-- 1. View the menuitems table 
SELECT * FROM menu_items;

-- 2. find the number of items on the menu
SELECT COUNT(*) FROM menu_items;

-- 3. What are the least and most expensive items on the menu
SELECT * FROM menu_items
ORDER BY price LIMIT 1;

SELECT * FROM menu_items
ORDER BY price DESC LIMIT 1;

-- 4. How manu Italian dishes are on the menu?
SELECT COUNT(*) FROM menu_items
WHERE category="Italian";

-- 5. what are the least and most expensive Italian dishes on the menu?
SELECT * FROM menu_items
WHERE category="Italian"
ORDER BY price LIMIT 1;

SELECT * FROM menu_items
WHERE category="Italian"
ORDER BY price DESC LIMIT 1;

-- 6. How manu dishes are in each category?
SELECT category,COUNT(menu_item_id) AS num_dishes 
FROM menu_items
GROUP BY category;

-- 7. what is the average dish price within each category?
SELECT category,AVG(price) AS num_dishes 
FROM menu_items
GROUP BY category;