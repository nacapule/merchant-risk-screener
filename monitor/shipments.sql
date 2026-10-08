-- One row per shipped order: the day the platform learned of the shipment report and
-- the day it learned of the carrier's delivery confirmation, if any.
SELECT f.order_id, o.merchant_id,
       CAST(ROUND(o.amount * 100) AS SIGNED) AS amount_cents,
       DATE(MIN(f.known_at)) AS shipped_d,
       DATE(MIN(dl.known_at)) AS confirmed_d
FROM fulfilments f
JOIN orders o ON o.order_id = f.order_id
LEFT JOIN deliveries dl ON dl.order_id = f.order_id
GROUP BY f.order_id, o.merchant_id, o.amount
ORDER BY o.merchant_id, f.order_id;
