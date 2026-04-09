<<<<<<< HEAD
-- int_application_base.sql
SELECT * FROM {{ ref('stg_application_train') }}
UNION ALL
SELECT
    *,
    NULL as target
FROM {{ ref('stg_application_test') }}