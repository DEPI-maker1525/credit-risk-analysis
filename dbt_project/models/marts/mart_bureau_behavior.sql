-- mart_bureau_behaviour
WITH application_base AS (
    SELECT * FROM {{ ref('int_application_base') }}
),
bureau_client AS (
    SELECT * FROM {{ ref('int_bureau_client_agg') }}
)
SELECT
    ap.loan_id AS client_id,
    ap.target,
    ap.annual_income,
    ap.total_loan_amount,
    ap.monthly_loan_amount,
    ap.income_type,
    ap.organization_type,
    b.bureau_num_credits,
    b.num_active_credits,
    b.num_curr_overdue,
    b.num_overdue_credits,
    b.num_prolonged_credits,
    b.total_debt,
    b.num_credits_last_year,
    b.num_long_term,
    b.num_short_term,
    b.num_business_credits,
    ROUND(ABS(b.oldest_credit_days) / 365.0, 1) AS oldest_credit_years,
    ROUND(ABS(b.newest_credit_days) / 365.0, 1) AS newest_credit_years,
    b.most_common_status,
    b.has_high_risk_status
FROM application_base ap
LEFT JOIN bureau_client b ON ap.loan_id = b.client_id
WHERE ap.target IS NOT NULL
