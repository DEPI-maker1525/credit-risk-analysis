SELECT * from {{ ref('stg_application_train') }}
UNION ALL
SELECT 
    *,
    NULL AS target
FROM {{ ref('stg_application_test') }}