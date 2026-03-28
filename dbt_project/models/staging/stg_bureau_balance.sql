SELECT
    SK_ID_BUREAU as bureau_id,
    MONTHS_BALANCE as months_balance,
    STATUS as status
FROM {{ source('raw', 'bureau_balance') }}