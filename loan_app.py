import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Credit Risk Predictor",
    page_icon="💳",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Green & White Theme ───────────────────────────────────────────────────────
st.markdown("""
<style>
/* ---------- global ---------- */
html, body, [data-testid="stAppViewContainer"] {
    background-color: #f0f7f0;
    color: #1a3a1a;
    font-family: 'Segoe UI', sans-serif;
}
[data-testid="stSidebar"] {
    background-color: #1b5e20;
    color: #ffffff;
}
[data-testid="stSidebar"] * {
    color: #ffffff !important;
}
/* ---------- header ---------- */
.main-header {
    background: linear-gradient(135deg, #2e7d32 0%, #1b5e20 100%);
    padding: 2rem 2.5rem;
    border-radius: 16px;
    margin-bottom: 2rem;
    box-shadow: 0 4px 20px rgba(27,94,32,0.25);
}
.main-header h1 { color: #ffffff; margin: 0; font-size: 2rem; }
.main-header p  { color: #c8e6c9; margin: 0.4rem 0 0; font-size: 1rem; }

/* ---------- section cards ---------- */
.section-card {
    background: #ffffff;
    border-radius: 12px;
    padding: 1.4rem 1.6rem;
    margin-bottom: 1.2rem;
    border-left: 5px solid #2e7d32;
    box-shadow: 0 2px 10px rgba(0,0,0,0.07);
}
.section-title {
    color: #1b5e20;
    font-size: 1.1rem;
    font-weight: 700;
    margin-bottom: 1rem;
    display: flex;
    align-items: center;
    gap: 0.5rem;
}

/* ---------- inputs ---------- */
[data-testid="stNumberInput"] input,
[data-testid="stSelectbox"] > div > div {
    border: 1.5px solid #a5d6a7 !important;
    border-radius: 8px !important;
    background: #f9fbe7 !important;
    color: #1a1a1a !important;
}
[data-testid="stNumberInput"] input:focus,
[data-testid="stSelectbox"] > div > div:focus-within {
    border-color: #2e7d32 !important;
    box-shadow: 0 0 0 2px rgba(46,125,50,0.2) !important;
}
/* selectbox selected value & dropdown options */
[data-testid="stSelectbox"] span,
[data-testid="stSelectbox"] div[role="option"],
[data-baseweb="select"] * {
    color: #1a1a1a !important;
}
/* number input arrows */
[data-testid="stNumberInput"] input::placeholder { color: #888 !important; }
[data-baseweb="input"] input { color: #1a1a1a !important; }
label { color: #2e7d32 !important; font-weight: 600 !important; font-size: 0.85rem !important; }

/* ---------- predict button ---------- */
div[data-testid="stButton"] > button {
    background: linear-gradient(135deg, #2e7d32, #1b5e20);
    color: white;
    border: none;
    padding: 0.75rem 3rem;
    font-size: 1.1rem;
    font-weight: 700;
    border-radius: 30px;
    width: 100%;
    transition: all 0.2s;
    box-shadow: 0 4px 15px rgba(46,125,50,0.4);
}
div[data-testid="stButton"] > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(46,125,50,0.5);
}

/* ---------- result boxes ---------- */
.result-approved {
    background: linear-gradient(135deg, #e8f5e9, #c8e6c9);
    border: 2px solid #2e7d32;
    border-radius: 16px;
    padding: 2rem;
    text-align: center;
}
.result-rejected {
    background: linear-gradient(135deg, #fce4ec, #f8bbd0);
    border: 2px solid #c62828;
    border-radius: 16px;
    padding: 2rem;
    text-align: center;
}
.result-icon   { font-size: 3.5rem; margin-bottom: 0.5rem; }
.result-label  { font-size: 1.8rem; font-weight: 800; margin-bottom: 0.3rem; }
.result-prob   { font-size: 1.1rem; opacity: 0.85; }
.prob-bar-wrap {
    background: #e0e0e0;
    border-radius: 20px;
    height: 18px;
    margin: 1rem auto;
    max-width: 380px;
    overflow: hidden;
}
.prob-bar-fill {
    height: 100%;
    border-radius: 20px;
    transition: width 0.8s ease;
}

/* ---------- footer ---------- */
.footer {
    text-align: center;
    color: #81c784;
    font-size: 0.8rem;
    margin-top: 2rem;
    padding-top: 1rem;
    border-top: 1px solid #c8e6c9;
}
</style>
""", unsafe_allow_html=True)

# ── Model loading ─────────────────────────────────────────────────────────────
MODEL_PATH = "ML/xgboost_pipeline"

@st.cache_resource(show_spinner="Loading model…")
def load_model(path: str):
    for ext in ["", ".pkl", ".joblib"]:
        full = path + ext
        if os.path.exists(full):
            return joblib.load(full)
    raise FileNotFoundError(
        f"Model not found at '{path}' (tried .pkl / .joblib). "
        "Make sure the ML/ folder is in the same directory as this script."
    )

try:
    model = load_model(MODEL_PATH)
    model_ok = True
except FileNotFoundError as e:
    model_ok = False
    model_error = str(e)

# ── Header ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="main-header">
  <h1>💳 Credit Risk Predictor</h1>
  <p>Fill in the applicant details below and click <strong>Predict</strong> to get a credit risk assessment.</p>
</div>
""", unsafe_allow_html=True)

if not model_ok:
    st.error(f"⚠️ {model_error}")
    st.info("The app will still render — fix the model path to enable predictions.")

# ── Helper ────────────────────────────────────────────────────────────────────
def section(icon: str, title: str):
    st.markdown(f'<div class="section-title">{icon} {title}</div>', unsafe_allow_html=True)

# ── Input form ────────────────────────────────────────────────────────────────
with st.form("prediction_form"):

    # ── 1 · Loan Information ────────────────────────────────────────────────
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    section("📄", "Loan Information")
    c1, c2, c3, c4 = st.columns(4)
    contract_type      = c1.selectbox("Contract Type",       ['Cash loans', 'Revolving loans'])
    total_loan_amount  = c2.number_input("Total Loan Amount",       min_value=0.0, value=100000.0, step=1000.0)
    monthly_loan_amount= c3.number_input("Monthly Loan Amount",     min_value=0.0, value=5000.0,  step=100.0)
    goods_price        = c4.number_input("Goods Price",             min_value=0.0, value=90000.0, step=1000.0)
    st.markdown('</div>', unsafe_allow_html=True)

    # ── 2 · Applicant Profile ───────────────────────────────────────────────
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    section("👤", "Applicant Profile")
    c1, c2, c3, c4 = st.columns(4)
    gender           = c1.selectbox("Gender",       ['M', 'F', 'XNA'])
    own_car          = c2.selectbox("Own Car",      ['Y', 'N'])
    own_realty       = c3.selectbox("Own Realty",   ['Y', 'N'])
    num_children     = c4.number_input("Number of Children",   min_value=0,   value=0, step=1)

    c1, c2, c3, c4 = st.columns(4)
    annual_income    = c1.number_input("Annual Income",        min_value=0.0, value=150000.0, step=1000.0)
    num_family_members= c2.number_input("Family Members",      min_value=0.0, value=2.0,     step=1.0)
    days_birth       = c3.number_input("Days Since Birth (neg)", max_value=0, value=-12000, step=1,
                                        help="Negative integer, e.g. -12000 means ~33 yrs old")
    days_id_publish  = c4.number_input("Days ID Published",   value=-2000.0, step=1.0,
                                        help="Days since ID was published (usually negative)")
    st.markdown('</div>', unsafe_allow_html=True)

    # ── 3 · Socio-Economic Status ───────────────────────────────────────────
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    section("🏠", "Socio-Economic Status")
    c1, c2, c3 = st.columns(3)
    income_type      = c1.selectbox("Income Type",    ['Working','State servant','Commercial associate','Pensioner','Student','Unemployed','Maternity leave','Businessman'])
    education_type   = c2.selectbox("Education Type", ['Secondary / secondary special','Lower secondary','Higher education','Incomplete higher','Academic degree'])
    family_status    = c3.selectbox("Family Status",  ['Married','Civil marriage','Separated','Single / not married','Widow','Unknown'])

    c1, c2, c3 = st.columns(3)
    housing_type     = c1.selectbox("Housing Type",   ['House / apartment','Office apartment','With parents','Rented apartment','Municipal apartment','Co-op apartment'])
    occupation_type  = c2.selectbox("Occupation Type",['Drivers','Sales staff','Unknown','Core staff','Managers','Accountants','Laborers','Medicine staff','Cleaning staff','Cooking staff','High skill tech staff','HR staff','Private service staff','Security staff','Waiters/barmen staff','Low-skill Laborers','Secretaries','IT staff','Realty agents'])
    organization_type= c3.selectbox("Organization Type",['Transport: type 3','Self-employed','Transport: type 2','Government','Business Entity Type 3','Other','Industry: type 4','Business Entity Type 2','Advertising','Security','XNA','Medicine','Kindergarten','Security Ministries','Military','Hotel','Agriculture','Electricity','Trade: type 7','Construction','Emergency','Mobile','School','Industry: type 9','Services','Business Entity Type 1','Industry: type 7','Trade: type 2','Restaurant','Trade: type 3','Bank','Industry: type 11','Postal','Transport: type 4','Industry: type 3','Trade: type 6','Police','University','Realtor','Cleaning','Industry: type 5','Industry: type 10','Housing','Industry: type 12','Insurance','Trade: type 1','Industry: type 1','Industry: type 2','Legal Services','Telecom','Culture','Trade: type 5','Trade: type 4','Industry: type 6','Religion','Industry: type 13','Transport: type 1','Industry: type 8'])
    st.markdown('</div>', unsafe_allow_html=True)

    # ── 4 · Employment & Region ─────────────────────────────────────────────
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    section("💼", "Employment & Region")
    c1, c2, c3, c4 = st.columns(4)
    days_employed        = c1.number_input("Days Employed (neg)",    value=-3000,  step=1,
                                            help="Negative = employed; positive = unemployed anomaly")
    days_employed_clean  = c2.number_input("Days Employed Clean",    value=-3000,  step=1,
                                            help="Cleaned version (Int64)")
    is_employment_anomaly= c3.number_input("Is Employment Anomaly",  min_value=0, max_value=1, value=0, step=1)
    region_rating_city   = c4.number_input("Region Rating (City)",   min_value=1, max_value=3, value=2, step=1)

    c1, c2 = st.columns(2)
    days_last_phone_change = c1.number_input("Days Last Phone Change", value=-500.0, step=1.0)
    extra_sources          = c2.number_input("Extra Sources (0–1)",    min_value=0.0, max_value=1.0, value=0.5, step=0.01,
                                              format="%.3f")
    st.markdown('</div>', unsafe_allow_html=True)

    # ── 5 · Bureau History ───────────────────────────────────────────────────
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    section("🏦", "Bureau Credit History")
    c1, c2, c3, c4 = st.columns(4)
    bureau_num_credits   = c1.number_input("Bureau # Credits",     min_value=0,   value=5,    step=1)
    num_active_credits   = c2.number_input("Active Credits",       min_value=0.0, value=2.0,  step=1.0)
    num_curr_overdue     = c3.number_input("Current Overdue",      min_value=0.0, value=0.0,  step=1.0)
    num_overdue_credits  = c4.number_input("Overdue Credits",      min_value=0.0, value=0.0,  step=1.0)

    c1, c2, c3, c4 = st.columns(4)
    num_prolonged_credits= c1.number_input("Prolonged Credits",    min_value=0.0, value=0.0,  step=1.0)
    total_debt           = c2.number_input("Total Debt",           min_value=0.0, value=0.0,  step=100.0)
    oldest_credit_days   = c3.number_input("Oldest Credit (days)", min_value=0,   value=1000, step=1)
    newest_credit_days   = c4.number_input("Newest Credit (days)", min_value=0,   value=100,  step=1)

    c1, c2, c3, c4 = st.columns(4)
    num_credits_last_year= c1.number_input("Credits Last Year",    min_value=0.0, value=1.0,  step=1.0)
    num_long_term        = c2.number_input("Long-Term Credits",    min_value=0.0, value=1.0,  step=1.0)
    num_short_term       = c3.number_input("Short-Term Credits",   min_value=0.0, value=1.0,  step=1.0)
    num_business_credits = c4.number_input("Business Credits",     min_value=0.0, value=0.0,  step=1.0)

    c1, c2 = st.columns(2)
    most_common_status   = c1.selectbox("Most Common Status", ['0', 'C', 'X', '1', '5', '2', '3', 'nan'])
    st.markdown('</div>', unsafe_allow_html=True)

    # ── 6 · Previous Applications ───────────────────────────────────────────
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    section("📋", "Previous Applications")
    c1, c2, c3, c4 = st.columns(4)
    total_prev_installments  = c1.number_input("Total Prev Installments",   min_value=0.0, value=0.0, step=1.0)
    total_future_installments= c2.number_input("Total Future Installments", min_value=0.0, value=0.0, step=1.0)
    most_contract_type       = c3.selectbox("Most Contract Type", ['Active', 'nan'])
    total_dpd_def            = c4.number_input("Total DPD Default",         min_value=0.0, value=0.0, step=1.0)

    c1, c2, c3, c4 = st.columns(4)
    avg_delay                = c1.number_input("Avg Delay (days)",          min_value=0.0, value=0.0, step=0.1)
    late_count               = c2.number_input("Late Count",                min_value=0,   value=0,   step=1)
    total_paid               = c3.number_input("Total Paid",                min_value=0.0, value=0.0, step=100.0)
    total_remaining          = c4.number_input("Total Remaining",           min_value=0.0, value=0.0, step=100.0)

    c1, c2, c3, c4 = st.columns(4)
    total_previous_applications= c1.number_input("Total Prev Applications", min_value=0, value=0, step=1)
    unique_contract_types      = c2.number_input("Unique Contract Types",   min_value=0, value=1, step=1)
    num_approved               = c3.number_input("Approved Applications",   min_value=0.0, value=0.0, step=1.0)
    num_refused                = c4.number_input("Refused Applications",    min_value=0.0, value=0.0, step=1.0)

    c1, c2, c3, c4 = st.columns(4)
    num_canceled               = c1.number_input("Canceled Applications",   min_value=0.0, value=0.0, step=1.0)
    avg_annuity_amount         = c2.number_input("Avg Annuity Amount",      min_value=0.0, value=0.0, step=100.0)
    avg_loan_amount            = c3.number_input("Avg Loan Amount",         min_value=0.0, value=0.0, step=100.0)
    avg_down_payment           = c4.number_input("Avg Down Payment",        min_value=0.0, value=0.0, step=100.0)

    c1, _ = st.columns([1, 3])
    total_is_insured           = c1.number_input("Total Is Insured",        min_value=0.0, value=0.0, step=1.0)
    st.markdown('</div>', unsafe_allow_html=True)

    # ── Submit ───────────────────────────────────────────────────────────────
    st.markdown("<br>", unsafe_allow_html=True)
    submitted = st.form_submit_button("🔍  Predict Credit Risk")

# ── Prediction ────────────────────────────────────────────────────────────────
if submitted:
    # Build DataFrame exactly matching training column order
    input_data = pd.DataFrame([{
        "contract_type":              contract_type,
        "gender":                     gender,
        "own_car":                    own_car,
        "own_realty":                 own_realty,
        "num_children":               int(num_children),
        "annual_income":              float(annual_income),
        "total_loan_amount":          float(total_loan_amount),
        "monthly_loan_amount":        float(monthly_loan_amount),
        "goods_price":                float(goods_price),
        "income_type":                income_type,
        "education_type":             education_type,
        "family_status":              family_status,
        "housing_type":               housing_type,
        "days_birth":                 int(days_birth),
        "days_employed":              int(days_employed),
        "days_employed_clean":        pd.array([int(days_employed_clean)], dtype="Int64")[0],
        "days_id_publish":            float(days_id_publish),
        "extra_sources":              float(extra_sources),
        "occupation_type":            occupation_type,
        "num_family_members":         float(num_family_members),
        "region_rating_city":         int(region_rating_city),
        "organization_type":          organization_type,
        "days_last_phone_change":     float(days_last_phone_change),
        "is_employment_anomaly":      int(is_employment_anomaly),
        "bureau_num_credits":         pd.array([int(bureau_num_credits)], dtype="Int64")[0],
        "num_active_credits":         float(num_active_credits),
        "num_curr_overdue":           float(num_curr_overdue),
        "num_overdue_credits":        float(num_overdue_credits),
        "num_prolonged_credits":      float(num_prolonged_credits),
        "total_debt":                 float(total_debt),
        "oldest_credit_days":         pd.array([int(oldest_credit_days)], dtype="Int64")[0],
        "newest_credit_days":         pd.array([int(newest_credit_days)], dtype="Int64")[0],
        "num_credits_last_year":      float(num_credits_last_year),
        "num_long_term":              float(num_long_term),
        "num_short_term":             float(num_short_term),
        "num_business_credits":       float(num_business_credits),
        "most_common_status":         None if most_common_status == "nan" else most_common_status,
        "total_prev_installments":    float(total_prev_installments),
        "total_future_installments":  float(total_future_installments),
        "most_contract_type":         None if most_contract_type == "nan" else most_contract_type,
        "total_dpd_def":              float(total_dpd_def),
        "avg_delay":                  float(avg_delay),
        "late_count":                 pd.array([int(late_count)], dtype="Int64")[0],
        "total_paid":                 float(total_paid),
        "total_remaining":            float(total_remaining),
        "total_previous_applications":pd.array([int(total_previous_applications)], dtype="Int64")[0],
        "unique_contract_types":      pd.array([int(unique_contract_types)], dtype="Int64")[0],
        "num_approved":               float(num_approved),
        "num_refused":                float(num_refused),
        "num_canceled":               float(num_canceled),
        "avg_annuity_amount":         float(avg_annuity_amount),
        "avg_loan_amount":            float(avg_loan_amount),
        "avg_down_payment":           float(avg_down_payment),
        "total_is_insured":           float(total_is_insured),
    }])

    if not model_ok:
        st.error("Cannot run prediction — model not loaded. Check the MODEL_PATH.")
    else:
        try:
            proba = model.predict_proba(input_data)[0]
            # Class 1 = default risk; class 0 = approved
            risk_prob    = float(proba[1])
            approve_prob = float(proba[0])
            prediction   = risk_prob >= 0.5          # True → HIGH RISK (rejected)

            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown("### 📊 Prediction Result")

            if not prediction:
                bar_color = "#2e7d32"
                st.markdown(f"""
                <div class="result-approved">
                  <div class="result-icon">✅</div>
                  <div class="result-label" style="color:#1b5e20;">APPROVED — Low Risk</div>
                  <div class="result-prob">Approval probability: <strong>{approve_prob*100:.1f}%</strong></div>
                  <div class="prob-bar-wrap">
                    <div class="prob-bar-fill" style="width:{approve_prob*100:.1f}%;background:{bar_color};"></div>
                  </div>
                  <div class="result-prob" style="font-size:0.9rem;color:#555;">
                    Risk probability: {risk_prob*100:.1f}%
                  </div>
                </div>
                """, unsafe_allow_html=True)
            else:
                bar_color = "#c62828"
                st.markdown(f"""
                <div class="result-rejected">
                  <div class="result-icon">❌</div>
                  <div class="result-label" style="color:#b71c1c;">REJECTED — High Risk</div>
                  <div class="result-prob">Risk probability: <strong>{risk_prob*100:.1f}%</strong></div>
                  <div class="prob-bar-wrap">
                    <div class="prob-bar-fill" style="width:{risk_prob*100:.1f}%;background:{bar_color};"></div>
                  </div>
                  <div class="result-prob" style="font-size:0.9rem;color:#555;">
                    Approval probability: {approve_prob*100:.1f}%
                  </div>
                </div>
                """, unsafe_allow_html=True)

            # Raw probabilities table
            with st.expander("🔬 Raw model output"):
                st.dataframe(pd.DataFrame({
                    "Outcome":     ["Approved (No Default)", "Rejected (Default)"],
                    "Probability": [f"{approve_prob*100:.4f}%", f"{risk_prob*100:.4f}%"],
                }), hide_index=True, use_container_width=True)

        except Exception as e:
            st.error(f"Prediction failed: {e}")
            st.exception(e)

# ── Footer ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="footer">
  Credit Risk Predictor · Powered by XGBoost · For internal use only
</div>
""", unsafe_allow_html=True)