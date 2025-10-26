import os
import sys

# Fix paths first
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, "../.."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

# Now import your own modules
from utils import apply_theme
from theme import THEME

import streamlit as st
import joblib
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

st.title("🎥 Netflix Recommendation System")
st.write("Find similar Movies and TV Shows using content-based filtering.")

# Load saved models & data
try:
    tfidf = joblib.load(r"C:\Users\Admibn\OneDrive\Desktop\Netflix Project\netflix-analysis-project\app\models\tfidf_vectorizer.pkl")
    cosine_sim = joblib.load(r"C:\Users\Admibn\OneDrive\Desktop\Netflix Project\netflix-analysis-project\app\models\cosine_similarity.pkl")
    df_ref = joblib.load(r"C:\Users\Admibn\OneDrive\Desktop\Netflix Project\netflix-analysis-project\app\models\data_reference.pkl")
except FileNotFoundError:
    st.error("❌ Model files not found. Please ensure tfidf_vectorizer.pkl, cosine_similarity.pkl, and data_reference.pkl are in `app/models/`.")
    st.stop()

df_ref["title_lower"] = df_ref["title"].str.lower()

# Recommender Function
def recommend(title):
    title = title.lower().strip()
    if title not in df_ref["title_lower"].values:
        return None

    idx = df_ref.index[df_ref["title_lower"] == title][0] # Get index of the title
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:11]
    recommendations = df_ref.iloc[[i[0] for i in sim_scores]]["title"].values
    return recommendations

# Streamlit UI
title_input = st.text_input("Enter a show or movie name:", placeholder="e.g. Breaking Bad")

if st.button("Get Recommendations"):
    if not title_input:
        st.warning("Please enter a title first.")
    else:
        recs = recommend(title_input)
        if recs is None:
            st.error("Title not found in the dataset.")
        else:
            st.success(f"Top 10 Recommendations for ‘{title_input.title()}’:")
            for i, show in enumerate(recs, 1):
                st.write(f"{i}. {show}")

# Button style (red buttons, white text) - re-declare for consistency
st.markdown("""
<style>
.stButton > button {
    background-color: #E50914 !important;
    color: #ffffff !important;
    font-weight: 600;
    border-radius: 10px;
    padding: 0.6em 1.2em;
    border: none;
    transition: transform .12s ease-in-out, box-shadow .12s ease-in-out;
    box-shadow: 0 4px 12px rgba(0,0,0,0.08);
}
.stButton > button:hover {
    background-color: #B00610 !important;
    transform: translateY(-2px);
}
</style>
""", unsafe_allow_html=True)

st.markdown("---")
col1, col2 = st.columns([1, 1])
with col1:
    if st.button("Back to Home"):
        try:
            st.switch_page(r"pages\01_Home.py")
        except Exception:
            try:
                st.switch_page("01_Home")
            except Exception:
                pass
with col2:
    if st.button("View Dashboards"):
        try:
            st.switch_page(r"pages\02_Dashboards.py")
        except Exception:
            try:
                st.switch_page("02_Dashboards")
            except Exception:
                pass