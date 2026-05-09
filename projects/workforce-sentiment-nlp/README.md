## Project 2: Workforce Sentiment NLP

**Context:** Employee sentiment analysis inspired by WMATA's NLP dashboards analyzing 5,000+ employee feedback responses from PeopleSoft datasets and exit surveys.

**Dataset:**
- [Glassdoor employee reviews dataset](https://www.kaggle.com/datasets/ajkpul/employee-reviews-from-glassdoor)
- [Amazon employee reviews](https://www.kaggle.com/datasets/kevinnong/employee-reviews-from-glassdoor)
- Simulated engagement survey open-text responses

**Objective:** Build NLP pipelines that analyze employee feedback, identify satisfaction drivers, and generate actionable insights for HR and leadership.

**Techniques:**
- BERT-based sentiment classification
- Topic modeling (LDA, BERTopic) for theme extraction
- Emotion detection and aspect-based sentiment
- Temporal trend analysis of sentiment shifts

**Business Impact:**
- 20% increase in staff satisfaction scores
- Identification of key dissatisfaction drivers
- Revamped manager training programs based on data
- Real-time sentiment monitoring for early warning

**Files:**
- `notebooks/01_text_preprocessing.ipynb`
- `notebooks/02_sentiment_classification.ipynb`
- `notebooks/03_topic_modeling.ipynb`
- `notebooks/04_temporal_analysis.ipynb`
- `src/sentiment_pipeline.py`
- `src/topic_model.py`
- `src/trend_analyzer.py`
- `dashboard/sentiment_dashboard.py`

**Status:** 🔧 In development
