-- stg_bureau.sql
WITH source AS (
    SELECT * 
    FROM {{ source('raw', 'bureau') }}
)
SELECT
    SK_ID_CURR                                      AS client_id,
    SK_ID_BUREAU                                    AS bureau_id,
    CREDIT_ACTIVE                                   AS credit_active,
    CREDIT_CURRENCY                                 AS credit_currency,
    DAYS_CREDIT                                     AS days_credit,
    CREDIT_DAY_OVERDUE                              AS credit_day_overdue,
    DAYS_CREDIT_ENDDATE                             AS days_credit_enddate,
    DAYS_ENDDATE_FACT                               AS days_enddate_fact,
    AMT_CREDIT_MAX_OVERDUE                          AS credit_max_overdue,
    CNT_CREDIT_PROLONG                              AS num_credit_prolong,
    AMT_CREDIT_SUM                                  AS credit_sum,
    ABS(AMT_CREDIT_SUM_DEBT)                        AS credit_sum_debt,
    ABS(AMT_CREDIT_SUM_LIMIT)                       AS credit_sum_limit,
    AMT_CREDIT_SUM_OVERDUE                          AS credit_sum_overdue,
    CREDIT_TYPE                                     AS credit_type,
    DAYS_CREDIT_UPDATE                              AS days_credit_update,
    
    CASE WHEN AMT_CREDIT_MAX_OVERDUE > 0 THEN 1 ELSE 0 END AS has_overdue_flag,
    CASE WHEN DAYS_CREDIT_ENDDATE IS NULL AND CREDIT_ACTIVE = 'Active' THEN 1 ELSE 0 END AS missing_enddate_active_flag

FROM source