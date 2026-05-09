## Project 1: Attrition Prediction Model

**Context:** Workforce attrition prediction inspired by Akin Gump's 87% accuracy logistic regression models and WMATA's Azure ML attrition workflows.

**Dataset:**
- [IBM HR Analytics Employee Attrition dataset](https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset)
- Simulated PeopleSoft/Workday export data
- [Bureau of Labor Statistics turnover data](https://www.bls.gov/)

**Objective:** Build predictive models that identify employees at risk of voluntary departure with >85% accuracy, enabling proactive retention strategies.

**Techniques:**
- Logistic regression with feature importance analysis
- Random forest and gradient boosting classifiers
- Survival analysis (Cox PH) for time-to-event prediction
- SHAP explainability for HR-friendly model interpretation

**Business Impact:**
- 87% accuracy in attrition prediction
- 30% reduction in voluntary turnover
- Targeted retention strategies for high-risk profiles
- Executive-ready risk dashboards

**Files:**
- `notebooks/01_hr_data_exploration.ipynb`
- `notebooks/02_attrition_baseline.ipynb`
- `notebooks/03_advanced_models.ipynb`
- `notebooks/04_survival_analysis.ipynb`
- `src/preprocess.py`
- `src/train_attrition_model.py`
- `src/predict.py`
- `dashboard/attrition_dashboard.py`

**Status:** 🔧 In development
