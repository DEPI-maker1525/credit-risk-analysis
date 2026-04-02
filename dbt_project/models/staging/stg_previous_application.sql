select 
    SK_ID_PREV as prev_bureau_id,
    SK_ID_CURR as loan_id,
    NAME_CONTRACT_TYPE as contract_type,
    AMT_ANNUITY as monthly_loan_amount,
    AMT_CREDIT as loan_amount_approved,
    AMT_GOODS_PRICE as goods_price,
    NAME_CASH_LOAN_PURPOSE as loan_purpose,
    NAME_CONTRACT_STATUS as contract_status,
    CODE_REJECT_REASON as reject_reason,
    NAME_YIELD_GROUP as installment_group,
    PRODUCT_COMBINATION as product_combination
from {{ source('raw', 'previous_application') }}
