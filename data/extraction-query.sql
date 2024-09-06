SELECT *
FROM `bigquery-public-data.thelook_ecommerce.orders` AS ordini
LEFT JOIN (
    SELECT *
    FROM (
        SELECT *
        FROM `bigquery-public-data.thelook_ecommerce.order_items` AS orderItems
        LEFT JOIN `bigquery-public-data.thelook_ecommerce.products` AS product
        ON orderItems.product_id = product.id
    ) AS oddprod
    LEFT JOIN `bigquery-public-data.thelook_ecommerce.users` AS user
    ON oddprod.user_id = user.id
) AS bigquery
ON ordini.order_id = bigquery.order_id;
