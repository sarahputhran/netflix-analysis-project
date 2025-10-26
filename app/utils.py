"""
Utility module for the Netflix Analysis app

- Applies global dark blue theme with Netflix red highlights
- Handles data loading with Streamlit caching
"""

from typing import Tuple
import os
import pandas as pd
import streamlit as st

# Define dark blue + Netflix red theme
THEME = {
    "primary": "#318E9F",
    "secondary": "#3FA6AB",
    "accent1": "#58C5FE",
    "accent2": "#19475F",
    "highlight": "#FF4B4B",
    "highlight_dark": "#D93C3C",
    "background": "#0A1923",
    "background_alt": "#132936",
    "text_primary": "#FFFFFF",
    "text_secondary": "#B8C7D1"
}


# Apply global theme and font styling
def apply_theme():
    """
    Apply global dark Netflix theme and Aptos font across all pages
    """
    st.markdown(
        f"""
        <style>
            @import url('https://fonts.cdnfonts.com/css/aptos');

            html, body, [class*="css"] {{
                font-family: 'Aptos', sans-serif !important;
                background-color: {THEME['background']} !important;
                color: {THEME['text_primary']};
            }}

            .stApp {{
                background-color: {THEME['background']} !important;
            }}

            .block-container {{
                background-color: {THEME['background']} !important;
                padding-top: 2rem;
                padding-bottom: 2rem;
            }}

            h1, h2, h3, h4, h5, h6 {{
                color: {THEME['text_primary']};
                font-weight: 600;
            }}

            p, li, span {{
                color: {THEME['text_secondary']};
                font-weight: 400;
            }}

            hr {{
                border: 1px solid {THEME['accent1']};
            }}

            .stAlert {{
                background-color: {THEME['background_alt']}AA !important;
                color: {THEME['text_primary']};
                border-radius: 6px;
            }}

            .stButton>button {{
                background-color: {THEME['highlight']};
                color: {THEME['text_primary']};
                border-radius: 8px;
                border: none;
                padding: 0.6em 1.2em;
                transition: 0.3s ease;
                font-weight: 500;
            }}

            .stButton>button:hover {{
                background-color: {THEME['highlight_dark']};
                transform: scale(1.03);
            }}
        </style>
        """,
        unsafe_allow_html=True
    )


# Load main cleaned dataset
@st.cache_data(ttl=60 * 60 * 24)
def load_master_data(path: str = r"C:\Users\Admin\OneDrive\Desktop\Netflix Project\netflix-analysis-project\data\cleaned\netflix_titles_clean.csv") -> pd.DataFrame:
    """
    Load main cleaned Netflix titles CSV
    """
    df = pd.read_csv(path)
    if "date_added_year" not in df.columns:
        if "date_added" in df.columns:
            df["date_added"] = pd.to_datetime(df["date_added"], errors="coerce")
            df["date_added_year"] = df["date_added"].dt.year
        else:
            df["date_added_year"] = pd.NA
    return df


# Load helper aggregated datasets
@st.cache_data(ttl=60 * 60 * 24)
def load_helper_tables(cleaned_folder: str = r"C:\Users\Admin\OneDrive\Desktop\Netflix Project\netflix-analysis-project\data\cleaned") -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """
    Load cleaned Netflix data and all helper CSVs
    """
    df_clean = pd.read_csv(os.path.join(cleaned_folder, "netflix_titles_clean.csv"))
    agg_by_year_type = pd.read_csv(os.path.join(cleaned_folder, "agg_by_year_type.csv"))
    agg_by_genre = pd.read_csv(os.path.join(cleaned_folder, "agg_by_genre.csv"))
    agg_by_country = pd.read_csv(os.path.join(cleaned_folder, "agg_by_country.csv"))
    return df_clean, agg_by_year_type, agg_by_genre, agg_by_country


# Preview helper for quick testing
def preview_loaded_data() -> None:
    """
    Print summary of loaded datasets for quick verification
    """
    df_clean, agg_by_year_type, agg_by_genre, agg_by_country = load_helper_tables()
    print(f"Main cleaned dataset rows: {len(df_clean)}")
    print("Columns:", list(df_clean.columns))
    print(f"agg_by_year_type rows: {len(agg_by_year_type)}")
    print(f"agg_by_genre rows: {len(agg_by_genre)}")
    print(f"agg_by_country rows: {len(agg_by_country)}")