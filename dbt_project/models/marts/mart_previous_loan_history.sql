-- previous loan history mart
WITH application_base AS (
    SELECT * FROM {{ ref('int_application_base') }}
),
previous_application AS (
    SELECT * FROM {{ ref('int_previous_application_agg') }}
),
credit_card_balance AS (
    SELECT * FROM {{ ref('int_credit_card_balance_agg') }}
)
SELECT
    ap.loan_id,
    ap.target,
    ap.annual_income,
    ap.total_loan_amount,
    ap.monthly_loan_amount,
    ap.contract_type,
    ap.income_type,
    p.total_previous_applications,
    p.num_approved,
    p.num_refused,
    p.num_canceled,
    p.avg_annuity_amount,
    p.avg_loan_amount,
    p.avg_down_payment,
    p.most_contract_type,
    p.most_client_type,
    p.total_is_insured,
    c.months_observed,
    c.avg_balance,
    c.avg_credit_limit,
    c.avg_utilization_ratio,
    c.total_drawings,
    c.total_payments_made,
    c.months_with_dpd,
    c.ever_over_limit_flag,
    CASE
        WHEN avg_utilization_ratio >= 0.9 THEN 'Maxed Out'
        WHEN avg_utilization_ratio >= 0.6 THEN 'High Usage'
        WHEN avg_utilization_ratio >= 0.3 THEN 'Moderate Usage'
        ELSE 'Low Usage'
    END AS credit_card_segment
FROM application_base ap
LEFT JOIN previous_application p ON p.client_id = ap.loan_id
LEFT JOIN credit_card_balance c ON c.client_id = ap.loan_id
WHERE ap.target IS NOT NULL