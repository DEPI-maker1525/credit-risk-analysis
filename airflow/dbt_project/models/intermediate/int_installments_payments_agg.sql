-- int_installments_payments_agg
WITH installment_payment AS (
    SELECT
        client_id,
        days_actual_payment - days_installment        AS day_delay,
        installment_amount,
        installment_amount - actual_payment           AS remaining
    FROM {{ ref('stg_installments_payments') }}
)
SELECT
    client_id,
    AVG(day_delay)                               AS avg_delay,
    COUNT(CASE WHEN day_delay > 0 THEN 1 END)    AS late_count,
    SUM(installment_amount)                      AS total_paid,
    SUM(remaining)                               AS total_remaining
FROM installment_payment
GROUP BY client_id