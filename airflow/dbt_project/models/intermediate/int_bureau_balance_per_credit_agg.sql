-- int_bureau_balance_per_credit_agg
WITH ranked AS (
    SELECT
        bureau_id,
        status,
        COUNT(*) AS cnt,
        ROW_NUMBER() OVER (
            PARTITION BY bureau_id
            ORDER BY COUNT(*) DESC
        ) AS rn
    FROM {{ ref('stg_bureau_balance') }}
    GROUP BY bureau_id, status
)

SELECT
    bureau_id,
    status AS most_common_status
FROM ranked
WHERE rn = 1
