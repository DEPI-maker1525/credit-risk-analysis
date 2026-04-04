SELECT
    SK_ID_PREV as prev_bureau_id,
    SK_ID_CURR as loan_id,
    MONTHS_BALANCE as months_balance,
    CASE
        WHEN AMT_BALANCE < 0 THEN 0
    MONTHS_BALANCE as month_balance,
    CASE
        WHEN AMT_BALANCE < 0 THEN 0 
        WHEN AMT_BALANCE > AMT_CREDIT_LIMIT_ACTUAL THEN AMT_CREDIT_LIMIT_ACTUAL
        ELSE AMT_BALANCE
    END as credit_card_balance,
    AMT_CREDIT_LIMIT_ACTUAL as credit_card_limit,
    CASE
        WHEN AMT_DRAWINGS_CURRENT < 0 THEN 0
        WHEN AMT_DRAWINGS_CURRENT > AMT_CREDIT_LIMIT_ACTUAL THEN AMT_CREDIT_LIMIT_ACTUAL
        ELSE AMT_DRAWINGS_CURRENT
    END as drawings_current,
    AMT_PAYMENT_TOTAL_CURRENT as credit_payment_current,
    CASE
        WHEN AMT_TOTAL_RECEIVABLE < 0 THEN 0
        WHEN AMT_TOTAL_RECEIVABLE > AMT_CREDIT_LIMIT_ACTUAL THEN AMT_CREDIT_LIMIT_ACTUAL
        ELSE AMT_TOTAL_RECEIVABLE
    END as total_receivable,
    AMT_DRAWINGS_CURRENT as drawings_current,
    AMT_PAYMENT_TOTAL_CURRENT as credit_payment_current,
    AMT_TOTAL_RECEIVABLE as total_receivable,
    NAME_CONTRACT_STATUS as contract_status,
    SK_DPD_DEF as credit_days_past_due
FROM {{ source('raw', 'credit_card_balance') }}