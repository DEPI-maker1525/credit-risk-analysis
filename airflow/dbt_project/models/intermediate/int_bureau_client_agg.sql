-- int bureau_client_agg
WITH transformed AS (
    SELECT
        client_id,
        bureau_id,
        CASE WHEN credit_active = 'Active' THEN 1 ELSE 0 END as is_bureau_active,
        ABS(days_credit) as days_credit,
        CASE WHEN credit_day_overdue > 0 THEN 1 ELSE 0 END as curr_overdue,
        has_overdue_flag,
        CASE WHEN num_credit_prolong > 0 THEN 1 ELSE 0 END as has_prolong_flag,
        COALESCE(credit_sum, 0) as credit_sum_debt,

        CASE
            WHEN credit_type IN ('Consumer credit', 'Credit card', 'Car loan', 'Mortgage', 'Microloan', 'Loan for business development') THEN credit_type
            ELSE 'Other' 
        END as credit_type,

        CASE
        WHEN credit_type IN ('Consumer credit', 'Credit card') THEN 'Short-term'
        WHEN credit_type IN ('Car loan', 'Mortgage') THEN 'Long-term'
        WHEN credit_type IN ('Microloan', 'Loan for business development') THEN 'Business'
        ELSE 'Other'
        END as credit_category,
        COALESCE(most_common_status, 'X') as most_common_status,
    
        CASE WHEN days_credit > -365 THEN 1 ELSE 0 END as credit_taken_last_year

    FROM {{ ref('stg_bureau') }}
    LEFT JOIN {{ ref('int_bureau_balance_per_credit_agg') }} USING (bureau_id)
),
bureau_aggregated AS (
    SELECT
        client_id,

        COUNT(*) AS bureau_num_credits,
        SUM(is_bureau_active) AS num_active_credits,
        SUM(curr_overdue) AS num_curr_overdue,
        SUM(has_overdue_flag) AS num_overdue_credits,
        SUM(has_prolong_flag) AS num_prolonged_credits,
        SUM(credit_sum_debt) AS total_debt,

        MAX(days_credit) AS oldest_credit_days,
        MIN(days_credit) AS newest_credit_days,

        SUM(credit_taken_last_year) AS num_credits_last_year,

        SUM(CASE WHEN credit_category = 'Long-term' THEN 1 ELSE 0 END) AS num_long_term,
        SUM(CASE WHEN credit_category = 'Short-term' THEN 1 ELSE 0 END) AS num_short_term,
        SUM(CASE WHEN credit_category = 'Business' THEN 1 ELSE 0 END) AS num_business_credits,

        MODE(most_common_status) AS most_common_status, 

        MAX(CASE WHEN most_common_status IN ('C', 'X', '0') THEN 0
                 WHEN most_common_status IN ('2', '1')      THEN 1
                 ELSE 2 END
        ) AS has_high_risk_status

    FROM transformed
    GROUP BY client_id
)

SELECT * FROM bureau_aggregated