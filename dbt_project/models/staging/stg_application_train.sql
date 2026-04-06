-- stg_application_train.sql
WITH source AS (
    SELECT * 
    FROM {{ source('raw', 'application_train') }}
),
cleaned AS (
    SELECT
        SK_ID_CURR                                      AS loan_id,
        TARGET                                          AS target,
        NAME_CONTRACT_TYPE                              AS contract_type,
        CODE_GENDER                                     AS gender,
        FLAG_OWN_CAR                                    AS own_car,
        FLAG_OWN_REALTY                                 AS own_realty,
        CNT_CHILDREN                                    AS num_children,
        AMT_INCOME_TOTAL                                AS annual_income,
        AMT_CREDIT                                      AS total_loan_amount,
        AMT_ANNUITY                                     AS monthly_loan_amount,
        COALESCE(AMT_GOODS_PRICE, AMT_CREDIT)           AS goods_price,
        NAME_INCOME_TYPE                                AS income_type,
        NAME_EDUCATION_TYPE                             AS education_type,
        NAME_FAMILY_STATUS                              AS family_status,
        NAME_HOUSING_TYPE                               AS housing_type,
        DAYS_BIRTH                                      AS days_birth,
        DAYS_EMPLOYED                                   AS days_employed,
        CASE 
            WHEN DAYS_EMPLOYED = 365243 THEN NULL 
            ELSE DAYS_EMPLOYED 
        END                                             AS days_employed_clean,
        DAYS_ID_PUBLISH                                 AS days_id_publish,
        (COALESCE(EXT_SOURCE_1, 0) +
        COALESCE(EXT_SOURCE_2, 0) +
        COALESCE(EXT_SOURCE_3, 0)) / 3                  AS extra_sources,
        OCCUPATION_TYPE                                 AS occupation_type,
        COALESCE(CNT_FAM_MEMBERS, 0)                    AS num_family_members,
        ABS(REGION_RATING_CLIENT_W_CITY)                AS region_rating_city,
        ORGANIZATION_TYPE                               AS organization_type,
        COALESCE(DAYS_LAST_PHONE_CHANGE, 0)                          AS days_last_phone_change,

        CASE WHEN DAYS_EMPLOYED = 365243 THEN 1 ELSE 0 END AS is_employment_anomaly

    FROM source
)

SELECT * 
FROM cleaned