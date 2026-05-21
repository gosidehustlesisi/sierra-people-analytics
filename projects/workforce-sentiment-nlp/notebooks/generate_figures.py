import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
import re
import warnings
import os
warnings.filterwarnings('ignore')

plt.style.use('seaborn-v0_8-whitegrid')

# Paths
script_dir = os.path.dirname(os.path.abspath(__file__))
base_dir = os.path.join(script_dir, '..')
data_dir = os.path.join(base_dir, 'data')
fig_dir = os.path.join(base_dir, 'figures')

os.makedirs(data_dir, exist_ok=True)
os.makedirs(fig_dir, exist_ok=True)

# Load Glassdoor reviews
df = pd.read_csv(os.path.join(data_dir, 'glassdoor-companies-reviews.csv'))
print(f"Dataset: {df.shape[0]} reviews, {df.shape[1]} columns")

# Clean and prepare
# Drop rows with missing critical fields
df = df.dropna(subset=['review_pros', 'review_cons', 'rating_overall'])
df['review_pros'] = df['review_pros'].astype(str)
df['review_cons'] = df['review_cons'].astype(str)

# ============================================================
# FIGURE 1: RATING DISTRIBUTION OVERVIEW
# ============================================================
fig, axes = plt.subplots(2, 2, figsize=(14, 12))

# Overall rating distribution
df['rating_overall'].value_counts().sort_index().plot(kind='bar', ax=axes[0,0], color='#1976D2')
axes[0,0].set_title('Overall Rating Distribution', fontsize=12, fontweight='bold')
axes[0,0].set_xlabel('Rating')
axes[0,0].set_ylabel('Count')
axes[0,0].tick_params(axis='x', rotation=0)

# Work-life balance rating
df['rating_work_life'].value_counts().sort_index().plot(kind='bar', ax=axes[0,1], color='#009688')
axes[0,1].set_title('Work-Life Balance Rating', fontsize=12, fontweight='bold')
axes[0,1].set_xlabel('Rating')
axes[0,1].set_ylabel('Count')
axes[0,1].tick_params(axis='x', rotation=0)

# Culture & values rating
df['rating_culture_values'].value_counts().sort_index().plot(kind='bar', ax=axes[1,0], color='#E91E63')
axes[1,0].set_title('Culture & Values Rating', fontsize=12, fontweight='bold')
axes[1,0].set_xlabel('Rating')
axes[1,0].set_ylabel('Count')
axes[1,0].tick_params(axis='x', rotation=0)

# Compensation benefits rating
df['rating_compensation_benefits'].value_counts().sort_index().plot(kind='bar', ax=axes[1,1], color='#FF9800')
axes[1,1].set_title('Compensation & Benefits Rating', fontsize=12, fontweight='bold')
axes[1,1].set_xlabel('Rating')
axes[1,1].set_ylabel('Count')
axes[1,1].tick_params(axis='x', rotation=0)

plt.tight_layout()
plt.savefig(os.path.join(fig_dir, '01_rating_distribution_overview.png'), dpi=150, bbox_inches='tight')
plt.show()

# ============================================================
# FIGURE 2: RATING COMPARISON BY DIMENSION
# ============================================================
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# Average ratings by dimension
rating_cols = ['rating_overall', 'rating_work_life', 'rating_culture_values', 
               'rating_compensation_benefits', 'rating_senior_leadership', 'rating_career_opportunities']
avg_ratings = df[rating_cols].mean().sort_values(ascending=True)
colors = ['#F44336', '#FF9800', '#FFEB3B', '#4CAF50', '#2196F3', '#9C27B0']
avg_ratings.plot(kind='barh', ax=axes[0], color=colors)
axes[0].set_title('Average Ratings by Dimension', fontsize=12, fontweight='bold')
axes[0].set_xlabel('Average Rating (1-5)')
for i, v in enumerate(avg_ratings):
    axes[0].text(v + 0.05, i, f'{v:.2f}', va='center', fontsize=10)

# Rating heatmap by company (top 10 companies by review count)
top_companies = df['company_name'].value_counts().head(10).index
company_ratings = df[df['company_name'].isin(top_companies)].groupby('company_name')[rating_cols].mean()
company_ratings = company_ratings.reindex(company_ratings.mean(axis=1).sort_values(ascending=False).index)

sns.heatmap(company_ratings, annot=True, fmt='.1f', cmap='RdYlGn', vmin=1, vmax=5, ax=axes[1])
axes[1].set_title('Rating Heatmap: Top 10 Companies', fontsize=12, fontweight='bold')
axes[1].set_xlabel('Rating Dimension')
axes[1].set_ylabel('Company')

plt.tight_layout()
plt.savefig(os.path.join(fig_dir, '02_rating_comparison_dimensions.png'), dpi=150, bbox_inches='tight')
plt.show()

print(f"\nAverage Ratings by Dimension:")
for dim, val in avg_ratings.items():
    print(f"  {dim}: {val:.2f}")

# ============================================================
# FIGURE 3: SENTIMENT ANALYSIS (PROS vs CONS)
# ============================================================
# Simple lexicon-based sentiment
positive_words = ['good', 'great', 'excellent', 'amazing', 'fantastic', 'wonderful', 'best', 'love', 'happy', 
                  'positive', 'awesome', 'outstanding', 'superb', 'perfect', 'benefits', 'growth', 'opportunity',
                  'flexible', 'balance', 'supportive', 'friendly', 'professional', 'career', 'learning']
negative_words = ['bad', 'terrible', 'awful', 'worst', 'hate', 'poor', 'negative', 'difficult', 'stressful',
                  'toxic', 'disappointing', 'frustrating', 'bureaucracy', 'micromanagement', 'unfair', 'low',
                  'overworked', 'burnout', 'layoff', 'fired', 'disorganized', 'chaos']

def count_sentiment_words(text, word_list):
    text = text.lower()
    count = 0
    for word in word_list:
        count += text.count(word)
    return count

df['pros_positive'] = df['review_pros'].apply(lambda x: count_sentiment_words(x, positive_words))
df['cons_negative'] = df['review_cons'].apply(lambda x: count_sentiment_words(x, negative_words))
df['pros_length'] = df['review_pros'].apply(len)
df['cons_length'] = df['review_cons'].apply(len)

fig, axes = plt.subplots(2, 2, figsize=(14, 12))

# Positive words in pros by rating
rating_positive = df.groupby('rating_overall')['pros_positive'].mean()
rating_positive.plot(kind='bar', ax=axes[0,0], color='#4CAF50')
axes[0,0].set_title('Avg Positive Words in Pros by Overall Rating', fontsize=12, fontweight='bold')
axes[0,0].set_xlabel('Overall Rating')
axes[0,0].set_ylabel('Avg Positive Word Count')
axes[0,0].tick_params(axis='x', rotation=0)

# Negative words in cons by rating
rating_negative = df.groupby('rating_overall')['cons_negative'].mean()
rating_negative.plot(kind='bar', ax=axes[0,1], color='#F44336')
axes[0,1].set_title('Avg Negative Words in Cons by Overall Rating', fontsize=12, fontweight='bold')
axes[0,1].set_xlabel('Overall Rating')
axes[0,1].set_ylabel('Avg Negative Word Count')
axes[0,1].tick_params(axis='x', rotation=0)

# Pros vs Cons length by rating
length_by_rating = df.groupby('rating_overall')[['pros_length', 'cons_length']].mean()
length_by_rating.plot(kind='bar', ax=axes[1,0], color=['#4CAF50', '#F44336'])
axes[1,0].set_title('Review Length (chars) by Rating', fontsize=12, fontweight='bold')
axes[1,0].set_xlabel('Overall Rating')
axes[1,0].set_ylabel('Average Characters')
axes[1,0].tick_params(axis='x', rotation=0)
axes[1,0].legend(['Pros Length', 'Cons Length'])

# Sentiment score distribution
# Net sentiment = positive words in pros - negative words in cons
df['net_sentiment'] = df['pros_positive'] - df['cons_negative']
df['net_sentiment'].hist(bins=20, ax=axes[1,1], color='#9C27B0', alpha=0.7)
axes[1,1].set_title('Net Sentiment Score Distribution', fontsize=12, fontweight='bold')
axes[1,1].set_xlabel('Net Sentiment (Pros Pos - Cons Neg)')
axes[1,1].set_ylabel('Frequency')
axes[1,1].axvline(df['net_sentiment'].mean(), color='red', linestyle='--', linewidth=2, label=f'Mean: {df["net_sentiment"].mean():.1f}')
axes[1,1].legend()

plt.tight_layout()
plt.savefig(os.path.join(fig_dir, '03_sentiment_analysis_pros_cons.png'), dpi=150, bbox_inches='tight')
plt.show()

# ============================================================
# FIGURE 4: TOP THEMES IN PROS & CONS
# ============================================================
def extract_common_words(texts, top_n=15):
    all_text = ' '.join(texts).lower()
    # Remove punctuation and split
    words = re.findall(r'\b[a-z]{3,}\b', all_text)
    # Filter common stop words
    stop_words = {'the', 'and', 'for', 'are', 'but', 'not', 'you', 'all', 'can', 'had', 'her', 'was', 'one', 'our', 'out', 'day', 'get', 'has', 'him', 'his', 'how', 'its', 'may', 'new', 'now', 'old', 'see', 'two', 'way', 'who', 'boy', 'did', 'she', 'use', 'her', 'man', 'men', 'too', 'work', 'company'}
    words = [w for w in words if w not in stop_words and len(w) > 3]
    return Counter(words).most_common(top_n)

pros_words = extract_common_words(df['review_pros'].tolist(), 15)
cons_words = extract_common_words(df['review_cons'].tolist(), 15)

fig, axes = plt.subplots(1, 2, figsize=(14, 8))

# Top words in pros
if pros_words:
    words, counts = zip(*pros_words)
    axes[0].barh(range(len(words)), counts, color='#4CAF50')
    axes[0].set_yticks(range(len(words)))
    axes[0].set_yticklabels(words)
    axes[0].set_title('Top 15 Words in PROS Reviews', fontsize=12, fontweight='bold')
    axes[0].set_xlabel('Frequency')
    axes[0].invert_yaxis()

# Top words in cons
if cons_words:
    words, counts = zip(*cons_words)
    axes[1].barh(range(len(words)), counts, color='#F44336')
    axes[1].set_yticks(range(len(words)))
    axes[1].set_yticklabels(words)
    axes[1].set_title('Top 15 Words in CONS Reviews', fontsize=12, fontweight='bold')
    axes[1].set_xlabel('Frequency')
    axes[1].invert_yaxis()

plt.tight_layout()
plt.savefig(os.path.join(fig_dir, '04_top_themes_pros_cons.png'), dpi=150, bbox_inches='tight')
plt.show()

print(f"\nTop words in PROS: {', '.join([w for w, c in pros_words[:10]])}")
print(f"Top words in CONS: {', '.join([w for w, c in cons_words[:10]])}")

# ============================================================
# FIGURE 5: EMPLOYEE STATUS & TENURE ANALYSIS
# ============================================================
fig, axes = plt.subplots(2, 2, figsize=(14, 12))

# Employee status distribution
status_counts = df['employee_status'].value_counts()
status_counts.plot(kind='pie', ax=axes[0,0], autopct='%1.1f%%', startangle=90)
axes[0,0].set_title('Employee Status Distribution', fontsize=12, fontweight='bold')
axes[0,0].set_ylabel('')

# Employee type (current vs former)
type_counts = df['employee_type'].value_counts()
type_counts.plot(kind='pie', ax=axes[0,1], autopct='%1.1f%%', startangle=90)
axes[0,1].set_title('Employment Type', fontsize=12, fontweight='bold')
axes[0,1].set_ylabel('')

# Employee length (tenure)
df['employee_length'].hist(bins=20, ax=axes[1,0], color='#2196F3', alpha=0.7)
axes[1,0].set_title('Employee Tenure Distribution (Years)', fontsize=12, fontweight='bold')
axes[1,0].set_xlabel('Years at Company')
axes[1,0].set_ylabel('Count')

# Rating by tenure
# Create tenure bins
df['tenure_bin'] = pd.cut(df['employee_length'], bins=[0, 1, 3, 5, 10, 50], labels=['<1yr', '1-3yr', '3-5yr', '5-10yr', '10yr+'])
tenure_rating = df.groupby('tenure_bin')['rating_overall'].mean()
tenure_rating.plot(kind='bar', ax=axes[1,1], color='#FF9800')
axes[1,1].set_title('Average Rating by Tenure', fontsize=12, fontweight='bold')
axes[1,1].set_xlabel('Tenure')
axes[1,1].set_ylabel('Average Overall Rating')
axes[1,1].tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.savefig(os.path.join(fig_dir, '05_employee_status_tenure.png'), dpi=150, bbox_inches='tight')
plt.show()

# ============================================================
# FIGURE 6: RECOMMENDATION & APPROVAL FLAGS
# ============================================================
fig, axes = plt.subplots(2, 2, figsize=(14, 12))

# CEO Approval
ceo_counts = df['flags_ceo_approval'].value_counts()
ceo_counts.plot(kind='bar', ax=axes[0,0], color=['#F44336', '#4CAF50', '#FF9800'])
axes[0,0].set_title('CEO Approval Distribution', fontsize=12, fontweight='bold')
axes[0,0].set_ylabel('Count')
axes[0,0].tick_params(axis='x', rotation=45)

# Recommend to Friend
rec_counts = df['flags_recommend_frend'].value_counts()
rec_counts.plot(kind='bar', ax=axes[0,1], color=['#F44336', '#4CAF50', '#FF9800'])
axes[0,1].set_title('Recommend to Friend Distribution', fontsize=12, fontweight='bold')
axes[0,1].set_ylabel('Count')
axes[0,1].tick_params(axis='x', rotation=45)

# Business Outlook
outlook_counts = df['flags_business_outlook'].value_counts()
outlook_counts.plot(kind='bar', ax=axes[1,0], color=['#F44336', '#4CAF50', '#FF9800'])
axes[1,0].set_title('Business Outlook Distribution', fontsize=12, fontweight='bold')
axes[1,0].set_ylabel('Count')
axes[1,0].tick_params(axis='x', rotation=45)

# Approval by rating
approval_by_rating = df.groupby('rating_overall')[['flags_ceo_approval', 'flags_recommend_frend', 'flags_business_outlook']].apply(
    lambda x: (x == 'POSITIVE').mean() * 100
)
approval_by_rating.plot(kind='bar', ax=axes[1,1], color=['#E91E63', '#2196F3', '#FF9800'])
axes[1,1].set_title('% Positive Flags by Overall Rating', fontsize=12, fontweight='bold')
axes[1,1].set_xlabel('Overall Rating')
axes[1,1].set_ylabel('% Positive')
axes[1,1].tick_params(axis='x', rotation=0)
axes[1,1].legend(['CEO Approval', 'Recommend', 'Business Outlook'])

plt.tight_layout()
plt.savefig(os.path.join(fig_dir, '06_recommendation_approval_flags.png'), dpi=150, bbox_inches='tight')
plt.show()

# ============================================================
# FIGURE 7: KEY INSIGHTS SUMMARY
# ============================================================
fig, ax = plt.subplots(figsize=(12, 8))
ax.axis('off')

# Calculate summary stats
avg_overall = df['rating_overall'].mean()
recommend_pct = (df['flags_recommend_frend'] == 'POSITIVE').mean() * 100
ceo_approve_pct = (df['flags_ceo_approval'] == 'POSITIVE').mean() * 100
outlook_pct = (df['flags_business_outlook'] == 'POSITIVE').mean() * 100
former_pct = df['employee_type'].str.contains('Former', na=False).mean() * 100
current_pct = df['employee_type'].str.contains('Current', na=False).mean() * 100

insights = [
    "WORKFORCE SENTIMENT NLP: KEY INSIGHTS",
    "",
    f"Dataset: {len(df)} real Glassdoor reviews from {df['company_name'].nunique()} companies",
    "",
    f"1. OVERALL SENTIMENT: Average rating {avg_overall:.2f}/5.0",
    f"2. RECOMMENDATION RATE: {recommend_pct:.1f}% would recommend to a friend",
    f"3. CEO APPROVAL: {ceo_approve_pct:.1f}% approve of CEO performance",
    f"4. BUSINESS OUTLOOK: {outlook_pct:.1f}% have positive business outlook",
    f"5. REVIEWER COMPOSITION: {current_pct:.1f}% current employees, {former_pct:.1f}% former",
    f"",
    f"6. TOP PROS THEMES: {', '.join([w for w, c in pros_words[:5]])}",
    f"7. TOP CONS THEMES: {', '.join([w for w, c in cons_words[:5]])}",
    f"8. SENTIMENT-RATING CORRELATION: Higher ratings correlate with more positive",
    f"   words in PROS and fewer negative words in CONS (r = {df['rating_overall'].corr(df['net_sentiment']):.2f})",
    f"",
    f"9. RATING BY DIMENSION (avg):",
    f"   • Overall: {avg_ratings['rating_overall']:.2f}",
    f"   • Work-Life: {avg_ratings['rating_work_life']:.2f}",
    f"   • Culture: {avg_ratings['rating_culture_values']:.2f}",
    f"   • Compensation: {avg_ratings['rating_compensation_benefits']:.2f}",
    f"   • Leadership: {avg_ratings['rating_senior_leadership']:.2f}",
    f"   • Career Ops: {avg_ratings['rating_career_opportunities']:.2f}",
    "",
    "Data Source: Glassdoor Company Reviews (Bright Data sample, 1,000 records)",
    "Analysis: Lexicon-based sentiment, frequency analysis, thematic extraction"
]

for i, line in enumerate(insights):
    weight = 'bold' if line.startswith(('WORKFORCE', 'Data', 'Analysis')) else 'normal'
    size = 14 if line.startswith('WORKFORCE') else 11 if line.startswith(('Data', 'Analysis')) else 11
    color = '#1565C0' if line.startswith('WORKFORCE') else '#555' if line.startswith(('Data', 'Analysis')) else '#333'
    ax.text(0.05, 0.95 - i*0.042, line, fontsize=size, fontweight=weight, color=color, transform=ax.transAxes)

plt.tight_layout()
plt.savefig(os.path.join(fig_dir, '07_key_insights_summary.png'), dpi=150, bbox_inches='tight')
plt.show()

print("\n" + "="*60)
print("NLP SENTIMENT FIGURE GENERATION COMPLETE")
print("="*60)
for f in sorted(os.listdir(fig_dir)):
    if f.endswith('.png'):
        print(f"  - {f}")
