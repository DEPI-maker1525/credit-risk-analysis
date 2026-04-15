-- int_credit_card_balance_agg.sql

WITH credit_card AS (
    SELECT * 
    FROM {{ ref('stg_credit_card_balance') }}
),

client_level AS (
    SELECT
        client_id,
        COUNT(*)      AS months_observed,

        ROUND(AVG(credit_card_balance), 2)           AS avg_balance,
        MAX(credit_card_balance)                     AS max_balance,

        ROUND(AVG(credit_card_limit), 2)             AS avg_credit_limit,
        MAX(credit_card_limit)                       AS max_credit_limit,

        ROUND(AVG(CASE 
                WHEN credit_card_limit > 0 THEN credit_card_balance / credit_card_limit
            END))                                    AS avg_utilization_ratio,

        SUM(drawings_current)                        AS total_drawings,
        SUM(payment_total_current)                   AS total_payments_made,

        ROUND(AVG(total_receivable), 2)              AS avg_total_receivable,
        MAX(total_receivable)                        AS max_total_receivable,

        SUM(CASE WHEN dpd_def > 0 THEN 1 ELSE 0 END)      AS months_with_dpd,

        MAX(CASE WHEN credit_card_balance > credit_card_limit THEN 1 ELSE 0 END) AS ever_over_limit_flag

    FROM credit_card
    GROUP BY client_id
)

SELECT * FROM client_level