import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, roc_curve, auc, roc_auc_score
import warnings
import os
warnings.filterwarnings('ignore')

# Set style
plt.style.use('seaborn-v0_8-whitegrid')
sns.set_palette("husl")

# Paths
script_dir = os.path.dirname(os.path.abspath(__file__))
base_dir = os.path.join(script_dir, '..')
data_dir = os.path.join(base_dir, 'data')
fig_dir = os.path.join(base_dir, 'figures')

os.makedirs(data_dir, exist_ok=True)
os.makedirs(fig_dir, exist_ok=True)

# Load data
data_path = os.path.join(data_dir, 'WA_Fn-UseC_-HR-Employee-Attrition.csv')
df = pd.read_csv(data_path)
print(f"Dataset shape: {df.shape}")
print(f"Attrition rate: {df['Attrition'].value_counts(normalize=True)['Yes']:.1%}")

# Encode target
df['Attrition_Binary'] = df['Attrition'].map({'Yes': 1, 'No': 0})

# ============================================================
# FIGURE 1: ATTRITION OVERVIEW
# ============================================================
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Overall attrition rate
df['Attrition'].value_counts().plot(kind='bar', ax=axes[0], color=['#2E7D32', '#C62828'])
axes[0].set_title('Overall Attrition Distribution', fontsize=14, fontweight='bold')
axes[0].set_ylabel('Count')
axes[0].tick_params(axis='x', rotation=0)
for i, v in enumerate(df['Attrition'].value_counts()):
    axes[0].text(i, v + 10, f'{v}\n({v/len(df)*100:.1f}%)', ha='center', fontweight='bold')

# Attrition by department
dept_attrition = df.groupby('Department')['Attrition_Binary'].agg(['count', 'sum', 'mean']).reset_index()
dept_attrition['rate'] = dept_attrition['mean'] * 100
dept_attrition = dept_attrition.sort_values('rate', ascending=True)

axes[1].barh(dept_attrition['Department'], dept_attrition['rate'], color='#C62828')
axes[1].set_title('Attrition Rate by Department', fontsize=14, fontweight='bold')
axes[1].set_xlabel('Attrition Rate (%)')
for i, (idx, row) in enumerate(dept_attrition.iterrows()):
    axes[1].text(row['rate'] + 0.3, i, f"{row['rate']:.1f}% ({row['sum']}/{row['count']})", va='center', fontsize=10)

plt.tight_layout()
plt.savefig(os.path.join(fig_dir, '01_attrition_overview.png'), dpi=150, bbox_inches='tight')
plt.show()

print(f"\nDepartment attrition rates:")
print(dept_attrition[['Department', 'rate']].to_string(index=False))

# ============================================================
# FIGURE 2: ATTRITION BY DEMOGRAPHICS
# ============================================================
fig, axes = plt.subplots(2, 2, figsize=(14, 12))

# Age distribution
bins = [18, 25, 30, 35, 40, 45, 50, 60]
labels = ['18-25', '26-30', '31-35', '36-40', '41-45', '46-50', '51-60']
df['AgeGroup'] = pd.cut(df['Age'], bins=bins, labels=labels, right=False)
age_attrition = df.groupby('AgeGroup')['Attrition_Binary'].mean() * 100
age_attrition.plot(kind='bar', ax=axes[0,0], color='#1565C0')
axes[0,0].set_title('Attrition Rate by Age Group', fontsize=12, fontweight='bold')
axes[0,0].set_ylabel('Attrition Rate (%)')
axes[0,0].tick_params(axis='x', rotation=45)

# Gender
gender_attrition = df.groupby('Gender')['Attrition_Binary'].mean() * 100
gender_attrition.plot(kind='bar', ax=axes[0,1], color=['#E91E63', '#2196F3'])
axes[0,1].set_title('Attrition Rate by Gender', fontsize=12, fontweight='bold')
axes[0,1].set_ylabel('Attrition Rate (%)')
axes[0,1].tick_params(axis='x', rotation=0)

# Marital Status
marital_attrition = df.groupby('MaritalStatus')['Attrition_Binary'].mean() * 100
marital_attrition.plot(kind='bar', ax=axes[1,0], color='#FF9800')
axes[1,0].set_title('Attrition Rate by Marital Status', fontsize=12, fontweight='bold')
axes[1,0].set_ylabel('Attrition Rate (%)')
axes[1,0].tick_params(axis='x', rotation=45)

# Education Field
edu_attrition = df.groupby('EducationField')['Attrition_Binary'].mean() * 100
edu_attrition.plot(kind='bar', ax=axes[1,1], color='#4CAF50')
axes[1,1].set_title('Attrition Rate by Education Field', fontsize=12, fontweight='bold')
axes[1,1].set_ylabel('Attrition Rate (%)')
axes[1,1].tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.savefig(os.path.join(fig_dir, '02_attrition_demographics.png'), dpi=150, bbox_inches='tight')
plt.show()

# ============================================================
# FIGURE 3: ATTRITION BY JOB FACTORS
# ============================================================
fig, axes = plt.subplots(2, 2, figsize=(14, 12))

# Overtime
overtime_attrition = df.groupby('OverTime')['Attrition_Binary'].mean() * 100
overtime_attrition.plot(kind='bar', ax=axes[0,0], color=['#4CAF50', '#F44336'])
axes[0,0].set_title('Attrition Rate by Overtime Status', fontsize=12, fontweight='bold')
axes[0,0].set_ylabel('Attrition Rate (%)')
axes[0,0].tick_params(axis='x', rotation=0)

# Job Role
role_attrition = df.groupby('JobRole')['Attrition_Binary'].mean() * 100
role_attrition.sort_values(ascending=True).plot(kind='barh', ax=axes[0,1], color='#9C27B0')
axes[0,1].set_title('Attrition Rate by Job Role', fontsize=12, fontweight='bold')
axes[0,1].set_xlabel('Attrition Rate (%)')

# Job Level
level_attrition = df.groupby('JobLevel')['Attrition_Binary'].mean() * 100
level_attrition.plot(kind='bar', ax=axes[1,0], color='#00BCD4')
axes[1,0].set_title('Attrition Rate by Job Level', fontsize=12, fontweight='bold')
axes[1,0].set_ylabel('Attrition Rate (%)')
axes[1,0].tick_params(axis='x', rotation=0)

# Business Travel
travel_attrition = df.groupby('BusinessTravel')['Attrition_Binary'].mean() * 100
travel_attrition.plot(kind='bar', ax=axes[1,1], color='#795548')
axes[1,1].set_title('Attrition Rate by Business Travel', fontsize=12, fontweight='bold')
axes[1,1].set_ylabel('Attrition Rate (%)')
axes[1,1].tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.savefig(os.path.join(fig_dir, '03_attrition_job_factors.png'), dpi=150, bbox_inches='tight')
plt.show()

# ============================================================
# FIGURE 4: ATTRITION BY SATISFACTION & COMPENSATION
# ============================================================
fig, axes = plt.subplots(2, 2, figsize=(14, 12))

# Job Satisfaction
js_attrition = df.groupby('JobSatisfaction')['Attrition_Binary'].mean() * 100
js_attrition.plot(kind='bar', ax=axes[0,0], color='#E91E63')
axes[0,0].set_title('Attrition Rate by Job Satisfaction (1=Low, 4=High)', fontsize=12, fontweight='bold')
axes[0,0].set_ylabel('Attrition Rate (%)')
axes[0,0].tick_params(axis='x', rotation=0)

# Environment Satisfaction
env_attrition = df.groupby('EnvironmentSatisfaction')['Attrition_Binary'].mean() * 100
env_attrition.plot(kind='bar', ax=axes[0,1], color='#009688')
axes[0,1].set_title('Attrition Rate by Environment Satisfaction', fontsize=12, fontweight='bold')
axes[0,1].set_ylabel('Attrition Rate (%)')
axes[0,1].tick_params(axis='x', rotation=0)

# Work-Life Balance
wlb_attrition = df.groupby('WorkLifeBalance')['Attrition_Binary'].mean() * 100
wlb_attrition.plot(kind='bar', ax=axes[1,0], color='#FF5722')
axes[1,0].set_title('Attrition Rate by Work-Life Balance', fontsize=12, fontweight='bold')
axes[1,0].set_ylabel('Attrition Rate (%)')
axes[1,0].tick_params(axis='x', rotation=0)

# Monthly Income
income_bins = [0, 3000, 5000, 7500, 10000, 15000, 20000]
income_labels = ['<3K', '3-5K', '5-7.5K', '7.5-10K', '10-15K', '15K+']
df['IncomeGroup'] = pd.cut(df['MonthlyIncome'], bins=income_bins, labels=income_labels)
income_attrition = df.groupby('IncomeGroup')['Attrition_Binary'].mean() * 100
income_attrition.plot(kind='bar', ax=axes[1,1], color='#607D8B')
axes[1,1].set_title('Attrition Rate by Monthly Income', fontsize=12, fontweight='bold')
axes[1,1].set_ylabel('Attrition Rate (%)')
axes[1,1].tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.savefig(os.path.join(fig_dir, '04_attrition_satisfaction_compensation.png'), dpi=150, bbox_inches='tight')
plt.show()

# ============================================================
# FIGURE 5: CORRELATION HEATMAP
# ============================================================
numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
numeric_cols.remove('EmployeeCount')
numeric_cols.remove('EmployeeNumber')
numeric_cols.remove('StandardHours')
numeric_cols.remove('Attrition_Binary')

plt.figure(figsize=(16, 12))
corr_matrix = df[numeric_cols + ['Attrition_Binary']].corr()
mask = np.triu(np.ones_like(corr_matrix, dtype=bool))
sns.heatmap(corr_matrix, mask=mask, annot=True, fmt='.2f', cmap='RdBu_r', center=0,
            square=True, linewidths=0.5, cbar_kws={"shrink": 0.8})
plt.title('Correlation Heatmap: Numeric Features vs Attrition', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig(os.path.join(fig_dir, '05_correlation_heatmap.png'), dpi=150, bbox_inches='tight')
plt.show()

# ============================================================
# FIGURE 6: FEATURE IMPORTANCE (RANDOM FOREST)
# ============================================================
# Prepare features
features_to_encode = ['BusinessTravel', 'Department', 'EducationField', 'Gender', 'JobRole', 'MaritalStatus', 'OverTime']
df_encoded = df.copy()
le = LabelEncoder()
for col in features_to_encode:
    df_encoded[col] = le.fit_transform(df_encoded[col])

feature_cols = [col for col in df_encoded.columns if col not in ['Attrition', 'Attrition_Binary', 'AgeGroup', 'IncomeGroup', 'EmployeeCount', 'EmployeeNumber', 'Over18', 'StandardHours']]
X = df_encoded[feature_cols]
y = df_encoded['Attrition_Binary']

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Random Forest
rf = RandomForestClassifier(n_estimators=100, random_state=42, class_weight='balanced')
rf.fit(X_train, y_train)

# Feature importance
importance = pd.DataFrame({
    'feature': feature_cols,
    'importance': rf.feature_importances_
}).sort_values('importance', ascending=True)

plt.figure(figsize=(10, 8))
plt.barh(importance['feature'], importance['importance'], color='#1976D2')
plt.title('Feature Importance: Random Forest', fontsize=14, fontweight='bold')
plt.xlabel('Importance')
plt.tight_layout()
plt.savefig(os.path.join(fig_dir, '06_feature_importance_rf.png'), dpi=150, bbox_inches='tight')
plt.show()

# ============================================================
# FIGURE 7: MODEL PERFORMANCE
# ============================================================
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Confusion Matrix
y_pred = rf.predict(X_test)
cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=axes[0],
            xticklabels=['Stay', 'Leave'], yticklabels=['Stay', 'Leave'])
axes[0].set_title('Confusion Matrix: Random Forest', fontsize=12, fontweight='bold')
axes[0].set_ylabel('Actual')
axes[0].set_xlabel('Predicted')

# ROC Curve
y_prob = rf.predict_proba(X_test)[:, 1]
fpr, tpr, _ = roc_curve(y_test, y_prob)
roc_auc = auc(fpr, tpr)

axes[1].plot(fpr, tpr, color='#C62828', lw=2, label=f'ROC curve (AUC = {roc_auc:.3f})')
axes[1].plot([0, 1], [0, 1], color='gray', lw=1, linestyle='--')
axes[1].set_xlim([0.0, 1.0])
axes[1].set_ylim([0.0, 1.05])
axes[1].set_xlabel('False Positive Rate')
axes[1].set_ylabel('True Positive Rate')
axes[1].set_title('ROC Curve: Random Forest', fontsize=12, fontweight='bold')
axes[1].legend(loc='lower right')

plt.tight_layout()
plt.savefig(os.path.join(fig_dir, '07_model_performance.png'), dpi=150, bbox_inches='tight')
plt.show()

# Print model metrics
print(f"\nRandom Forest Performance:")
print(f"  AUC: {roc_auc:.3f}")
print(f"  Accuracy: {rf.score(X_test, y_test):.3f}")
print(classification_report(y_test, y_pred, target_names=['Stay', 'Leave']))

# ============================================================
# FIGURE 8: ATTRITION BY TENURE & CAREER PROGRESSION
# ============================================================
fig, axes = plt.subplots(2, 2, figsize=(14, 12))

# Years at Company
years_bins = [0, 2, 5, 10, 15, 40]
years_labels = ['0-2', '2-5', '5-10', '10-15', '15+']
df['YearsGroup'] = pd.cut(df['YearsAtCompany'], bins=years_bins, labels=years_labels, right=False)
years_attrition = df.groupby('YearsGroup')['Attrition_Binary'].mean() * 100
years_attrition.plot(kind='bar', ax=axes[0,0], color='#673AB7')
axes[0,0].set_title('Attrition Rate by Years at Company', fontsize=12, fontweight='bold')
axes[0,0].set_ylabel('Attrition Rate (%)')
axes[0,0].tick_params(axis='x', rotation=45)

# Years in Current Role
role_years_attrition = df.groupby('YearsInCurrentRole')['Attrition_Binary'].mean() * 100
role_years_attrition.plot(kind='bar', ax=axes[0,1], color='#3F51B5')
axes[0,1].set_title('Attrition Rate by Years in Current Role', fontsize=12, fontweight='bold')
axes[0,1].set_ylabel('Attrition Rate (%)')
axes[0,1].tick_params(axis='x', rotation=45)

# Years Since Last Promotion
promo_attrition = df.groupby('YearsSinceLastPromotion')['Attrition_Binary'].mean() * 100
promo_attrition.plot(kind='bar', ax=axes[1,0], color='#E91E63')
axes[1,0].set_title('Attrition Rate by Years Since Promotion', fontsize=12, fontweight='bold')
axes[1,0].set_ylabel('Attrition Rate (%)')
axes[1,0].tick_params(axis='x', rotation=45)

# Number of Companies Worked
companies_attrition = df.groupby('NumCompaniesWorked')['Attrition_Binary'].mean() * 100
companies_attrition.plot(kind='bar', ax=axes[1,1], color='#009688')
axes[1,1].set_title('Attrition Rate by Number of Companies Worked', fontsize=12, fontweight='bold')
axes[1,1].set_ylabel('Attrition Rate (%)')
axes[1,1].tick_params(axis='x', rotation=0)

plt.tight_layout()
plt.savefig(os.path.join(fig_dir, '08_attrition_tenure_career.png'), dpi=150, bbox_inches='tight')
plt.show()

# ============================================================
# FIGURE 9: KEY INSIGHTS SUMMARY
# ============================================================
fig, ax = plt.subplots(figsize=(12, 8))
ax.axis('off')

insights = [
    "KEY INSIGHTS: WORKFORCE ATTRITION ANALYSIS",
    "",
    f"1. OVERALL ATTRITION: {df['Attrition_Binary'].mean()*100:.1f}% (237 of 1,470 employees)",
    f"2. HIGHEST RISK DEPARTMENT: {dept_attrition.iloc[-1]['Department']} ({dept_attrition.iloc[-1]['rate']:.1f}%)",
    f"3. OVERTIME IMPACT: {overtime_attrition['Yes']:.1f}% attrition with overtime vs {overtime_attrition['No']:.1f}% without",
    f"4. INCOME CORRELATION: Lower income groups show {income_attrition.iloc[0]:.1f}% attrition vs {income_attrition.iloc[-1]:.1f}% for highest",
    f"5. SATISFACTION DRIVERS: Job satisfaction 1 = {js_attrition.iloc[0]:.1f}% attrition vs satisfaction 4 = {js_attrition.iloc[-1]:.1f}%",
    f"6. TOP PREDICTIVE FEATURES: {', '.join(importance.tail(5)['feature'].tolist()[::-1])}",
    f"7. MODEL PERFORMANCE: AUC = {roc_auc:.3f}, enabling risk scoring for 1,470 employees",
    "",
    "Data Source: IBM HR Analytics Employee Attrition & Performance (Kaggle)",
    "1,470 employees · 35 features · Zero synthetic records"
]

for i, line in enumerate(insights):
    weight = 'bold' if line.startswith(('KEY', 'Data')) else 'normal'
    size = 14 if line.startswith('KEY') else 12 if line.startswith('Data') else 11
    color = '#1565C0' if line.startswith('KEY') else '#555' if line.startswith('Data') else '#333'
    ax.text(0.05, 0.95 - i*0.08, line, fontsize=size, fontweight=weight, color=color, transform=ax.transAxes)

plt.tight_layout()
plt.savefig(os.path.join(fig_dir, '09_key_insights_summary.png'), dpi=150, bbox_inches='tight')
plt.show()

print("\n" + "="*60)
print("FIGURE GENERATION COMPLETE")
print("="*60)
print(f"Figures saved to {fig_dir}:")
for f in sorted(os.listdir(fig_dir)):
    if f.endswith('.png'):
        print(f"  - {f}")
