-- Evaluation only: the workbench's adjudicated basis for each disputed order.
-- 'none' means the order never received a positive label. The monitor never reads this.
SELECT o.merchant_id, DATE(cb.opened_ts) AS d, cb.reason,
       COALESCE((SELECT l.basis FROM labels l
                 WHERE l.order_id = cb.order_id AND l.label = 1
                 ORDER BY l.label_known_at LIMIT 1), 'none') AS basis
FROM chargebacks cb JOIN orders o ON o.order_id = cb.order_id
ORDER BY o.merchant_id, d, cb.chargeback_id;
