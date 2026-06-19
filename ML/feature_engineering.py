"""
- 2. Feature Engineering
Feature engineering was performed to transform raw financial and behavioral information into more informative predictors.
The engineered features captured important customer risk signals and improved the predictive power of the final models
"""

from sklearn.base import BaseEstimator, TransformerMixin

class FeatureEngineering(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass

    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        X = X.copy()

        """Create New Features"""
        # age
        X['age'] = abs(X['days_birth']) / 365

        # employment years
        X['employment_years'] = (abs(X['days_employed_clean']) / 365).fillna(0)

        # loan to income ratio
        X['loan_income_ratio'] = X['total_loan_amount'] / (X['annual_income'] + 1)

        # monthly debt ratio
        X['monthly_debt_ratio'] = (X['monthly_loan_amount'] / ((X['annual_income'] / 12) + 1))

        # loan goods ratio
        X['loan_goods_ratio'] = X['total_loan_amount'] / (X['goods_price'] + 1)

        # Income per family member
        X['income_per_fam_member'] = X['annual_income'] / (X['num_family_members'] + 1)

        # active credit ratio
        X['active_credit_ratio'] = X['num_active_credits'] / (X['bureau_num_credits'] + 1)

        # overdue ratio
        X['overdue_ratio'] = X['num_overdue_credits'] / (X['bureau_num_credits'] + 1)

        # prolonged ratio
        X['prolonged_ratio'] = X['num_prolonged_credits'] / (X['bureau_num_credits'] + 1)

        # has history bureau
        X['has_bureau_history'] = (X['bureau_num_credits'] > 0).astype(int)

        # debt per credit
        X['debt_per_credit'] = X['total_debt'] / (X['bureau_num_credits'] + 1)

        # credit history years
        X['credit_history_years'] = (abs(X['oldest_credit_days']) / 365)

        # recency_credits ratio
        X['recency_credit_ratio'] = X['num_credits_last_year'] / (X['bureau_num_credits'] + 1)

        # total paid ratio
        X['payment_completion_ratio'] = (X['total_paid'] / (X['total_paid'] + X['total_remaining'] + 1))

        # total remaining ratio
        X['remaining_burden_ratio'] = (X['total_remaining'] / (X['total_paid'] + X['total_remaining'] + 1))

        # Approved ratio
        X['approval_ratio'] = (X['num_approved'] / (X['total_previous_applications'] + 1))

        # Refusal ratio
        X['refusal_ratio'] = (X['num_refused'] / (X['total_previous_applications'] + 1))

        # insurance ratio
        X['insurance_ratio'] = (X['total_is_insured'] / (X['total_previous_applications'] + 1))

        # down payment ratio
        X['down_payment_ratio'] = (X['avg_down_payment'] / (X['avg_loan_amount'] + 1))

        """Drop Features"""
        X = X.drop([
            'days_birth', 'days_employed', 'days_id_publish', 'days_last_phone_change','days_employed_clean',
            'most_common_status', 'organization_type'], axis=1)

        return X