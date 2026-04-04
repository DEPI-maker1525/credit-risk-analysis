-- stg_credit_card_balance.sql
SELECT
    SK_ID_PREV                                      AS prev_credit_id,
    SK_ID_CURR                                      AS client_id,
    MONTHS_BALANCE                                  AS months_balance,
    ABS(AMT_BALANCE)                                AS credit_card_balance,
    AMT_CREDIT_LIMIT_ACTUAL                         AS credit_card_limit,
    ABS(AMT_DRAWINGS_CURRENT)                       AS drawings_current,
    AMT_PAYMENT_TOTAL_CURRENT                       AS payment_total_current,
    ABS(AMT_TOTAL_RECEIVABLE)                       AS total_receivable,
    NAME_CONTRACT_STATUS                            AS contract_status,
    SK_DPD_DEF                                      AS dpd_def
FROM {{ source('raw', 'credit_card_balance') }}