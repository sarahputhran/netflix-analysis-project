import streamlit as st
import time
from utils import apply_theme

# ───────────────────────────────
# Streamlit Page Configuration
# ───────────────────────────────
st.set_page_config(
    page_title="Netflix Data Analysis",
    page_icon="🎬",
    layout="wide"
)

# ───────────────────────────────
# Apply Custom Theme
# ───────────────────────────────
apply_theme()

# ───────────────────────────────
# Loading / Intro Screen
# ───────────────────────────────
st.markdown("""
    <div style='text-align:center; margin-top:20%;'>
        <h2 style='color:#E50914;'>Loading Netflix Analysis App...</h2>
        <p style='color:#aaa;'>Please wait while we set things up.</p>
    </div>
""", unsafe_allow_html=True)

# Short pause for smooth visual transition
time.sleep(1.5)

# ───────────────────────────────
# Navigation Entry
# ───────────────────────────────
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<div style='text-align:center;'>", unsafe_allow_html=True)

st.markdown("""
    <style>
        .stButton > button {
            background-color: #E50914 !important;
            color: #ffffff !important;
            font-weight: 600;
            border-radius: 10px;
            padding: 0.8em 1.5em;
            font-size: 1.1rem;
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

if st.button("🚀 Enter App"):
    try:
        st.switch_page("pages/01_Home.py")
    except Exception as e:
        st.error(f"Navigation failed: {e}")

st.markdown("</div>", unsafe_allow_html=True)