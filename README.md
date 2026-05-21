<div align="center">

<img src="https://raw.githubusercontent.com/gosidehustlesisi/sierra-mobility-data/main/avatar.png" width="160" height="160" style="border-radius: 50%; border: 4px solid #8b5cf6; box-shadow: 0 0 30px rgba(139,92,246,0.3);" alt="Sierra Napier" />

# Sierra Napier

### **People Analytics Portfolio**

<p style="font-size: 1.1rem; color: #94a3b8; max-width: 600px; margin: 0 auto;">
I analyze workforce attrition patterns. I benchmark compensation across industries. I map diversity metrics and sentiment trends.
<br><br>
Real HR data. Zero synthetic records. Decision-ready outputs.
</p>

</div>

---

<div align="center">

**3 projects · 23 figures · IBM HR Analytics · Glassdoor Reviews · Real Data**

</div>

---

## Verified Data Sources

<p align="center">
  <img src="https://img.shields.io/badge/IBM%20HR%20Analytics-1%2C470%20employees-009CDE?style=flat-square" alt="IBM HR" />
  <img src="https://img.shields.io/badge/Glassdoor-1%2C000%20reviews-2E7D32?style=flat-square" alt="Glassdoor" />
  <img src="https://img.shields.io/badge/Status-LIVE-success?style=flat-square" alt="Live" />
</p>

---

## At a Glance

| Records | Sources | Projects | Figures | Categories |
|---------|---------|----------|---------|------------|
| **2,470** | **2** | **3** | **23** | **Attrition · DEI · Sentiment** |

---

## About This Work

**I work at the intersection of workforce data and organizational intelligence.** My background spans federal program analytics, people operations, and HR technology — but the throughline is always the same: I don't just collect HR data. I build the systems that predict attrition, benchmark pay, and measure inclusion.

**Career Arc:**
- **Federal Analytics (MPA/MPH)** → Program evaluation, FOIA compliance automation, capital portfolio governance
- **Applied ML Engineering** → Predictive maintenance, NLP pipelines, demand forecasting with real public datasets
- **People Analytics** → Workforce attrition modeling, compensation benchmarking, diversity analytics

**The constant:** Every project starts with a real dataset, ends with a deployable insight, and ships with full provenance.

---

## Project 1: Workforce Attrition Prediction

**Predictive modeling for employee turnover using IBM HR Analytics**

<p align="left">
  <img src="https://img.shields.io/badge/Source-IBM%20HR%20Analytics%20(Kaggle)-009CDE?style=flat-square" />
  <img src="https://img.shields.io/badge/Records-1%2C470%20employees-blue?style=flat-square" />
  <img src="https://img.shields.io/badge/Model%20AUC-0.757-success?style=flat-square" />
  <img src="https://img.shields.io/badge/Figures-9-success?style=flat-square" />
</p>

---

### What This Means for Your Business

Employee turnover costs 50–200% of annual salary per departure. This project builds predictive models that identify at-risk employees before they submit their resignation — enabling proactive retention interventions.

### Key Findings

| Metric | Value |
|--------|-------|
| **Overall Attrition Rate** | **16.1%** (237 of 1,470 employees) |
| **Highest Risk Department** | **Sales: 20.6%** |
| **Overtime Impact** | **30.5% attrition with overtime vs 10.4% without** |
| **Income Correlation** | Lower income = higher attrition risk |
| **Model AUC** | **0.757** (Random Forest with balanced classes) |

### Figures Generated

| Figure | Description |
|--------|-------------|
| `01_attrition_overview.png` | Overall attrition distribution + department breakdown |
| `02_attrition_demographics.png` | Attrition by age, gender, marital status, education |
| `03_attrition_job_factors.png` | Overtime, job role, level, travel impact |
| `04_attrition_satisfaction_compensation.png` | Satisfaction scores + income group analysis |
| `05_correlation_heatmap.png` | Full correlation matrix of numeric features |
| `06_feature_importance_rf.png` | Random Forest feature importance ranking |
| `07_model_performance.png` | Confusion matrix + ROC curve (AUC = 0.757) |
| `08_attrition_tenure_career.png` | Tenure, role duration, promotion gaps |
| `09_key_insights_summary.png` | Executive summary with all key metrics |

### Tech Stack

Python · pandas · scikit-learn · matplotlib · seaborn

---

→ [Notebooks & Code](projects/attrition-prediction-model/notebooks/)

---

### What I'd Bring to Your Team

- **Predictive attrition modeling** with interpretable outputs
- **Department-level risk dashboards** for targeted intervention
- **Feature importance analysis** to identify retention levers

---

---

## Project 2: DEI Executive Dashboard

**Diversity, equity & inclusion analytics on real workforce data**

<p align="left">
  <img src="https://img.shields.io/badge/Source-IBM%20HR%20Analytics-009CDE?style=flat-square" />
  <img src="https://img.shields.io/badge/Records-1%2C470%20employees-blue?style=flat-square" />
  <img src="https://img.shields.io/badge/Figures-7-success?style=flat-square" />
</p>

---

### What This Means for Your Business

DEI isn't a checkbox — it's a competitive advantage backed by data. This project analyzes real workforce demographics to measure representation gaps, pay equity, and retention parity across gender, age, and organizational level.

### Key Findings

| Metric | Value |
|--------|-------|
| **Gender Pay Gap** | **No significant gap detected** (p = 0.22) |
| **Male Mean Income** | $6,381 |
| **Female Mean Income** | $6,687 |
| **Female Attrition** | 14.8% |
| **Male Attrition** | 17.0% |
| **Sales Dept Diversity** | Most gender-balanced, highest attrition |

### Figures Generated

| Figure | Description |
|--------|-------------|
| `01_gender_representation.png` | Gender breakdown by department & job level |
| `02_pay_equity_analysis.png` | Income distributions + statistical t-test |
| `03_dei_attrition_retention.png` | Attrition by gender, department, level, age |
| `04_promotion_career_parity.png` | Promotion gaps, training equity, stock options |
| `05_worklife_satisfaction_demographics.png` | WLB, satisfaction, overtime by gender |
| `06_education_hiring_diversity.png` | Education field, level, marital status, commute |
| `07_executive_dei_scorecard.png` | One-page executive summary with all DEI KPIs |

### Honest Note on Pay Equity

The data shows **no statistically significant gender pay gap** in this dataset (t-test p = 0.22). This doesn't mean pay equity is perfect — it means the sample doesn't show a detectable difference. Real pay equity audits require larger samples and controls for role, tenure, and performance.

### Tech Stack

Python · pandas · scipy · matplotlib · seaborn

---

→ [Notebooks & Code](projects/dei-executive-dashboard/notebooks/)

---

### What I'd Bring to Your Team

- **DEI measurement frameworks** with statistical rigor
- **Pay equity analysis** with t-tests and cohort comparisons
- **Executive scorecards** for board-ready reporting

---

---

## Project 3: Workforce Sentiment NLP

**Employee sentiment analysis using 1,000 real Glassdoor reviews**

<p align="left">
  <img src="https://img.shields.io/badge/Source-Glassdoor%20Reviews-2E7D32?style=flat-square" />
  <img src="https://img.shields.io/badge/Records-1%2C000%20reviews-blue?style=flat-square" />
  <img src="https://img.shields.io/badge/Figures-7-success?style=flat-square" />
</p>

---

### What This Means for Your Business

Employee sentiment is a leading indicator of turnover, productivity, and employer brand. This project analyzes real Glassdoor reviews to extract themes, measure sentiment across dimensions, and identify what employees love and what drives them away.

### Key Findings

| Metric | Value |
|--------|-------|
| **Average Overall Rating** | **2.45 / 5.0** |
| **Recommend to Friend** | **46.8%** positive |
| **CEO Approval** | **44.8%** positive |
| **Top PROS Themes** | good, great, people, benefits, team |
| **Top CONS Themes** | management, people, work, company, culture |
| **Lowest Dimension** | Senior Leadership (2.12/5) |

### Figures Generated

| Figure | Description |
|--------|-------------|
| `01_rating_distribution_overview.png` | Overall, WLB, culture, compensation ratings |
| `02_rating_comparison_dimensions.png` | Average ratings by dimension + company heatmap |
| `03_sentiment_analysis_pros_cons.png` | Lexicon sentiment: positive/negative word counts |
| `04_top_themes_pros_cons.png` | Top 15 words in PROS vs CONS reviews |
| `05_employee_status_tenure.png` | Current vs former, tenure distribution, rating by tenure |
| `06_recommendation_approval_flags.png` | CEO approval, recommend, outlook flags |
| `07_key_insights_summary.png` | Executive summary with all sentiment KPIs |

### Tech Stack

Python · pandas · NLTK-style lexicon · matplotlib · seaborn

---

→ [Notebooks & Code](projects/workforce-sentiment-nlp/notebooks/)

---

### What I'd Bring to Your Team

- **Real-time sentiment monitoring** from review platforms
- **Theme extraction** from open-text feedback
- **Competitive benchmarking** against industry peers

---

---

## Data Provenance & Citations

| Project | Primary Source | Method | Records | Status |
|---|---|---|---|---|
| **Workforce Attrition** | IBM HR Analytics (Kaggle) | Direct download | 1,470 employees | ✅ Complete |
| **DEI Dashboard** | IBM HR Analytics (Kaggle) | Same dataset, DEI lens | 1,470 employees | ✅ Complete |
| **Sentiment NLP** | Glassdoor Reviews (Bright Data sample) | Direct download | 1,000 reviews | ✅ Complete |

**All data is real. Zero synthetic records. Every figure traces to a verifiable source.**

---

## Quick Start

```bash
# Clone the repo
git clone https://github.com/gosidehustlesisi/sierra-people-analytics.git
cd sierra-people-analytics

# Install dependencies
pip install pandas numpy matplotlib seaborn scikit-learn scipy

# Run figure generation
python projects/attrition-prediction-model/notebooks/generate_figures.py
python projects/dei-executive-dashboard/notebooks/generate_figures.py
python projects/workforce-sentiment-nlp/notebooks/generate_figures.py
```

**Requirements:** `pip install pandas numpy matplotlib seaborn scikit-learn scipy`

---

## Contact

**Sierra Napier** — Data Scientist · AI Architect · People Analytics

- 🌐 **Portfolio:** [gosidehustlesisi.github.io/sierra-applied-ml](https://gosidehustlesisi.github.io/sierra-applied-ml/)
- 💼 **Consulting:** [gosidehustlesisi.github.io/side-hustle.html](https://gosidehustlesisi.github.io/side-hustle.html)
- 📧 **Email:** book@baldbeautymua.com
- 💻 **GitHub:** [@gosidehustlesisi](https://github.com/gosidehustlesisi)

**Open to:** HR analytics consulting · People operations strategy · Workforce planning contracts

---

<div align="center">

*People analytics powered by real data. Zero synthetic records. Decision-ready insights.*

**Built with curiosity, rigor, and a lot of pandas.**

</div>
