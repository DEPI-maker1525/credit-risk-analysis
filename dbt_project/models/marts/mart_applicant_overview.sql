-- mart_applicant_overview.sql
WITH application_base AS (
    SELECT * FROM {{ ref('int_application_base') }}
)
SELECT
    loan_id as client_id,
    target,
    contract_type,
    gender,
    own_car,
    own_realty,
    num_children,
    annual_income,
    total_loan_amount,
    monthly_loan_amount,
    goods_price,
    income_type,
    ROUND(ABS(days_birth) / 365.0, 0)    AS age,
    ROUND(ABS(days_employed) / 365.0, 1) AS years_employed,
    education_type,
    family_status,
    housing_type,
    occupation_type,
    num_family_members,
    organization_type,
    region_rating_city
FROM application_base
WHERE target IS NOT NULL