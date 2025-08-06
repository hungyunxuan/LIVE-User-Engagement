import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# === Load Data ===
DATA_PATH = os.path.join("..", "data", "final_df_model.csv")
df = pd.read_csv("../data/final_df_model.csv")

st.title("📊 TikTok LIVE Video Engagement Dashboard")

# === Overview Metrics ===
st.header("📌 Summary Statistics")
st.write(df.describe())

# === Distribution Plots ===
st.header("📈 Engagement Metrics Distribution")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Like Count Distribution")
    fig, ax = plt.subplots()
    sns.histplot(df["liveRoomInfo.likeCount"], bins=20, ax=ax)
    st.pyplot(fig)

with col2:
    st.subheader("Likes Per User Distribution")
    fig, ax = plt.subplots()
    sns.histplot(df["likes_per_user"], bins=20, ax=ax)
    st.pyplot(fig)

# === Time-based Analysis ===
if "create_hour" in df.columns and "time_of_day" in df.columns:
    st.header("⏰ Time of Day Analysis")
    fig, ax = plt.subplots()
    sns.boxplot(data=df, x="time_of_day", y="liveRoomInfo.likeCount", ax=ax)
    ax.set_title("Like Count by Time of Day")
    st.pyplot(fig)

# === Category Type Analysis ===
if "category_type" in df.columns:
    st.header("📚 Category Type Engagement")
    fig, ax = plt.subplots()
    sns.boxplot(data=df, x="category_type", y="liveRoomInfo.likeCount", ax=ax)
    ax.set_title("Like Count by Category Type")
    st.pyplot(fig)

# === Prediction Result (Optional) ===
if "prediction" in df.columns:
    st.header("🤖 Model Predictions vs Actual")
    fig, ax = plt.subplots()
    sns.scatterplot(x=df["liveRoomInfo.likeCount"], y=df["prediction"], ax=ax)
    ax.set_xlabel("Actual Like Count")
    ax.set_ylabel("Predicted Like Count")
    ax.set_title("Actual vs Predicted")
    st.pyplot(fig)

# === Raw Data Preview ===
st.header("🧾 Raw Data Sample")
st.dataframe(df.head(20))
