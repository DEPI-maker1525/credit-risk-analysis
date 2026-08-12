# 🚀 End-to-End Workflow Credit Risk Analysis

## 📌 Project Overview

Financial institutions and banks face a major challenge in assessing whether a loan applicant is likely to repay a loan or become a **default client**. Incorrect credit decisions can lead to significant financial losses, increased risk exposure, and inefficient resource allocation.

This project presents a complete **End-to-End Credit Risk Analysis Workflow** that combines **Data Engineering**, **Business Intelligence**, and **Machine Learning** to support data-driven lending decisions.

The solution starts from raw data ingestion and transformation, moves through analytical reporting and visualization, and ends with an intelligent web application capable of predicting whether a client is likely to default on a loan.

---

## 🎯 Problem Statement

Banks and financial companies receive thousands of loan applications from customers with different financial backgrounds.

The main challenge is:

* Identifying high-risk applicants before approving loans.
* Reducing financial losses caused by loan defaults.
* Making credit decisions based on data rather than intuition.
* Providing fast and reliable risk assessment.

To address these challenges, we built a complete data-driven solution that automates the credit risk analysis process.

---

## 🏗️ Project Architecture

The project follows an End-to-End workflow consisting of four main stages:

### 1️⃣ Data Pipeline & ELT Process

We built a robust **ELT (Extract, Load, Transform)** pipeline to process the raw credit data.

#### Tasks:

* Extract data from the source dataset.
* Load raw data into the warehouse.
* Clean and transform the data using dbt tool.
* Handle missing values and inconsistencies.
* Create analytical datasets ready for reporting and machine learning.

---

### 2️⃣ Business Intelligence Dashboard

After transforming the data, we created an interactive **Power BI Dashboard** to provide valuable business insights.

#### Dashboard Features:

* Loan distribution analysis.
* Client demographic analysis.
* Default vs Non-Default comparison.
* Income and credit amount analysis.
* Risk segmentation.
* Interactive filters and drill-down capabilities.

📊 The dashboard enables stakeholders to explore credit risk patterns and make informed decisions.

---

### 3️⃣ Machine Learning Model

We developed a Machine Learning model to predict whether a client is likely to default on a loan.

#### ML Workflow:

* Data preprocessing.
* Feature engineering.
* Model training and evaluation.
* Performance comparison.
* Prediction generation.

---

### 4️⃣ Interactive Web Application

To make the solution accessible to end users, we developed an interactive web application.

#### Features:

* User-friendly interface.
* Input customer information.
* Real-time prediction.
* Display credit risk result instantly.
* Support decision-making for loan approval processes.

Check the web applciation [here](https://credit-loan-app-predictor.streamlit.app/#credit-risk-predictor)

---

## 📂 Dataset

This project uses the **Home Credit Default Risk Dataset** provided by Kaggle.

🔗 Dataset Link:

https://www.kaggle.com/competitions/home-credit-default-risk/overview

The dataset contains customer demographic, financial, and loan-related information used to predict repayment ability.

---

## 🚀 Business Impact

This solution helps financial institutions:

* Reduce loan default risk.
* Improve credit approval decisions.
* Automate risk assessment processes.
* Gain actionable insights through dashboards.
* Enhance operational efficiency.
* Support data-driven lending strategies.