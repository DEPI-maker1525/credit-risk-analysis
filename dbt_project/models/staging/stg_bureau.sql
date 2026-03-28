SELECT
    SK_ID_CURR as member_id,
    SK_ID_BUREAU as bureau_id,
    CREDIT_ACTIVE as loan_active,
    DAYS_CREDIT as days_loan,
    DAYS_CREDIT_ENDDATE as days_loan_enddate_active,
    DAYS_ENDDATE_FACT as days_loan_enddate_closed,
    AMT_CREDIT_MAX_OVERDUE as max_loan_overdue,
    CNT_CREDIT_PROLONG as num_loan_prolong,
    AMT_CREDIT_SUM as former_loan_total,
    AMT_CREDIT_SUM_DEBT as loan_remainder_debt,
    AMT_CREDIT_SUM_LIMIT as credit_limit,
    AMT_CREDIT_SUM_OVERDUE as current_loan_overdue,
    CREDIT_TYPE as loan_type,
    DAYS_CREDIT_UPDATE as days_loan_update,
    AMT_ANNUITY as monthly_loan_amount
from {{source('raw', 'bureau')}}


