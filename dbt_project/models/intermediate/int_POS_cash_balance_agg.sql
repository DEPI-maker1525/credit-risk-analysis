-- int_POS_cash_balance_agg
WITH pos_cash AS (
    SELECT * 
    FROM {{ ref('stg_POS_CASH_balance') }}
)
SELECT
    client_id,
    SUM(num_instalment)                                       AS total_prev_installments,
    SUM(COALESCE(num_instalment_future, 0))                   AS total_future_installments,
    {{ get_mode('stg_POS_CASH_balance', 'contract_status') }} AS most_contract_type,
    SUM(dpd_def)                                              AS total_dpd_def
FROM pos_cash
GROUP BY client_id