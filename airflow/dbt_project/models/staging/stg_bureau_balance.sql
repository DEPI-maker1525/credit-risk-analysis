-- stg_bureau_balance.sql
SELECT
    SK_ID_BUREAU                         AS bureau_id,
    MONTHS_BALANCE                       AS months_balance,
    STATUS                               AS status
FROM {{ source('raw', 'bureau_balance') }}