SELECT
    SK_ID_PREV as prev_bureau_id,
    SK_ID_CURR as loan_id,
    NUM_INSTALMENT_VERSION as installment_version,
    NUM_INSTALMENT_NUMBER as installment_number,
    DAYS_INSTALMENT as days_installment,
    DAYS_ENTRY_PAYMENT as days_actual_payment,
    AMT_INSTALMENT as instalment_amount,
    AMT_PAYMENT as actual_payment
FROM {{ source('raw', 'installments_payments') }}

