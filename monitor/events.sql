-- Event days survive even when there are no approved orders that day.
-- Each source uses the date on which the platform knew the event.
WITH events AS (
  SELECT o.merchant_id, DATE(o.ts) AS d, COUNT(*) AS n_orders,
         CAST(ROUND(SUM(o.amount) * 100) AS SIGNED) AS gmv_cents,
         SUM(u.signup_ts > o.ts - INTERVAL 30 DAY) AS n_new_orders,
         CAST(ROUND(SUM(CASE WHEN u.signup_ts > o.ts - INTERVAL 30 DAY
                            THEN o.amount ELSE 0 END) * 100) AS SIGNED) AS new_gmv_cents,
         0 AS n_disputes, 0 AS n_refunds
  FROM orders o JOIN users u ON u.user_id = o.user_id
  WHERE o.status = 'approved'
  GROUP BY o.merchant_id, DATE(o.ts)
  UNION ALL
  SELECT o.merchant_id, DATE(cb.opened_ts), 0, 0, 0, 0, COUNT(*), 0
  FROM chargebacks cb JOIN orders o ON o.order_id = cb.order_id
  GROUP BY o.merchant_id, DATE(cb.opened_ts)
  UNION ALL
  SELECT merchant_id, DATE(known_at), 0, 0, 0, 0, 0, COUNT(DISTINCT order_id)
  FROM cash_events
  WHERE kind = 'refund'
  GROUP BY merchant_id, DATE(known_at)
)
SELECT merchant_id, d,
       CAST(SUM(n_orders) AS SIGNED) AS n_orders,
       CAST(SUM(gmv_cents) AS SIGNED) AS gmv_cents,
       CAST(SUM(n_new_orders) AS SIGNED) AS n_new_orders,
       CAST(SUM(new_gmv_cents) AS SIGNED) AS new_gmv_cents,
       CAST(SUM(n_disputes) AS SIGNED) AS n_disputes,
       CAST(SUM(n_refunds) AS SIGNED) AS n_refunds
FROM events
GROUP BY merchant_id, d
ORDER BY merchant_id, d;
