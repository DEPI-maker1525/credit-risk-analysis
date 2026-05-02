-- stg_pos_cash_balance.sql
SELECT
    SK_ID_PREV                                      AS prev_credit_id,
    SK_ID_CURR                                      AS client_id,
    MONTHS_BALANCE                                  AS months_balance,
    COALESCE(CNT_INSTALMENT, 0)                     AS num_instalment,
    CNT_INSTALMENT_FUTURE                           AS num_instalment_future,
    NAME_CONTRACT_STATUS                            AS contract_status,
    SK_DPD_DEF                                      AS dpd_def
FROM {{ source('raw', 'pos_cash_balance') }}