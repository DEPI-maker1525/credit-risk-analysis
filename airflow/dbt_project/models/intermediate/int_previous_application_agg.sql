-- int_previous_applications_agg.sql
WITH prev_apps AS (
    SELECT * 
    FROM {{ ref('stg_previous_application') }}
),

client_level AS (
    SELECT
        client_id,

        COUNT(*)                                                        as total_previous_applications,
        COUNT(DISTINCT contract_type)                                   as unique_contract_types,

        SUM(CASE WHEN contract_status = 'Approved' THEN 1 ELSE 0 END)   as num_approved,
        SUM(CASE WHEN contract_status = 'Refused'  THEN 1 ELSE 0 END)   as num_refused,
        SUM(CASE WHEN contract_status = 'Canceled' THEN 1 ELSE 0 END)   as num_canceled,

        ROUND(AVG(monthly_loan_amount), 2)                              as avg_annuity_amount,

        ROUND(AVG(loan_amount_approved), 2)                             as avg_loan_amount,

        ROUND(AVG(goods_price), 2)                                      as avg_down_payment,

        {{ get_mode('stg_previous_application', 'reject_reason') }}     as most_contract_type,
        {{ get_mode('stg_previous_application', 'yield_group') }}       as most_yield_group,
        {{ get_mode('stg_previous_application', 'client_type') }}       as most_client_type,
        sum(is_insured) as total_is_insured
    FROM prev_apps
    GROUP BY client_id
)

SELECT * FROM client_level