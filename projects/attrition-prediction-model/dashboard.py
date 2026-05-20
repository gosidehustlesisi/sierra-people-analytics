import streamlit as st

st.set_page_config(page_title="Attrition Prediction Model", layout="wide")

st.title("👤 Attrition Prediction Model")
st.caption("People Analytics | Workforce Retention Intelligence")

st.info("📊 Data download script in progress. Showing demo layout with expected visualizations.")

st.warning("This dashboard will display HR attrition data once the download pipeline is complete. Below is the planned structure.")

st.divider()

st.subheader("Expected KPIs")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Attrition Rate", "14.2%", delta="-2.1% YoY")
col2.metric("At-Risk Employees", "47", delta="+12")
col3.metric("Retention Cost Saved", "$1.2M", delta="+$340K")
col4.metric("Model Accuracy", "87.3%", delta="+3.5%")

st.divider()

st.subheader("Expected Visualizations")

chart_col1, chart_col2 = st.columns(2)
with chart_col1:
    st.markdown("**Chart: Attrition Risk Distribution**")
    st.empty()
    st.caption("Planned: Histogram of predicted attrition probabilities across workforce")
    
    st.markdown("**Chart: Feature Importance**")
    st.empty()
    st.caption("Planned: SHAP values / feature importance from predictive model")

with chart_col2:
    st.markdown("**Chart: Departmental Attrition Breakdown**")
    st.empty()
    st.caption("Planned: Bar chart of attrition rates by department")
    
    st.markdown("**Chart: Tenure vs. Attrition Correlation**")
    st.empty()
    st.caption("Planned: Scatter plot showing attrition probability by tenure and salary level")

st.divider()

with st.expander("📁 Project Structure (Planned)"):
    st.code("""
projects/attrition-prediction-model/
├── data/
│   └── hr_employee_attrition.csv       # Downloaded from IBM HR Analytics
├── notebooks/
│   └── attrition_model.ipynb           # EDA + model training
├── figures/
│   ├── risk_distribution.png
│   ├── feature_importance.png
│   ├── department_breakdown.png
│   └── tenure_analysis.png
├── dashboard.py                        # This file
└── model/
    └── attrition_classifier.pkl        # Trained scikit-learn model
""")

st.sidebar.caption("Built by Sierra Napier | gosidehustlesisi")
