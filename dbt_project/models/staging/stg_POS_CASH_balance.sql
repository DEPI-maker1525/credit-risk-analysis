SELECT
    SK_ID_PREV as comp_bureau_id,
    SK_ID_CURR as member_id,
    MONTHS_BALANCE as months_balance,
    CNT_INSTALMENT as num_instalment,
    CNT_INSTALMENT_FUTURE as num_instalment_future,
    NAME_CONTRACT_STATUS as former_loan_status,
    SK_DPD_DEF as days_past_due
FROM {{ source('raw', 'pos_cash_balance') }}
