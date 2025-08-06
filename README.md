# LIVE‑User‑Engagement: Engagement Forecasting & Hybrid Recommender System 🚀

A full-stack video analytics and recommendation pipeline built around TikTok‑style live and short‑form video engagement. It includes forecasting like‑counts, personalized recommendations, and interactive visualization of results.

---

## Project Overview

- **Predict LIVE-style Engagement**: Trained deep learning regression models (TensorFlow/Keras) to forecast `likeCount` using engineered features—achieving ~90% reduction in MAE vs. baseline.
- **Hybrid Recommender Engine**: Combined collaborative filtering (SVD via Surprise) and content-based filtering (TF-IDF + cosine similarity), with cold-start support using metadata like descriptions and categories.
- **Feature Engineering & Data Pipelines**: Created features from metadata (e.g., duration bins, verified creator flags, engagement per user) and transformed raw logs into user-item matrices and embeddings.
- **Metric & Causal Analysis Simulation**: Designed metrics for product health, implemented MAE benchmarking, and simulated A/B testing and causal inference to assess model impact.
- **Visualization Dashboard**: Built a Streamlit interface for stakeholders to explore predictions, recommendation results, feature importance, and business insights.

---

## Tech Stack & Skills

- **Python, pandas** – data ingestion, cleaning, transformation, deduplication  
- **scikit-learn** – TF-IDF encoding, cosine similarity  
- **Surprise (SVD)** – collaborative filtering  
- **TensorFlow / Keras** – regression modeling and evaluation  
- **Streamlit, Matplotlib, Seaborn** – dashboard visualization and interactive charts  
- **Statistical evaluation** – MAE benchmarking against baseline models  
- **Hybrid recommendation strategies** – combining collaborative and content-based signals, handling cold start

---

## Installation & Setup

```bash
# Clone and navigate
git clone https://github.com/hungyunxuan/LIVE-User-Engagement.git
cd LIVE-User-Engagement

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # (Linux/macOS) or use `venv\Scripts\activate` on Windows

# Install dependencies
pip install -r requirements.txt

```
## Streamlit Dashboard

Visualise results with the interactive dashboard:
```bash
streamlit run live_dashboard.py
```
## Directory Structure
.
├── data/
│   └── final_df_model.csv       # Processed dataset with features & predictions
├── run_recommendation_pipeline.py
├── live_dashboard.py
├── README.md
└── requirements.txt

## Impact and Business Alignment 
1. Enhances user experience by recommending videos tailored to user behavior and content metadata, even in cold‑start situations.
2. Supports creator ecosystem by enabling discovery of similar content to boost visibility and engagement.
3. Enables algorithmic improvement by exposing forecast accuracy and recommendations through metrics and dashboards for iterative evaluation.
