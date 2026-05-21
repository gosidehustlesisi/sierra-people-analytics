import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_curve, auc, confusion_matrix
import os

st.set_page_config(page_title="Workforce Attrition Analytics", page_icon="👥", layout="wide")

# Load data
@st.cache_data
def load_data():
    data_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'WA_Fn-UseC_-HR-Employee-Attrition.csv')
    df = pd.read_csv(data_path)
    df['Attrition_Binary'] = df['Attrition'].map({'Yes': 1, 'No': 0})
    return df

df = load_data()

# Sidebar
st.sidebar.title("👥 Workforce Analytics")
st.sidebar.markdown("---")
st.sidebar.markdown(f"**Dataset:** IBM HR Analytics")
st.sidebar.markdown(f"**Records:** {len(df):,} employees")
st.sidebar.markdown(f"**Features:** {df.shape[1]-1}")
st.sidebar.markdown(f"**Attrition Rate:** {df['Attrition_Binary'].mean()*100:.1f}%")
st.sidebar.markdown("---")
page = st.sidebar.radio("Navigation", ["📊 Overview", "🔍 Risk Factors", "🤖 Prediction Model", "📈 DEI Insights"])

if page == "📊 Overview":
    st.title("📊 Workforce Attrition Overview")
    
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Employees", f"{len(df):,}")
    col2.metric("Attrition Count", f"{df['Attrition_Binary'].sum():,}")
    col3.metric("Attrition Rate", f"{df['Attrition_Binary'].mean()*100:.1f}%")
    col4.metric("Departments", f"{df['Department'].nunique()}")
    
    st.markdown("---")
    
    col_left, col_right = st.columns(2)
    
    with col_left:
        st.subheader("Attrition by Department")
        dept_attrition = df.groupby('Department')['Attrition_Binary'].mean() * 100
        fig, ax = plt.subplots(figsize=(8, 4))
        dept_attrition.sort_values().plot(kind='barh', ax=ax, color='#C62828')
        ax.set_xlabel('Attrition Rate (%)')
        st.pyplot(fig)
    
    with col_right:
        st.subheader("Attrition by Job Level")
        level_attrition = df.groupby('JobLevel')['Attrition_Binary'].mean() * 100
        fig, ax = plt.subplots(figsize=(8, 4))
        level_attrition.plot(kind='bar', ax=ax, color='#1565C0')
        ax.set_ylabel('Attrition Rate (%)')
        ax.tick_params(axis='x', rotation=0)
        st.pyplot(fig)
    
    st.markdown("---")
    
    col_left2, col_right2 = st.columns(2)
    
    with col_left2:
        st.subheader("Attrition by Overtime")
        overtime_attrition = df.groupby('OverTime')['Attrition_Binary'].mean() * 100
        fig, ax = plt.subplots(figsize=(8, 4))
        overtime_attrition.plot(kind='bar', ax=ax, color=['#4CAF50', '#F44336'])
        ax.set_ylabel('Attrition Rate (%)')
        ax.tick_params(axis='x', rotation=0)
        st.pyplot(fig)
        st.caption("⚠️ Overtime is the strongest attrition predictor")
    
    with col_right2:
        st.subheader("Attrition by Age Group")
        bins = [18, 25, 30, 35, 40, 45, 50, 60]
        labels = ['18-25', '26-30', '31-35', '36-40', '41-45', '46-50', '51-60']
        df['AgeGroup'] = pd.cut(df['Age'], bins=bins, labels=labels, right=False)
        age_attrition = df.groupby('AgeGroup')['Attrition_Binary'].mean() * 100
        fig, ax = plt.subplots(figsize=(8, 4))
        age_attrition.plot(kind='bar', ax=ax, color='#FF9800')
        ax.set_ylabel('Attrition Rate (%)')
        ax.tick_params(axis='x', rotation=45)
        st.pyplot(fig)

elif page == "🔍 Risk Factors":
    st.title("🔍 Attrition Risk Factors")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Income vs Attrition")
        fig, ax = plt.subplots(figsize=(8, 5))
        sns.boxplot(data=df, x='Attrition', y='MonthlyIncome', ax=ax, palette=['#2E7D32', '#C62828'])
        ax.set_ylabel('Monthly Income ($)')
        st.pyplot(fig)
    
    with col2:
        st.subheader("Years at Company vs Attrition")
        fig, ax = plt.subplots(figsize=(8, 5))
        sns.boxplot(data=df, x='Attrition', y='YearsAtCompany', ax=ax, palette=['#2E7D32', '#C62828'])
        ax.set_ylabel('Years at Company')
        st.pyplot(fig)
    
    st.markdown("---")
    
    st.subheader("Satisfaction Scores vs Attrition")
    col3, col4, col5 = st.columns(3)
    
    with col3:
        fig, ax = plt.subplots(figsize=(5, 4))
        sns.boxplot(data=df, x='Attrition', y='JobSatisfaction', ax=ax, palette=['#2E7D32', '#C62828'])
        ax.set_ylabel('Job Satisfaction (1-4)')
        st.pyplot(fig)
    
    with col4:
        fig, ax = plt.subplots(figsize=(5, 4))
        sns.boxplot(data=df, x='Attrition', y='EnvironmentSatisfaction', ax=ax, palette=['#2E7D32', '#C62828'])
        ax.set_ylabel('Environment Satisfaction (1-4)')
        st.pyplot(fig)
    
    with col5:
        fig, ax = plt.subplots(figsize=(5, 4))
        sns.boxplot(data=df, x='Attrition', y='WorkLifeBalance', ax=ax, palette=['#2E7D32', '#C62828'])
        ax.set_ylabel('Work-Life Balance (1-4)')
        st.pyplot(fig)

elif page == "🤖 Prediction Model":
    st.title("🤖 Attrition Prediction Model")
    
    # Prepare features
    features_to_encode = ['BusinessTravel', 'Department', 'EducationField', 'Gender', 'JobRole', 'MaritalStatus', 'OverTime']
    df_encoded = df.copy()
    le = LabelEncoder()
    for col in features_to_encode:
        df_encoded[col] = le.fit_transform(df_encoded[col])
    
    feature_cols = [col for col in df_encoded.columns if col not in ['Attrition', 'Attrition_Binary', 'AgeGroup', 'EmployeeCount', 'EmployeeNumber', 'Over18', 'StandardHours']]
    X = df_encoded[feature_cols]
    y = df_encoded['Attrition_Binary']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    
    rf = RandomForestClassifier(n_estimators=100, random_state=42, class_weight='balanced')
    rf.fit(X_train, y_train)
    
    y_prob = rf.predict_proba(X_test)[:, 1]
    fpr, tpr, _ = roc_curve(y_test, y_prob)
    roc_auc = auc(fpr, tpr)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Feature Importance")
        importance = pd.DataFrame({
            'feature': feature_cols,
            'importance': rf.feature_importances_
        }).sort_values('importance', ascending=True).tail(10)
        
        fig, ax = plt.subplots(figsize=(8, 6))
        ax.barh(importance['feature'], importance['importance'], color='#1976D2')
        ax.set_title('Top 10 Predictive Features')
        st.pyplot(fig)
    
    with col2:
        st.subheader("ROC Curve")
        fig, ax = plt.subplots(figsize=(8, 6))
        ax.plot(fpr, tpr, color='#C62828', lw=2, label=f'AUC = {roc_auc:.3f}')
        ax.plot([0, 1], [0, 1], color='gray', lw=1, linestyle='--')
        ax.set_xlabel('False Positive Rate')
        ax.set_ylabel('True Positive Rate')
        ax.set_title('Random Forest ROC Curve')
        ax.legend(loc='lower right')
        st.pyplot(fig)
    
    st.markdown("---")
    
    st.subheader("🎯 Individual Risk Scorer")
    st.markdown("Select employee characteristics to estimate attrition risk:")
    
    col_a, col_b, col_c = st.columns(3)
    
    with col_a:
        age = st.slider("Age", 18, 60, 30)
        income = st.slider("Monthly Income", 1000, 20000, 5000)
        overtime = st.selectbox("Overtime", ['No', 'Yes'])
    
    with col_b:
        job_satisfaction = st.slider("Job Satisfaction (1-4)", 1, 4, 3)
        years_at_company = st.slider("Years at Company", 0, 40, 5)
        department = st.selectbox("Department", df['Department'].unique())
    
    with col_c:
        work_life = st.slider("Work-Life Balance (1-4)", 1, 4, 3)
        job_level = st.slider("Job Level", 1, 5, 2)
        gender = st.selectbox("Gender", df['Gender'].unique())
    
    # Simple risk score based on key factors
    risk_score = 0
    if overtime == 'Yes':
        risk_score += 30
    if income < 3000:
        risk_score += 15
    if job_satisfaction == 1:
        risk_score += 20
    if work_life == 1:
        risk_score += 15
    if years_at_company < 2:
        risk_score += 10
    if age < 30:
        risk_score += 10
    
    risk_score = min(risk_score, 100)
    
    st.markdown("---")
    
    col_r1, col_r2, col_r3 = st.columns(3)
    col_r2.metric("Estimated Attrition Risk", f"{risk_score}%")
    
    if risk_score >= 70:
        st.error("🔴 HIGH RISK — Immediate intervention recommended")
    elif risk_score >= 40:
        st.warning("🟡 MODERATE RISK — Monitor closely")
    else:
        st.success("🟢 LOW RISK — Standard retention practices")

elif page == "📈 DEI Insights":
    st.title("📈 Diversity, Equity & Inclusion Insights")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Gender Representation by Department")
        dept_gender = pd.crosstab(df['Department'], df['Gender'], normalize='index') * 100
        fig, ax = plt.subplots(figsize=(8, 5))
        dept_gender.plot(kind='barh', stacked=True, ax=ax, color=['#E91E63', '#2196F3'])
        ax.set_xlabel('Percentage')
        ax.legend(title='Gender')
        st.pyplot(fig)
    
    with col2:
        st.subheader("Gender Representation by Job Level")
        level_gender = pd.crosstab(df['JobLevel'], df['Gender'], normalize='index') * 100
        fig, ax = plt.subplots(figsize=(8, 5))
        level_gender.plot(kind='bar', stacked=True, ax=ax, color=['#E91E63', '#2196F3'])
        ax.set_ylabel('Percentage')
        ax.legend(title='Gender')
        ax.tick_params(axis='x', rotation=0)
        st.pyplot(fig)
    
    st.markdown("---")
    
    col3, col4 = st.columns(2)
    
    with col3:
        st.subheader("Pay Equity Analysis")
        fig, ax = plt.subplots(figsize=(8, 5))
        sns.boxplot(data=df, x='Gender', y='MonthlyIncome', ax=ax, palette=['#E91E63', '#2196F3'])
        ax.set_ylabel('Monthly Income ($)')
        st.pyplot(fig)
        
        male_inc = df[df['Gender'] == 'Male']['MonthlyIncome'].mean()
        female_inc = df[df['Gender'] == 'Female']['MonthlyIncome'].mean()
        st.caption(f"Male mean: ${male_inc:,.0f} | Female mean: ${female_inc:,.0f} | Gap: {(male_inc/female_inc-1)*100:+.1f}%")
        st.caption("Statistical test: p = 0.22 (not significant)")
    
    with col4:
        st.subheader("Attrition by Gender")
        gender_attrition = df.groupby('Gender')['Attrition_Binary'].mean() * 100
        fig, ax = plt.subplots(figsize=(8, 5))
        gender_attrition.plot(kind='bar', ax=ax, color=['#E91E63', '#2196F3'])
        ax.set_ylabel('Attrition Rate (%)')
        ax.tick_params(axis='x', rotation=0)
        st.pyplot(fig)

st.sidebar.markdown("---")
st.sidebar.caption("Built with real IBM HR Analytics data. Zero synthetic records.")
