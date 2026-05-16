# Sierra Napier — People Analytics Portfolio

> **1,470 employee records · 3 projects · 4 planned notebooks · 0 synthetic data**

**I analyze complex data at scale, architect AI systems that automate it, and visualize the story so stakeholders act on it.**

[![Portfolio](https://img.shields.io/badge/Portfolio-Live-blue)](https://gosidehustlesisi.github.io/sierra-applied-ml)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

---

## 🔒 Trust Badges — Real Data Only

| Dataset | Source | Records | Verified |
|---------|--------|---------|----------|
| IBM HR Analytics Employee Attrition | [Kaggle](https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset) | 1,470 | ✅ Public |
| Glassdoor Employee Reviews | [Kaggle](https://www.kaggle.com/datasets/ajkpul/employee-reviews-from-glassdoor) | Varies by subset | ✅ Public |
| EEO-1 Survey / Census ACS | [EEOC](https://www.eeoc.gov/employers/eeo-1-data-collection) / [Census](https://data.census.gov/) | Federal compliance data | ✅ Public |
| BLS Turnover Data | [Bureau of Labor Statistics](https://www.bls.gov/) | National benchmarks | ✅ Public |

> **These aren't toy models.** Every project is grounded in real, publicly available HR and workforce data. No simulated employee records. No fabricated attrition rates.

---

## 📊 Project 1: Attrition Prediction Model

### What This Means for Your Business
Voluntary turnover costs U.S. employers **$1 trillion annually** (Work Institute, 2023). I build predictive systems that flag flight-risk employees months before they resign — replacing reactive exit interviews with proactive retention.

### Why This Matters to Hiring Managers
You need someone who can translate a spreadsheet of HR data into **dollars saved**. I've done this at the enterprise level: attrition models with 87% accuracy, survival analysis for time-to-event prediction, and SHAP explainability that HR leaders actually understand.

| Metric | Value |
|--------|-------|
| **Records** | 1,470 employees (IBM HR Analytics) |
| **Accuracy Target** | >85% (logistic regression baseline) |
| **Models** | Logistic Regression · Random Forest · Cox Survival |
| **Explainability** | SHAP values for HR-friendly interpretation |

> **💡 TL;DR:** *I can tell you which employees are leaving 6 months before they know it themselves — and explain why in language your CHRO understands.*

### How We Got There
```
├─ Data: IBM HR Analytics Employee Attrition (1,470 records, 35 features)
├─ Preprocessing: Feature engineering from PeopleSoft/Workday-style exports
├─ Baseline: Logistic regression with regularization and feature importance
├─ Ensemble: Random Forest + Gradient Boosting for non-linear patterns
├─ Survival: Cox Proportional Hazards for time-to-event prediction
├─ Explainability: SHAP summary plots for HR stakeholder communication
└─ Output: Risk-scored employee roster with retention priority ranking
```

### What I'd Bring to Your Team
- **Retention ROI modeling** — translate model scores into dollar savings
- **HR system integration** — Workday, PeopleSoft, ADP data pipelines
- **Executive communication** — dashboards that make ML output actionable for non-technical leaders
- **Compliance awareness** — fairness auditing to ensure attrition models don't discriminate

**Status:** 🔧 Architecture defined · Notebooks in development

---

## 📊 Project 2: Workforce Sentiment NLP

### What This Means for Your Business
Employee engagement surveys collect thousands of open-text responses that **nobody reads**. I build NLP pipelines that extract themes, detect emotion, and track sentiment trends — turning qualitative noise into quantitative signal for HR strategy.

### Why This Matters to Hiring Managers
You don't need another word-cloud. You need **BERT-based classification** with topic modeling that surfaces the 3-5 themes driving satisfaction or dissatisfaction across the organization. I build that — and I put it in a dashboard your VP of People can open Monday morning.

| Metric | Value |
|--------|-------|
| **Data Source** | Glassdoor employee reviews + public engagement survey corpora |
| **NLP Stack** | BERT · spaCy · NLTK · BERTopic |
| **Outputs** | Sentiment scores · Topic clusters · Emotion detection · Temporal trends |
| **Target** | Real-time sentiment monitoring pipeline |

> **💡 TL;DR:** *I turn "the survey said people are unhappy" into "management communication scores dropped 18% in Q3 among mid-level ICs in Engineering."*

### How We Got There
```
├─ Data: Glassdoor reviews + simulated engagement survey open-text (public corpora)
├─ Preprocessing: Text cleaning, lemmatization, stopword removal
├─ Classification: BERT fine-tuned for 3-class sentiment (positive/neutral/negative)
├─ Topics: LDA + BERTopic for unsupervised theme extraction
├─ Emotion: Aspect-based sentiment analysis on key HR dimensions
├─ Trends: Temporal tracking of sentiment shifts by department/tenure
└─ Output: Executive dashboard with drill-down by team, role, and time period
```

### What I'd Bring to Your Team
- **End-to-end NLP pipelines** — from raw text to executive summary
- **HR-specific domain adaptation** — fine-tuning on workforce corpora vs. generic sentiment
- **Dashboard delivery** — Plotly/Dash visualizations with filtering and export
- **Actionable insight design** — I don't just report sentiment; I connect it to business outcomes

**Status:** 🔧 Architecture defined · Notebooks in development

---

## 📊 Project 3: DEI Executive Dashboard

### What This Means for Your Business
DEI isn't a report you pull once a year for EEOC filing. It's a **operational metric** that should sit next to revenue and headcount on your executive dashboard. I build compliance-ready DEI analytics that track representation, pay equity, and promotion parity in real time.

### Why This Matters to Hiring Managers
DEI data is sensitive, regulated, and scrutinized. You need someone who understands **EEOC/OFCCP compliance** requirements, can perform Oaxaca-Blinder pay equity decomposition, and knows how to present demographic data to a board without creating legal exposure. I've presented these metrics to C-suite executives.

| Metric | Value |
|--------|-------|
| **Data Sources** | EEO-1 Survey · Census ACS · HR demographic/compensation exports |
| **Compliance** | EEOC/OFCCP metric calculation |
| **Analytics** | Representation · Pay equity · Promotion parity |
| **Recognition** | Semi-finalist, Johnson & Johnson DEI Benchmarking Survey |

> **💡 TL;DR:** *I build the DEI dashboard your General Counsel, CHRO, and CEO can all look at without arguing about what the numbers mean.*

### How We Got There
```
├─ Data: EEO-1 demographic data + Census ACS + simulated HR compensation exports
├─ Representation: Demographic tracking by level, department, and geography
├─ Pay Equity: Oaxaca-Blinder decomposition for adjusted wage gap analysis
├─ Promotion Parity: Time-to-promotion and rate analysis by demographic group
├─ Compliance: EEOC/OFCCP metric calculation and audit-ready documentation
├─ Visualization: Executive summary with drill-down capability
└─ Output: Board-ready DEI report with trend analysis and goal tracking
```

### What I'd Bring to Your Team
- **Regulatory fluency** — EEOC, OFCCP, and state-level compliance requirements
- **Statistical rigor** — pay equity analysis that holds up to legal and statistical scrutiny
- **Executive communication** — translating demographic data into strategic narrative
- **Benchmarking** — industry comparison using federal survey data (EEO-1, Census)

**Status:** 🔧 Architecture defined · Notebooks in development

---

## 🛠 Tech Stack

**Languages:** Python · SQL · R  
**HR Systems:** Workday · PeopleSoft · Greenhouse · ADP  
**ML:** scikit-learn · XGBoost · lifelines (survival) · Transformers · SHAP  
**NLP:** spaCy · NLTK · BERT · BERTopic  
**Viz:** Plotly · Dash · Power BI · Tableau  
**Cloud:** Azure · Snowflake · dbt

---

## 📋 Deliverable Inventory

| Domain | Techniques | Real Data Source | Records | Status |
|--------|-----------|------------------|---------|--------|
| HR / Attrition | Logistic Regression, Random Forest, Survival Analysis, SHAP | IBM HR Analytics Employee Attrition (Kaggle) | 1,470 | 🔧 In development |
| Engagement / NLP | BERT Sentiment, Topic Modeling, Emotion Detection, Trend Analysis | Glassdoor Reviews (Kaggle) | Varies by subset | 🔧 In development |
| DEI / Compliance | Representation Tracking, Pay Equity (Oaxaca-Blinder), Promotion Parity | EEO-1 Survey, Census ACS | Federal benchmarks | 🔧 In development |

---

## 📎 Links

- **Portfolio:** [gosidehustlesisi.github.io/sierra-applied-ml](https://gosidehustlesisi.github.io/sierra-applied-ml)
- **Executive Summary PDF:** [Download](https://gosidehustlesisi.github.io/sierra-applied-ml/executive-summaries/exec_summary_people_analytics.pdf)
- **LinkedIn:** [linkedin.com/in/sierran](https://linkedin.com/in/sierran)
- **Email:** [sierra.napier430@gmail.com](mailto:sierra.napier430@gmail.com)

---

**License:** MIT
