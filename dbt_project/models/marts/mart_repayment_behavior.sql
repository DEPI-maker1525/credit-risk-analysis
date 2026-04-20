-- mart_repayment_behavior.sql
WITH application_base AS (
    SELECT * FROM {{ ref('int_application_base') }}
),
installment_payment AS (
    SELECT * FROM {{ ref('int_installments_payments_agg') }}
),
pos_cash AS (
    SELECT * FROM {{ ref('int_POS_cash_balance_agg') }}
)
SELECT
    ap.loan_id,
    ap.target,
    ap.annual_income,
    ap.total_loan_amount,
    ap.monthly_loan_amount,
    ap.contract_type,
    ap.income_type,
    ps.total_prev_installments,
    ps.total_future_installments,
    ps.most_contract_type,
    ps.total_dpd_def,
    i.avg_delay,
    i.late_count,
    i.total_paid,
    i.total_remaining,
    CASE 
        WHEN i.avg_delay <= 0 THEN 'Good Payer'
        WHEN i.avg_delay <= 5 THEN 'Slightly Late'
        WHEN i.avg_delay <= 15 THEN 'Frequently Late'
        ELSE 'High Risk'
    END AS repayment_segment
FROM application_base ap
LEFT JOIN pos_cash ps ON ps.client_id = ap.loan_id
LEFT JOIN installment_payment i ON i.client_id = ap.loan_id
WHERE ap.target IS NOT NULL