import streamlit as st
import pandas as pd

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Loan Web App",
    page_icon="💳",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── Custom CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
  /* Google Font */
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');

  html, body, [class*="css"] { font-family: 'Inter', sans-serif; }

  /* Background */
  .stApp { background-color: #f4faf4; }

  /* Top header bar */
  .app-header {
    background: linear-gradient(135deg, #1a7f3c 0%, #2ecc71 100%);
    color: white;
    padding: 2rem 2.5rem 1.5rem;
    border-radius: 0 0 18px 18px;
    margin-bottom: 2rem;
    box-shadow: 0 4px 20px rgba(30,160,70,0.18);
  }
  .app-header h1 { margin: 0; font-size: 2.2rem; font-weight: 700; letter-spacing: -0.5px; }
  .app-header p  { margin: 0.3rem 0 0; opacity: 0.88; font-size: 1rem; }

  /* Section cards */
  .section-card {
    background: white;
    border-radius: 14px;
    padding: 1.6rem 1.8rem;
    margin-bottom: 1.4rem;
    border: 1px solid #d4edda;
    box-shadow: 0 2px 10px rgba(30,160,70,0.06);
  }
  .section-title {
    font-size: 1rem;
    font-weight: 700;
    color: #1a7f3c;
    text-transform: uppercase;
    letter-spacing: 0.8px;
    border-bottom: 2px solid #d4edda;
    padding-bottom: 0.5rem;
    margin-bottom: 1.1rem;
  }

  /* Field metadata badge */
  .field-meta {
    font-size: 0.72rem;
    color: #6c757d;
    margin-bottom: 0.15rem;
  }
  .field-meta span {
    background: #e8f5e9;
    color: #1a7f3c;
    border-radius: 4px;
    padding: 1px 6px;
    margin-right: 4px;
    font-weight: 600;
  }

  /* Submit button */
  div.stButton > button {
    background: linear-gradient(135deg, #1a7f3c, #2ecc71);
    color: white;
    border: none;
    border-radius: 10px;
    padding: 0.7rem 2.5rem;
    font-size: 1.05rem;
    font-weight: 600;
    cursor: pointer;
    width: 100%;
    transition: opacity .2s;
  }
  div.stButton > button:hover { opacity: 0.88; }

  /* Success box */
  .success-box {
    background: #e8f5e9;
    border-left: 5px solid #1a7f3c;
    border-radius: 10px;
    padding: 1.2rem 1.5rem;
    margin-top: 1.5rem;
  }
  .success-box h3 { color: #1a7f3c; margin-top: 0; }
</style>
""", unsafe_allow_html=True)

# ── Header ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="app-header">
  <h1>💳 Loan Web App</h1>
  <p>Complete the application form below. All fields are validated before submission.</p>
</div>
""", unsafe_allow_html=True)

# ── Helper: field meta label ──────────────────────────────────────────────────
def meta(dtype, rule=""):
    rule_html = f"<span>{rule}</span>" if rule else ""
    st.markdown(f'<div class="field-meta"><span>{dtype}</span>{rule_html}</div>', unsafe_allow_html=True)

# ── Form ──────────────────────────────────────────────────────────────────────
errors = {}
values = {}

with st.form("loan_form"):

    # ── SECTION 1: Basic Identity ─────────────────────────────────────────────
    st.markdown('<div class="section-card"><div class="section-title">1 · Basic Identity</div>', unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)

    with c1:
        meta("Integer", "Exactly 6 digits")
        loan_id = st.number_input("Loan ID", min_value=0, max_value=999999999, step=1, key="loan_id")
        values["loan_id"] = int(loan_id)

    with c2:
        meta("String", "Cash loans | Revolving loans")
        contract_type = st.selectbox("Contract Type", ["Cash loans", "Revolving loans"])
        values["contract_type"] = contract_type

    with c3:
        meta("String", "F | M")
        gender = st.selectbox("Gender", ["F", "M"])
        values["gender"] = gender

    c4, c5, c6 = st.columns(3)
    with c4:
        meta("String", "Y | N")
        own_car = st.selectbox("Own Car", ["N", "Y"])
        values["own_car"] = own_car

    with c5:
        meta("String", "Y | N")
        own_realty = st.selectbox("Own Realty", ["N", "Y"])
        values["own_realty"] = own_realty

    with c6:
        meta("Integer", "≥ 0")
        num_children = st.number_input("Number of Children", min_value=0, step=1)
        values["num_children"] = int(num_children)

    st.markdown('</div>', unsafe_allow_html=True)

    # ── SECTION 2: Financial Info ─────────────────────────────────────────────
    st.markdown('<div class="section-card"><div class="section-title">2 · Financial Information</div>', unsafe_allow_html=True)
    c1, c2, c3, c4 = st.columns(4)

    with c1:
        meta("Float", "Must be positive")
        annual_income = st.number_input("Annual Income", min_value=0.0, step=100.0, format="%.2f")
        values["annual_income"] = annual_income

    with c2:
        meta("Float", "Must be positive")
        total_loan_amount = st.number_input("Total Loan Amount", min_value=0.0, step=100.0, format="%.2f")
        values["total_loan_amount"] = total_loan_amount

    with c3:
        meta("Float", "Must be positive")
        monthly_loan_amount = st.number_input("Monthly Loan Amount", min_value=0.0, step=10.0, format="%.2f")
        values["monthly_loan_amount"] = monthly_loan_amount

    with c4:
        meta("Float", "Must be positive")
        goods_price = st.number_input("Goods Price", min_value=0.0, step=100.0, format="%.2f")
        values["goods_price"] = goods_price

    st.markdown('</div>', unsafe_allow_html=True)

    # ── SECTION 3: Personal Background ───────────────────────────────────────
    st.markdown('<div class="section-card"><div class="section-title">3 · Personal Background</div>', unsafe_allow_html=True)
    c1, c2, c3, c4 = st.columns(4)

    INCOME_TYPES = ['Pensioner','State servant','Working','Commercial associate',
                    'Unemployed','Student','Businessman','Maternity leave']
    EDUCATION_TYPES = ['Secondary / secondary special','Higher education',
                       'Lower secondary','Incomplete higher','Academic degree']
    FAMILY_STATUS = ['Married','Separated','Single / not married','Civil marriage','Widow','Unknown']
    HOUSING_TYPES = ['House / apartment','With parents','Rented apartment',
                     'Municipal apartment','Co-op apartment','Office apartment']

    with c1:
        meta("String", "Income type")
        income_type = st.selectbox("Income Type", INCOME_TYPES)
        values["income_type"] = income_type

    with c2:
        meta("String", "Education type")
        education_type = st.selectbox("Education Type", EDUCATION_TYPES)
        values["education_type"] = education_type

    with c3:
        meta("String", "Family status")
        family_status = st.selectbox("Family Status", FAMILY_STATUS)
        values["family_status"] = family_status

    with c4:
        meta("String", "Housing type")
        housing_type = st.selectbox("Housing Type", HOUSING_TYPES)
        values["housing_type"] = housing_type

    st.markdown('</div>', unsafe_allow_html=True)

    # ── SECTION 4: Days / Employment ─────────────────────────────────────────
    st.markdown('<div class="section-card"><div class="section-title">4 · Days & Employment</div>', unsafe_allow_html=True)
    c1, c2, c3, c4, c5 = st.columns(5)

    with c1:
        meta("Integer", "Must be negative")
        days_birth = st.number_input("Days Birth", max_value=-1, step=1, value=-1)
        values["days_birth"] = int(days_birth)

    with c2:
        meta("Integer", "Must be negative")
        days_employed = st.number_input("Days Employed", max_value=-1, step=1, value=-1)
        values["days_employed"] = int(days_employed)

    with c3:
        meta("Integer", "Must be negative")
        days_employed_clean = st.number_input("Days Employed (Clean)", max_value=-1, step=1, value=-1)
        values["days_employed_clean"] = int(days_employed_clean)

    with c4:
        meta("Integer", "Must be negative")
        days_id_publish = st.number_input("Days ID Publish", max_value=-1, step=1, value=-1)
        values["days_id_publish"] = int(days_id_publish)

    with c5:
        meta("Float", "Between 0 and 1")
        extra_sources = st.number_input("Extra Sources", min_value=0.0, max_value=1.0, step=0.01, format="%.3f")
        values["extra_sources"] = extra_sources

    st.markdown('</div>', unsafe_allow_html=True)

    # ── SECTION 5: Occupation & Region ───────────────────────────────────────
    st.markdown('<div class="section-card"><div class="section-title">5 · Occupation & Region</div>', unsafe_allow_html=True)

    OCCUPATION_TYPES = ['Laborers','Accountants','Realty agents','Cooking staff','Unknown','Sales staff',
                        'Core staff','Cleaning staff','Drivers','High skill tech staff','Waiters/barmen staff',
                        'Managers','Medicine staff','Security staff','Low-skill Laborers','Private service staff',
                        'Secretaries','IT staff','HR staff']
    ORG_TYPES = ['Business Entity Type 3','Business Entity Type 1','Realtor','Restaurant','XNA','Self-employed',
                 'Trade: type 7','Housing','School','Medicine','Business Entity Type 2','Government','Kindergarten',
                 'Other','Bank','Construction','Services','Military','Trade: type 3','Security','Industry: type 9',
                 'Industry: type 3','Transport: type 2','Industry: type 7','Transport: type 3','Security Ministries',
                 'Police','Transport: type 4','Trade: type 1','Postal','Legal Services','Industry: type 4',
                 'Trade: type 6','Insurance','Industry: type 11','Industry: type 1','Agriculture','Industry: type 2',
                 'Industry: type 12','Industry: type 5','Electricity','Trade: type 2','University','Telecom','Hotel',
                 'Emergency','Cleaning','Industry: type 10','Advertising','Culture','Transport: type 1',
                 'Industry: type 6','Mobile','Religion','Industry: type 13','Trade: type 4','Industry: type 8',
                 'Trade: type 5']

    c1, c2, c3 = st.columns(3)

    with c1:
        meta("String", "Occupation type")
        occupation_type = st.selectbox("Occupation Type", OCCUPATION_TYPES)
        values["occupation_type"] = occupation_type

    with c2:
        meta("Integer", "≥ 0")
        num_family_members = st.number_input("Num Family Members", min_value=0, step=1)
        values["num_family_members"] = int(num_family_members)

    with c3:
        meta("Integer", "1 | 2 | 3")
        region_rating_city = st.selectbox("Region Rating City", [1, 2, 3])
        values["region_rating_city"] = region_rating_city

    meta("String", "Organization type")
    organization_type = st.selectbox("Organization Type", ORG_TYPES)
    values["organization_type"] = organization_type

    st.markdown('</div>', unsafe_allow_html=True)

    # ── SECTION 6: Phone & Employment Anomaly ────────────────────────────────
    st.markdown('<div class="section-card"><div class="section-title">6 · Phone & Anomaly</div>', unsafe_allow_html=True)
    c1, c2 = st.columns(2)

    with c1:
        meta("Integer", "Must be negative")
        days_last_phone_change = st.number_input("Days Last Phone Change", max_value=-1, step=1, value=-1)
        values["days_last_phone_change"] = int(days_last_phone_change)

    with c2:
        meta("Integer", "0 | 1")
        is_employment_anomaly = st.selectbox("Is Employment Anomaly", [0, 1])
        values["is_employment_anomaly"] = is_employment_anomaly

    st.markdown('</div>', unsafe_allow_html=True)

    # ── SECTION 7: Bureau / Credit History ───────────────────────────────────
    st.markdown('<div class="section-card"><div class="section-title">7 · Bureau & Credit History</div>', unsafe_allow_html=True)
    c1, c2, c3, c4, c5 = st.columns(5)

    with c1:
        meta("Integer", "≥ 0")
        bureau_num_credits = st.number_input("Bureau Num Credits", min_value=0, step=1)
        values["bureau_num_credits"] = int(bureau_num_credits)

    with c2:
        meta("Integer", "≥ 0")
        num_active_credits = st.number_input("Num Active Credits", min_value=0, step=1)
        values["num_active_credits"] = int(num_active_credits)

    with c3:
        meta("Integer", "≥ 0")
        num_curr_overdue = st.number_input("Num Curr Overdue", min_value=0, step=1)
        values["num_curr_overdue"] = int(num_curr_overdue)

    with c4:
        meta("Integer", "≥ 0")
        num_overdue_credits = st.number_input("Num Overdue Credits", min_value=0, step=1)
        values["num_overdue_credits"] = int(num_overdue_credits)

    with c5:
        meta("Integer", "≥ 0")
        num_prolonged_credits = st.number_input("Num Prolonged Credits", min_value=0, step=1)
        values["num_prolonged_credits"] = int(num_prolonged_credits)

    c1, c2, c3, c4, c5 = st.columns(5)

    with c1:
        meta("Float", "≥ 0")
        total_debt = st.number_input("Total Debt", min_value=0.0, step=100.0, format="%.2f")
        values["total_debt"] = total_debt

    with c2:
        meta("Integer", "Must be positive")
        oldest_credit_days = st.number_input("Oldest Credit Days", min_value=1, step=1)
        values["oldest_credit_days"] = int(oldest_credit_days)

    with c3:
        meta("Integer", "Must be positive")
        newest_credit_days = st.number_input("Newest Credit Days", min_value=1, step=1)
        values["newest_credit_days"] = int(newest_credit_days)

    with c4:
        meta("Integer", "≥ 0")
        num_credits_last_year = st.number_input("Num Credits Last Year", min_value=0, step=1)
        values["num_credits_last_year"] = int(num_credits_last_year)

    with c5:
        meta("Integer", "≥ 0")
        num_long_term = st.number_input("Num Long Term", min_value=0, step=1)
        values["num_long_term"] = int(num_long_term)

    c1, c2 = st.columns(2)
    with c1:
        meta("Integer", "≥ 0")
        num_short_term = st.number_input("Num Short Term", min_value=0, step=1)
        values["num_short_term"] = int(num_short_term)

    with c2:
        meta("Integer", "≥ 0")
        num_business_credits = st.number_input("Num Business Credits", min_value=0, step=1)
        values["num_business_credits"] = int(num_business_credits)

    st.markdown('</div>', unsafe_allow_html=True)

    # ── SECTION 8: Previous Applications & Status ────────────────────────────
    st.markdown('<div class="section-card"><div class="section-title">8 · Previous Applications & Status</div>', unsafe_allow_html=True)

    COMMON_STATUS = ['X', '0', 'C', '1', '5', '2', 'Unknown/NaN']
    c1, c2, c3 = st.columns(3)

    with c1:
        meta("String", "Credit status")
        most_common_status = st.selectbox("Most Common Status", COMMON_STATUS)
        values["most_common_status"] = most_common_status if most_common_status != 'Unknown/NaN' else None

    with c2:
        meta("Integer", "≥ 0")
        has_high_risk_status = st.number_input("Has High Risk Status", min_value=0, step=1)
        values["has_high_risk_status"] = int(has_high_risk_status)

    with c3:
        meta("Integer", "≥ 0")
        total_prev_installments = st.number_input("Total Prev Installments", min_value=0, step=1)
        values["total_prev_installments"] = int(total_prev_installments)

    c1, c2, c3 = st.columns(3)

    with c1:
        meta("Float", "≥ 0")
        total_future_installments = st.number_input("Total Future Installments", min_value=0.0, step=1.0, format="%.2f")
        values["total_future_installments"] = total_future_installments

    with c2:
        meta("String", "Active | Closed")
        most_contract_type = st.selectbox("Most Contract Type", ["Active", "Closed"])
        values["most_contract_type"] = most_contract_type

    with c3:
        meta("Float", "≥ 0")
        total_dpd_def = st.number_input("Total DPD Def", min_value=0.0, step=1.0, format="%.2f")
        values["total_dpd_def"] = total_dpd_def

    st.markdown('</div>', unsafe_allow_html=True)

    # ── SECTION 9: Payment Metrics ───────────────────────────────────────────
    st.markdown('<div class="section-card"><div class="section-title">9 · Payment Metrics</div>', unsafe_allow_html=True)
    c1, c2, c3, c4 = st.columns(4)

    with c1:
        meta("Float", "Positive or negative")
        avg_delay = st.number_input("Avg Delay", step=0.01, format="%.2f")
        values["avg_delay"] = avg_delay

    with c2:
        meta("Integer", "≥ 0")
        late_count = st.number_input("Late Count", min_value=0, step=1)
        values["late_count"] = int(late_count)

    with c3:
        meta("Float", "≥ 0")
        total_paid = st.number_input("Total Paid", min_value=0.0, step=100.0, format="%.2f")
        values["total_paid"] = total_paid

    with c4:
        meta("Float", "≥ 0")
        total_remaining = st.number_input("Total Remaining", min_value=0.0, step=100.0, format="%.2f")
        values["total_remaining"] = total_remaining

    st.markdown('</div>', unsafe_allow_html=True)

    # ── SECTION 10: Application Counts ───────────────────────────────────────
    st.markdown('<div class="section-card"><div class="section-title">10 · Application Counts</div>', unsafe_allow_html=True)
    c1, c2, c3, c4, c5 = st.columns(5)

    with c1:
        meta("Integer", "≥ 0")
        total_previous_applications = st.number_input("Total Prev Applications", min_value=0, step=1)
        values["total_previous_applications"] = int(total_previous_applications)

    with c2:
        meta("Integer", "≥ 0")
        unique_contract_types = st.number_input("Unique Contract Types", min_value=0, step=1)
        values["unique_contract_types"] = int(unique_contract_types)

    with c3:
        meta("Integer", "≥ 0")
        num_approved = st.number_input("Num Approved", min_value=0, step=1)
        values["num_approved"] = int(num_approved)

    with c4:
        meta("Integer", "≥ 0")
        num_refused = st.number_input("Num Refused", min_value=0, step=1)
        values["num_refused"] = int(num_refused)

    with c5:
        meta("Integer", "≥ 0")
        num_canceled = st.number_input("Num Canceled", min_value=0, step=1)
        values["num_canceled"] = int(num_canceled)

    st.markdown('</div>', unsafe_allow_html=True)

    # ── SECTION 11: Averages ─────────────────────────────────────────────────
    st.markdown('<div class="section-card"><div class="section-title">11 · Averages</div>', unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)

    with c1:
        meta("Float", "≥ 0")
        avg_annuity_amount = st.number_input("Avg Annuity Amount", min_value=0.0, step=10.0, format="%.2f")
        values["avg_annuity_amount"] = avg_annuity_amount

    with c2:
        meta("Float", "≥ 0")
        avg_loan_amount = st.number_input("Avg Loan Amount", min_value=0.0, step=100.0, format="%.2f")
        values["avg_loan_amount"] = avg_loan_amount

    with c3:
        meta("Float", "≥ 0")
        avg_down_payment = st.number_input("Avg Down Payment", min_value=0.0, step=10.0, format="%.2f")
        values["avg_down_payment"] = avg_down_payment

    st.markdown('</div>', unsafe_allow_html=True)

    # ── Submit ────────────────────────────────────────────────────────────────
    submitted = st.form_submit_button("🚀 Submit Application")

# ── Post-submit validation ────────────────────────────────────────────────────
if submitted:
    errors = {}

    # loan_id: exactly 6 digits
    lid = str(int(values["loan_id"]))
    if len(lid) != 6:
        errors["loan_id"] = f"Loan ID must be exactly 6 digits (got {len(lid)})."

    # positive checks
    for field in ["annual_income", "total_loan_amount", "monthly_loan_amount", "goods_price"]:
        if values[field] <= 0:
            errors[field] = f"{field.replace('_', ' ').title()} must be greater than 0."

    # negative checks
    for field in ["days_birth", "days_employed", "days_employed_clean", "days_id_publish", "days_last_phone_change"]:
        if values[field] >= 0:
            errors[field] = f"{field.replace('_', ' ').title()} must be a negative number."

    # extra_sources range
    if not (0.0 <= values["extra_sources"] <= 1.0):
        errors["extra_sources"] = "Extra Sources must be between 0 and 1."

    # positive credit days
    for field in ["oldest_credit_days", "newest_credit_days"]:
        if values[field] <= 0:
            errors[field] = f"{field.replace('_', ' ').title()} must be positive."

    # ── Display errors ────────────────────────────────────────────────────────
    if errors:
        st.error("⚠️ Please fix the following errors before submitting:")
        for field, msg in errors.items():
            st.markdown(f"- **{field}**: {msg}")
    else:
        st.markdown("""
        <div class="success-box">
          <h3>✅ Application Submitted Successfully!</h3>
          <p>All fields passed validation. Here is a summary of the submitted data:</p>
        </div>
        """, unsafe_allow_html=True)

        # Display as a styled dataframe
        df = pd.DataFrame(list(values.items()), columns=["Field", "Value"])
        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True,
            column_config={
                "Field": st.column_config.TextColumn("Field", width="medium"),
                "Value": st.column_config.TextColumn("Value", width="large"),
            }
        )
