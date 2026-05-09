## Project 3: DEI Executive Dashboard

**Context:** DEI metrics and compliance dashboard inspired by Akin Gump's executive DEI reporting and EEOC/OFCCP compliance work.

**Dataset:**
- [EEO-1 Survey data](https://www.eeoc.gov/employers/eeo-1-data-collection)
- [Census ACS demographic data](https://data.census.gov/)
- Simulated HR demographic and compensation data

**Objective:** Create an executive-ready DEI dashboard that tracks representation, pay equity, promotion parity, and compliance metrics across the organization.

**Techniques:**
- Demographic representation tracking by level/department
- Pay equity analysis (Oaxaca-Blinder decomposition)
- Promotion rate parity analysis
- EEOC/OFCCP compliance metric calculation
- Interactive executive summary with drill-down

**Business Impact:**
- Semi-finalist in Johnson & Johnson DEI Benchmarking Survey
- Executive visibility into inclusion metrics
- Compliance audit readiness
- Data-driven inclusion strategy informed by analytics

**Files:**
- `notebooks/01_demographic_analysis.ipynb`
- `notebooks/02_pay_equity.ipynb`
- `notebooks/03_promotion_parity.ipynb`
- `src/dei_metrics.py`
- `src/pay_equity_engine.py`
- `src/compliance_tracker.py`
- `dashboard/dei_executive_dashboard.py`

**Status:** 🔧 In development
