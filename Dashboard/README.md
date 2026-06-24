# Credit Risk Dashboard Documentation

This document describes the four dashboard pages included in the credit risk analysis report. Each section starts with the dashboard image, followed by a concise explanation of the key metrics, charts, and business insights.

## CREDIT RISK OVERVIEW (Dashboard 1)

![Credit Risk Overview - Dashboard 1](images/page%201.png)

### Purpose

Dashboard 1 provides a high-level summary of portfolio risk, client profile indicators, and the strongest demographic drivers of default. It is designed as the opening page for quickly understanding the overall credit risk position.

### Key Performance Indicators

| Metric | Value | Interpretation |
| --- | ---: | --- |
| Total Clients | 307.511K | Total customer/application population covered by the analysis. |
| Avg Income | 168.80K | Average customer income across the portfolio. |
| Avg Loan | 599.03K | Average loan amount issued or requested. |
| Default Rate | 0.08 | Overall default ratio, equal to approximately 8%. |

### Charts and Metrics

- **Contract Default Rate**
  - Cash loans show a higher default rate than revolving loans.
  - This indicates that larger or longer-term cash loan products may require stronger screening and monitoring.

- **Family Status Default Rate**
  - Civil marriage and single/not married customers have the highest default rates.
  - Widowed customers show the lowest default risk among the displayed family-status groups.

- **Education Default Rate**
  - Lower secondary education is associated with the highest default rate.
  - Academic degree holders have the lowest default rate, suggesting education level is a useful risk segmentation variable.

- **Gender Default Rate**
  - Male clients account for a larger share of defaults than female clients.
  - This does not imply causation, but it highlights gender as a variable to monitor alongside income, contract type, and occupation.

- **Defaults Proportion**
  - Non-defaulted clients represent the vast majority of the portfolio.
  - Defaulted clients are a relatively small share, which is expected in a healthy lending portfolio but can still represent significant financial exposure.

- **Contract Type Proportion**
  - Cash loans dominate the portfolio at approximately 90.5%.
  - Revolving loans represent about 9.5%, making the portfolio heavily concentrated in cash lending.

- **Default Rate Based on Income Type**
  - Maternity leave and unemployed segments show the highest default rates.
  - Working, commercial associate, state servant, and pensioner categories show lower default levels.

### Main Insights

- Overall portfolio default is moderate at around 8%.
- Cash loans are both the largest contract type and a higher-risk category.
- Income source, education level, and family status are important default-risk indicators.
- The highest-risk customer groups should receive additional affordability checks and targeted credit policy review.

---

## CREDIT BUREAU & DEBT RISK ANALYSIS (Dashboard 2)

![Credit Bureau and Debt Risk Analysis - Dashboard 2](images/page%203.png)

### Purpose

Dashboard 2 focuses on bureau history, debt exposure, overdue behavior, and active credit obligations. It helps evaluate whether customers with existing debt records or overdue accounts show higher default probability.

### Key Performance Indicators

| Metric | Value | Interpretation |
| --- | ---: | --- |
| Avg Debt Ratio | 11.08 | Average debt ratio across customers with bureau information. |
| Total Active Credits | 541.92K | Total active credit records observed in bureau data. |
| Overdue Rate | 0.23 | Share or rate of overdue credit behavior in the analyzed bureau population. |

### Filters

- **Organization Type**
  - Allows users to isolate bureau risk by employer or organization category.
- **Income Type**
  - Allows comparison of debt and overdue behavior across customer income sources.

### Charts and Metrics

- **Default Rate by Total Overdues**
  - Default rate generally rises as total overdue count increases.
  - The chart peaks near higher overdue counts, showing that repeated historical delinquency is a strong warning signal.

- **Default Rate by Current Overdues**
  - Current overdue accounts show a sharp increase in default rate.
  - Customers with several active overdue obligations are much more likely to default.

- **Contract Default Rate**
  - Contract category 3 has the highest default rate among the displayed groups.
  - Lower categories show more moderate default behavior, suggesting contract-level bureau segmentation matters.

- **Default Rate Matrix**
  - Compares non-default and default customers across long-term credits, short-term credits, recent credits, active credits, and total debt.
  - Non-default customers account for most credit volume, but default customers still show meaningful exposure across active and recent credit lines.

### Main Insights

- Overdue history is one of the clearest bureau-based risk indicators.
- Current overdue obligations are especially important because they reflect active repayment stress.
- Customers with multiple open credits and high total debt should receive deeper debt-burden review.
- Bureau variables should be prioritized in credit scoring and policy rules because they directly capture repayment behavior.

---

## LOAN APPLICATION & CUSTOMER BEHAVIOR ANALYSIS (Dashboard 3)

![Loan Application and Customer Behavior Analysis - Dashboard 3](images/page%204.png)

### Purpose

Dashboard 3 summarizes previous application outcomes, repayment behavior, loan size, and annuity patterns. It helps explain how customer history and product structure relate to approval and repayment risk.

### Key Performance Indicators

| Metric | Value | Interpretation |
| --- | ---: | --- |
| Total Previous Applications | 1M | Total historical applications used for behavioral analysis. |
| Total Refused | 245.39K | Number of previously refused applications. |
| Total Approved | 886.10K | Number of previously approved applications. |

### Charts and Metrics

- **Repayment Segment Proportion**
  - Good payers represent the dominant segment at approximately 92.32%.
  - High-risk, slightly late, and frequently late customers form a much smaller share of the portfolio.
  - The repayment distribution suggests that most customers have acceptable repayment behavior, while a small segment requires focused monitoring.

- **Relation Between Annuity & Total Loan**
  - Average loan amount and average annuity are compared by target group.
  - The visual shows that loan size remains high across groups, while annuity levels differ between target categories.
  - This helps identify whether risk is more connected to repayment burden than loan amount alone.

- **Average Annuity Based on Target & Contract**
  - Cash loans have higher average annuity values than revolving loans.
  - The difference is visible for both target groups, suggesting contract type strongly affects repayment obligations.
  - Higher annuity levels can increase pressure on customers and should be evaluated against income.

### Main Insights

- Most previous applicants are good payers, but the high-risk minority is still important for loss prevention.
- Refused applications represent a sizable historical segment and may contain useful signals for future approval rules.
- Cash loans carry higher annuity obligations than revolving loans.
- Comparing annuity to income and loan amount is essential for assessing repayment affordability.

---

## CREDIT RISK OVERVIEW (Dashboard 4)

![Credit Risk Overview - Dashboard 4](images/page%202.png)

### Purpose

Dashboard 4 extends the credit risk overview with occupation, housing, ownership, age, work experience, and income-to-loan relationships. It is useful for identifying customer characteristics associated with higher default risk.

### Charts and Metrics

- **Occupation Default Rate**
  - Low-skill laborers have the highest default rate, approaching 0.17.
  - Drivers, waiters/bar staff, security staff, and laborers also show elevated risk.
  - Occupation appears to be a meaningful proxy for income stability and repayment capacity.

- **Housing Type Default Rate**
  - Customers in rented apartments show the highest default rate.
  - Customers living with parents also show elevated risk.
  - Office apartments and co-op apartments have lower default levels among the displayed housing categories.

- **Region Rate Default Rate**
  - Region 3 contributes the largest default share at approximately 47.2%.
  - Region 2 follows with about 32.8%, while Region 1 contributes around 20.0%.
  - Geographic region should be monitored as part of risk segmentation.

- **Own Realty Default Rate**
  - Customers who do not own realty represent a slightly higher default share than those who do.
  - Property ownership may indicate financial stability or available collateral strength.

- **Own Car Default Rate**
  - Customers without a car represent a slightly larger default share than car owners.
  - Car ownership may be a secondary indicator of financial capacity.

- **Age Default Rate**
  - Younger customers show higher default rates.
  - Default risk declines steadily as age increases, indicating that age is a strong behavioral risk factor.

- **Experience Default Rate**
  - Default rates are generally lower with more work experience.
  - A sharp spike appears at a specific high-experience point, which may require data-quality validation or investigation of a small segment.

- **Relation Between Loan Amount & Income**
  - The scatter chart compares median income and median loan amount by target group.
  - The non-default group shows a higher median income and higher median loan amount.
  - This suggests that stronger income can support larger loan exposure when affordability is maintained.

### Main Insights

- Default risk is higher among low-skill occupations, rented housing segments, younger clients, and customers with limited ownership indicators.
- Age and work experience show a clear relationship with repayment risk.
- Ownership of realty or a car may provide useful supporting signals, but should not be used alone.
- The portfolio should combine demographic, financial, and bureau indicators for a more reliable credit risk assessment.

---

## Overall Recommendations

- Strengthen approval checks for high-risk income types, low-skill occupations, rented housing segments, and customers with active overdue accounts.
- Use bureau overdue counts and current delinquency as major scoring inputs.
- Review cash loan pricing, limits, and affordability rules because cash loans dominate the portfolio and show higher risk in multiple views.
- Monitor younger customers and customers with limited work experience using additional income-stability indicators.
- Combine dashboard findings into a single risk framework covering affordability, credit history, customer profile, and repayment behavior.
