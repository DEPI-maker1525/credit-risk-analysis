WITH avg_annuity_ratio AS (
    SELECT AVG(AMT_CREDIT / AMT_ANNUITY) as avg_ratio
    FROM {{ source('raw', 'application_train') }}
)
SELECT
    SK_ID_CURR as member_id,
    NAME_CONTRACT_TYPE as contract_type,
    CODE_GENDER as gender,
    FLAG_OWN_CAR as own_car,
    FLAG_OWN_REALTY as own_realty,
    CNT_CHILDREN as num_children,
    AMT_INCOME_TOTAL as annual_income,
    AMT_CREDIT as total_loan_amount,
    COALESCE(
        AMT_ANNUITY,
        AMT_CREDIT / (SELECT avg_ratio FROM avg_annuity_ratio)
    ) as monthly_loan_amount,
    (COALESCE(AMT_GOODS_PRICE, AMT_CREDIT)) as goods_price,
    NAME_INCOME_TYPE as job_type,
    NAME_EDUCATION_TYPE as education_type,
    NAME_FAMILY_STATUS as family_status,
    NAME_HOUSING_TYPE as housing_type,
    DAYS_BIRTH as age_day_application,
    DAYS_EMPLOYED as days_employed,
    DAYS_ID_PUBLISH as days_id_changed,
    OCCUPATION_TYPE as occupation_type,
    (COALESCE(CNT_FAM_MEMBERS, 0)) as num_family_members,
    REGION_RATING_CLIENT_W_CITY as region_rating_city,
    ORGANIZATION_TYPE as organization_type,
    (
        COALESCE(EXT_SOURCE_1, 0) +
        COALESCE(EXT_SOURCE_2, 0) +
        COALESCE(EXT_SOURCE_3, 0)
    ) / 3 as avg_external_sources,
    (COALESCE(DAYS_LAST_PHONE_CHANGE, 0)) as days_last_phone_change
FROM {{ source('raw', 'application_test') }}