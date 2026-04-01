WITH averages AS (
    SELECT 
        AVG(AMT_CREDIT_SUM) AS avg_loan,
        AVG(AMT_CREDIT_SUM_OVERDUE) AS avg_overdue
    FROM {{ source('raw', 'bureau') }}
),

bureau_raw AS (
    SELECT
        SK_ID_CURR AS loan_id,
        SK_ID_BUREAU AS bureau_id,
        CREDIT_ACTIVE AS loan_active,
        DAYS_CREDIT AS days_loan,
        CREDIT_DAY_OVERDUE AS curr_loan_days_overdue,

        CASE
            WHEN DAYS_CREDIT_ENDDATE > 3650 THEN 3650
            WHEN DAYS_CREDIT_ENDDATE < -3650 THEN -3650
            WHEN DAYS_CREDIT_ENDDATE IS NULL AND CREDIT_ACTIVE = 'Active' THEN 9999
            WHEN DAYS_CREDIT_ENDDATE IS NULL AND CREDIT_ACTIVE != 'Active' THEN -9999
            ELSE DAYS_CREDIT_ENDDATE
        END AS days_loan_enddate_active,

        CASE
            WHEN DAYS_ENDDATE_FACT < -3650 THEN -3650
            ELSE DAYS_ENDDATE_FACT
        END AS days_loan_enddate_closed,

        CASE
            WHEN AMT_CREDIT_MAX_OVERDUE IS NULL OR AMT_CREDIT_MAX_OVERDUE = 0 THEN 0
            ELSE 1
        END AS has_overdue,

        COALESCE(AMT_CREDIT_MAX_OVERDUE, 0) AS max_overdue_amount,
        CNT_CREDIT_PROLONG AS num_loan_prolong,

        CASE
            WHEN AMT_CREDIT_SUM IS NULL THEN 0
            WHEN AMT_CREDIT_SUM > a.avg_loan THEN a.avg_loan
            ELSE AMT_CREDIT_SUM
        END AS former_loan_total,

        CASE
            WHEN AMT_CREDIT_SUM_DEBT < 0 THEN 0
            ELSE AMT_CREDIT_SUM_DEBT
        END AS loan_remainder_debt,

        CASE
            WHEN AMT_CREDIT_SUM_OVERDUE > a.avg_overdue THEN a.avg_overdue
            ELSE AMT_CREDIT_SUM_OVERDUE
        END AS curr_loan_overdue,

        CREDIT_TYPE AS loan_type,

        CASE
            WHEN DAYS_CREDIT_UPDATE > 0 THEN 0
            ELSE DAYS_CREDIT_UPDATE
        END as days_loan_update

    FROM {{ source('raw', 'bureau') }}
    CROSS JOIN averages a
)
SELECT *
FROM bureau_raw