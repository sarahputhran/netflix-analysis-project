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

# Apply theme
apply_theme()

# ───────────────────── Custom Styling ─────────────────────
st.markdown(f"""
    <style>
        #MainMenu, footer, header {{visibility: hidden;}}

        .main {{
            text-align: center;
            padding-top: 5%;
            padding-bottom: 5%;
        }}

        .hero-title {{
            font-size: 3rem;
            font-weight: 700;
            color: {THEME["text_primary"]};
            margin-bottom: 0.25em;
        }}
        .hero-subtitle {{
            font-size: 1.3rem;
            color: {THEME["text_secondary"]};
            margin-bottom: 2em;
        }}

        /* Button container */
        .nav-buttons {{
            display: flex;
            justify-content: center;
            gap: 2em;
            flex-wrap: wrap;
        }}

        /* Card-style buttons */
        .stButton > button {{
            background-color: {THEME["highlight"]};
            color: white;
            font-size: 1.15rem;
            padding: 0.8em 1.6em;
            border-radius: 15px;
            border: none;
            transition: all 0.3s ease;
            font-weight: 600;
            box-shadow: 0px 4px 15px rgba(0,0,0,0.1);
        }}
        .stButton > button:hover {{
            background-color: {THEME["accent1"]};
            transform: scale(1.03);
            box-shadow: 0px 6px 20px rgba(0,0,0,0.15);
        }}

        /* Footer */
        .footer {{
            margin-top: 4em;
            color: {THEME["text_secondary"]};
            font-size: 0.95rem;
        }}
    </style>
""", unsafe_allow_html=True)

# ───────────────────── Hero Section ─────────────────────
st.markdown("<div class='main'>", unsafe_allow_html=True)

st.markdown("<div class='hero-title'>🎥 Netflix Data Analysis & Recommender</div>", unsafe_allow_html=True)
st.markdown(
    "<div class='hero-subtitle'>Explore insights, visualize trends, and get personalized recommendations powered by Machine Learning.</div>",
    unsafe_allow_html=True
)

# ───────────────────── Project Overview / Problem Definition ─────────────────────
st.markdown("---")
st.markdown(
    """
### 🎯 **Goal**
To understand Netflix’s content patterns and build a recommender system that suggests titles based on description and genre similarity.

### 📌 **Objectives**
- Analyze Netflix’s catalog across years, genres, countries, and ratings.  
- Develop a **content-based recommender** using TF-IDF (description + genres) and cosine similarity.  
- Present insights through **interactive dashboards** built in Tableau, Power BI, and Plotly.  
- Integrate everything in a **Streamlit web app** for unified exploration and recommendations.

### ⚙️ **Dataset**
- Source: Netflix Titles Dataset (Kaggle)  
- Cleaned version used: `data/cleaned/netflix_titles_clean.csv`
"""
)

st.markdown("---")

# Button style (red buttons, white text) - keeps theme consistent across pages
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

# ───────────────────── Minimal Footer ─────────────────────
st.markdown(
    f"<div class='footer'>Built with Python • Streamlit • Plotly</div>",
    unsafe_allow_html=True,
)

st.markdown("</div>", unsafe_allow_html=True)