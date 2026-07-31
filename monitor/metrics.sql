-- Daily merchant health rollup for portfolio monitoring (AUP-06).
-- Point-in-time honest: chargebacks are attributed to the day they were OPENED
-- (not the order date — a monitor cannot see future disputes), and installment
-- failures to their due date. Chargeback rate is therefore a LAGGING indicator
-- here, exactly as in production; volume/ticket/new-buyer drift lead.
WITH orders_day AS (
  SELECT o.merchant_id, DATE(o.ts) AS d,
         COUNT(*) AS n_orders,
         ROUND(SUM(o.amount), 2) AS gmv,
         ROUND(AVG(o.amount), 2) AS avg_ticket,
         ROUND(AVG(u.signup_ts > o.ts - INTERVAL 30 DAY), 3) AS new_buyer_share
  FROM orders o JOIN users u ON u.user_id = o.user_id
  WHERE o.status = 'approved'
  GROUP BY o.merchant_id, DATE(o.ts)
),
cbs_day AS (
  SELECT o.merchant_id, DATE(cb.opened_ts) AS d, COUNT(*) AS n_cbs_opened
  FROM chargebacks cb JOIN orders o ON o.order_id = cb.order_id
  GROUP BY o.merchant_id, DATE(cb.opened_ts)
),
fails_day AS (
  SELECT o.merchant_id, DATE(i.due_ts) AS d, COUNT(*) AS n_inst_failed
  FROM installments i
  JOIN plans p ON p.plan_id = i.plan_id
  JOIN orders o ON o.order_id = p.order_id
  WHERE i.outcome IN ('failed', 'written_off')
  GROUP BY o.merchant_id, DATE(i.due_ts)
)
SELECT od.merchant_id, od.d, od.n_orders, od.gmv, od.avg_ticket, od.new_buyer_share,
       COALESCE(cb.n_cbs_opened, 0) AS n_cbs_opened,
       COALESCE(fd.n_inst_failed, 0) AS n_inst_failed
FROM orders_day od
LEFT JOIN cbs_day cb ON cb.merchant_id = od.merchant_id AND cb.d = od.d
LEFT JOIN fails_day fd ON fd.merchant_id = od.merchant_id AND fd.d = od.d
ORDER BY od.merchant_id, od.d;
