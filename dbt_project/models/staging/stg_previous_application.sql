<<<<<<< HEAD
SELECT
    SK_ID_PREV as prev_bureau_id,
    SK_ID_CURR as loan_id,
    CASE
        WHEN NAME_CONTRACT_TYPE == 'XNA' THEN 'Other'
        ELSE NAME_CONTRACT_TYPE
    END as contract_type,
    AMT_ANNUITY as monthly_loan_amount,
    CASE
        WHEN AMT_CREDIT IS NULL THEN 0
        ELSE AMT_CREDIT
    END as loan_amount_approved,
FROM {{ source('raw', 'previous_application') }}