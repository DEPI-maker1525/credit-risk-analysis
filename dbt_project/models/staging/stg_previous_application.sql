-- stg_previous_application.sql
SELECT
    SK_ID_PREV                                      AS prev_credit_id,
    SK_ID_CURR                                      AS client_id,
    NAME_CONTRACT_TYPE                              AS contract_type,
    AMT_ANNUITY                                     AS monthly_loan_amount,
    AMT_CREDIT                                      AS loan_amount_approved,
    AMT_GOODS_PRICE                                 AS goods_price,
    NAME_CASH_LOAN_PURPOSE                          AS loan_purpose,
    NAME_CONTRACT_STATUS                            AS contract_status,
    CODE_REJECT_REASON                              AS reject_reason,
    NAME_YIELD_GROUP                                AS yield_group,
    PRODUCT_COMBINATION                             AS product_combination,
    DAYS_DECISION                                   AS days_decision,
    NAME_PAYMENT_TYPE                               AS payment_type,
    NAME_CLIENT_TYPE                                AS client_type,
    NAME_GOODS_CATEGORY                             AS goods_category,
    NFLAG_INSURED_ON_APPROVAL                       AS is_insured 
FROM {{ source('raw', 'previous_application') }}