import streamlit as st

st.set_page_config(page_title="Workforce Sentiment NLP", layout="wide")

st.title("💬 Workforce Sentiment NLP Analysis")
st.caption("People Analytics | Natural Language Processing on Employee Feedback")

st.info("📊 Data download script in progress. Showing demo layout with expected sentiment distribution and word cloud placeholders.")

st.warning("This dashboard will display NLP-processed employee sentiment data once the download pipeline is complete. Below is the planned structure.")

st.divider()

st.subheader("Expected KPIs")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Sentiment Score", "+0.42", delta="+0.08")
col2.metric("Positive %", "62%", delta="+7%")
col3.metric("Negative Themes", "8", delta="-3")
col4.metric("Engagement Index", "74/100", delta="+6 pts")

st.divider()

st.subheader("Expected Visualizations")

chart_col1, chart_col2 = st.columns(2)
with chart_col1:
    st.markdown("**Chart: Sentiment Distribution**")
    st.empty()
    st.caption("Planned: Histogram of sentiment scores across all employee comments")
    
    st.markdown("**Chart: Sentiment by Department**")
    st.empty()
    st.caption("Planned: Grouped bar chart of positive/negative/neutral by team")

with chart_col2:
    st.markdown("**Word Cloud: Positive Themes**")
    st.empty()
    st.caption("Planned: Word cloud from top positive sentiment phrases")
    
    st.markdown("**Word Cloud: Negative Themes**")
    st.empty()
    st.caption("Planned: Word cloud from top negative sentiment phrases")

st.divider()

st.subheader("Expected Topic Breakdown")
topic_col1, topic_col2, topic_col3 = st.columns(3)
with topic_col1:
    st.markdown("**Top Positive Topics**")
    st.markdown("1. Work-life balance")
    st.markdown("2. Team collaboration")
    st.markdown("3. Career growth")
    st.markdown("4. Management support")
    st.markdown("5. Remote flexibility")

with topic_col2:
    st.markdown("**Top Negative Topics**")
    st.markdown("1. Compensation fairness")
    st.markdown("2. Meeting overload")
    st.markdown("3. Tool/tech limitations")
    st.markdown("4. Promotion transparency")
    st.markdown("5. Cross-team communication")

with topic_col3:
    st.markdown("**Emerging Themes**")
    st.markdown("1. AI/automation concerns")
    st.markdown("2. Burnout indicators")
    st.markdown("3. Return-to-office tension")
    st.markdown("4. DEI program feedback")
    st.markdown("5. Mental health support")

st.divider()

with st.expander("📁 Project Structure (Planned)"):
    st.code("""
projects/workforce-sentiment-nlp/
├── data/
│   └── employee_feedback.csv           # Downloaded from HRIS / survey platform
├── notebooks/
│   └── sentiment_nlp.ipynb             # Text preprocessing + model training
├── figures/
│   ├── sentiment_distribution.png
│   ├── sentiment_by_department.png
│   ├── positive_wordcloud.png
│   ├── negative_wordcloud.png
│   └── topic_breakdown.png
├── dashboard.py                        # This file
└── model/
    └── sentiment_classifier.pkl        # Trained transformers/sklearn model
""")

st.sidebar.caption("Built by Sierra Napier | gosidehustlesisi")
