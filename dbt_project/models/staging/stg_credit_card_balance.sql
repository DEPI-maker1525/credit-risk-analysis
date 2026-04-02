SELECT
    SK_ID_PREV as prev_bureau_id,
    SK_ID_CURR as loan_id,
    MONTHS_BALANCE as month_balance,
    CASE
        WHEN AMT_BALANCE < 0 THEN 0 
        WHEN AMT_BALANCE > AMT_CREDIT_LIMIT_ACTUAL THEN AMT_CREDIT_LIMIT_ACTUAL
        ELSE AMT_BALANCE
    END as credit_card_balance,
    AMT_CREDIT_LIMIT_ACTUAL as credit_card_limit,
    AMT_DRAWINGS_CURRENT as drawings_current,
    AMT_PAYMENT_TOTAL_CURRENT as credit_payment_current,
    AMT_TOTAL_RECEIVABLE as total_receivable,
    NAME_CONTRACT_STATUS as contract_status,
    SK_DPD_DEF as credit_days_past_due
FROM {{ source('raw', 'credit_card_balance') }}