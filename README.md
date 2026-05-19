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

**3 projects · IBM HR Analytics · Glassdoor · EEO-1 · BLS** · **In Development**

</div>

---

## Verified Data Sources

<p align="center">
  <img src="https://img.shields.io/badge/IBM%20HR%20Analytics-Kaggle%20Dataset-009CDE?style=flat-square" alt="IBM HR" />
  <img src="https://img.shields.io/badge/Glassdoor-Compensation%20%26%20Reviews-2E7D32?style=flat-square" alt="Glassdoor" />
  <img src="https://img.shields.io/badge/EEO--1-Federal%20Diversity%20Data-8B0000?style=flat-square" alt="EEO-1" />
  <img src="https://img.shields.io/badge/BLS-Occupational%20Employment-1B4F72?style=flat-square" alt="BLS" />
  <img src="https://img.shields.io/badge/Status-IN%20DEVELOPMENT-f59e0b?style=flat-square" alt="In Development" />
</p>

---

## At a Glance

| Records | Sources | Projects | Charts | Categories |
|---------|---------|----------|--------|------------|
| **TBD** | **4** | **3** | **TBD** | **Attrition · Compensation · Diversity · Sentiment** |

---

## About This Work

**I work at the intersection of workforce data and organizational intelligence.** My background spans federal program analytics, people operations, and HR technology — but the throughline is always the same: I don't just collect HR data. I build the systems that predict attrition, benchmark pay, and measure inclusion.

**Career Arc:**
- **Federal Analytics (MPA/MPH)** → Program evaluation, FOIA compliance automation, capital portfolio governance
- **Applied ML Engineering** → Predictive maintenance, NLP pipelines, demand forecasting with real public datasets
- **People Analytics** → Workforce attrition modeling, compensation benchmarking, diversity analytics

**The constant:** Every project starts with a real dataset, ends with a deployable insight, and ships with full provenance.

---

---

# Project 1: Workforce Attrition Analysis

**Predictive modeling for employee turnover using IBM HR Analytics**

<p align="left">
  <img src="https://img.shields.io/badge/Source-IBM%20HR%20Analytics%20(Kaggle)-009CDE?style=flat-square" />
  <img src="https://img.shields.io/badge/Status-IN%20DEVELOPMENT-f59e0b?style=flat-square" />
</p>

---

### What This Means for Your Business

Employee turnover costs 50–200% of annual salary per departure. I build predictive models that identify at-risk employees before they submit their resignation — enabling proactive retention interventions rather than reactive backfill.

**Key business application:** HR retention strategy, succession planning, and workforce stability forecasting.

### Why This Matters to Hiring Managers

Most attrition models are black-box neural networks that HR can't explain to leadership. I build interpretable models — logistic regression with SHAP values, random forests with feature importance — that produce actionable, auditable insights.

---

**Metrics (Planned)**

| Dataset | Records | Features | Target | Techniques |
|---|---|---|---|---|
| **IBM HR Analytics** | **1,470 employees** | **35** | **Attrition (Yes/No)** | **Logistic Regression, Random Forest, XGBoost, SHAP** |

---

### Planned Analysis

- Load IBM HR Analytics dataset from Kaggle
- Engineer features: tenure, overtime ratio, satisfaction score composite, salary percentile
- Train interpretable classifiers with cross-validation
- Generate SHAP values for individual prediction explanation
- Build attrition risk dashboard with department-level breakdowns
- Identify top predictors: overtime, income, job satisfaction, years at company

**Tech stack:** Python · pandas · scikit-learn · XGBoost · SHAP · matplotlib

---

→ [Notebooks — Coming Soon](projects/workforce-attrition/notebooks/)

---

### What I'd Bring to Your Team

- **Predictive attrition modeling** with interpretable outputs
- **SHAP-based explanation** for individual risk scoring
- **Department-level dashboards** for targeted intervention

---

---

# Project 2: Compensation Benchmarking Engine

**Industry pay analysis using Glassdoor and BLS data**

<p align="left">
  <img src="https://img.shields.io/badge/Source-Glassdoor%20%2B%20BLS-2E7D32?style=flat-square" />
  <img src="https://img.shields.io/badge/Status-IN%20DEVELOPMENT-f59e0b?style=flat-square" />
</p>

---

### What This Means for Your Business

Compensation is the #1 driver of attrition and the #1 cost line item. I build benchmarking engines that compare your pay bands against market rates by role, location, and industry — not just national averages, but granular competitive positioning.

**Key business application:** Pay equity audits, offer calibration, and retention-adjusted compensation strategy.

### Why This Matters to Hiring Managers

Most compensation analyses use outdated salary surveys. I integrate live Glassdoor scraping with BLS Occupational Employment data to produce current, location-specific benchmarks. The output isn't a report — it's a decision tool.

---

**Metrics (Planned)**

| Sources | Roles | Locations | Metrics | Techniques |
|---|---|---|---|---|
| **Glassdoor + BLS** | **50+** | **MSA-level** | **Base, bonus, equity, total comp** | **Web scraping, outlier detection, percentile ranking** |

---

### Planned Analysis

- Scrape Glassdoor salary data for target roles and locations
- Merge with BLS OES wage data for validation and gap analysis
- Build percentile ranking engine (25th, 50th, 75th, 90th)
- Identify pay equity gaps by gender, ethnicity, and tenure
- Generate competitive positioning heatmaps by role × location
- Build interactive compensation dashboard

**Tech stack:** Python · requests · BeautifulSoup · pandas · matplotlib · BLS API

---

→ [Notebooks — Coming Soon](projects/compensation-benchmarking/notebooks/)

---

### What I'd Bring to Your Team

- **Live compensation benchmarking** with market-rate validation
- **Pay equity analysis** with statistical significance testing
- **Offer calibration** tools for recruiting and retention

---

---

# Project 3: Diversity & Inclusion Analytics

**EEO-1 compliance and workforce sentiment measurement**

<p align="left">
  <img src="https://img.shields.io/badge/Source-EEO--1%20%2B%20BLS-8B0000?style=flat-square" />
  <img src="https://img.shields.io/badge/Status-IN%20DEVELOPMENT-f59e0b?style=flat-square" />
</p>

---

### What This Means for Your Business

Diversity isn't a checkbox — it's a competitive advantage backed by data. I analyze EEO-1 filings and workforce sentiment to measure representation gaps, track progress against benchmarks, and identify intervention points where inclusion efforts will have the highest impact.

**Key business application:** DEI strategy, compliance reporting, and culture measurement.

### Why This Matters to Hiring Managers

Most DEI reports are static PDFs produced once a year. I build live dashboards that track representation by level, department, and time — with sentiment analysis from Glassdoor reviews to measure whether diversity translates to inclusion.

---

**Metrics (Planned)**

| Source | Records | Dimensions | Metrics | Techniques |
|---|---|---|---|---|
| **EEO-1 + BLS + Glassdoor** | **Federal filings + reviews** | **Race, gender, level, department** | **Representation, sentiment, turnover by group** | **NLP sentiment, cohort analysis, gap visualization** |

---

### Planned Analysis

- Download and parse EEO-1 Component 1 data (federal filing)
- Merge with BLS demographic data for industry benchmarking
- Scrape Glassdoor reviews for sentiment by demographic group
- Build representation pyramid (entry → exec) by race and gender
- Compute adverse impact ratios and statistical significance
- Generate inclusion scorecard with trend analysis

**Tech stack:** Python · pandas · NLP (VADER/ TextBlob) · matplotlib · EEO-1 data

---

→ [Notebooks — Coming Soon](projects/diversity-inclusion/notebooks/)

---

### What I'd Bring to Your Team

- **DEI measurement frameworks** with federal compliance alignment
- **Sentiment analysis** for culture and inclusion monitoring
- **Adverse impact analysis** for legal and audit readiness

---

---

## Data Provenance & Citations

| Project | Primary Source | Method | Records | Status |
|---|---|---|---|---|
| **Workforce Attrition** | IBM HR Analytics (Kaggle) | Dataset download | 1,470 employees | 🟡 In Development |
| **Compensation** | Glassdoor + BLS OES | Web scraping + API | 50+ roles, MSA-level | 🟡 In Development |
| **Diversity & Inclusion** | EEO-1 + BLS + Glassdoor | Federal filings + NLP | Federal + review data | 🟡 In Development |

**All planned data sources are real public datasets.** No synthetic records will be used. Every analysis will trace to a verifiable source.

---

## Quick Start

```bash
# Clone the repo
git clone https://github.com/gosidehustlesisi/sierra-people-analytics.git
cd sierra-people-analytics

# Install dependencies
pip install -r requirements.txt

# Notebooks coming soon
# jupyter notebook projects/workforce-attrition/notebooks/
# jupyter notebook projects/compensation-benchmarking/notebooks/
# jupyter notebook projects/diversity-inclusion/notebooks/
```

**Requirements:** `pip install pandas numpy matplotlib seaborn scikit-learn xgboost shap requests beautifulsoup4 nltk`

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

*People analytics in development — real data, real insights, coming soon.*

**Built with curiosity, rigor, and a lot of scikit-learn.**

</div>
