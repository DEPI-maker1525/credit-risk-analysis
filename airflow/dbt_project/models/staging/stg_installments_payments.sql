-- stg_installments_payments.sql
SELECT
    SK_ID_PREV                                      AS prev_credit_id,
    SK_ID_CURR                                      AS client_id,
    NUM_INSTALMENT_VERSION                          AS installment_version,
    NUM_INSTALMENT_NUMBER                           AS installment_number,
    DAYS_INSTALMENT                                 AS days_installment,
    DAYS_ENTRY_PAYMENT                              AS days_actual_payment,
    AMT_INSTALMENT                                  AS installment_amount,
    AMT_PAYMENT                                     AS actual_payment
FROM {{ source('raw', 'installments_payments') }}