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
from streamlit.components.v1 import html
import plotly.express as px
import plotly.io as pio
import pandas as pd

# Apply theme
apply_theme()

# Hide scrollbars
st.markdown("""
    <style>
    ::-webkit-scrollbar {display:none;}
    html, body {overflow:hidden;}
    iframe {border:none!important;overflow:hidden!important;}
    </style>
""", unsafe_allow_html=True)

# Title
st.title("📊 Dashboards – Tableau, Power BI & Plotly Visualizations")

st.markdown("""
Interactive dashboards built from the cleaned Netflix dataset.
Explore the **Tableau**, **Power BI**, and **Plotly** views below.
""")

st.markdown("---")

# ───────────────────── Tableau Embed ─────────────────────
st.header("🎞️ Tableau Dashboard – Netflix Titles Insights")
tableau_embed = """
<iframe src="https://public.tableau.com/views/NetflixTitlesTableau/InsightsDashboard?:embed=yes&:showVizHome=no&:toolbar=no"
        width="100%" height="1000" style="border:none;"></iframe>
"""
html(tableau_embed, height=1000)

# ───────────────────── Insights: Tableau Dashboard ─────────────────────
st.markdown("### Insights from Tableau Dashboard")
st.markdown("""
- The Tableau dashboard complements Plotly visuals with **aggregated views** of genres, types, and countries.  
- It confirms the **global dominance of U.S. and Indian content** and the rapid expansion from 2015–2020.  
- The combined dashboards reinforce Netflix’s evolution into a **data-driven, globally diversified platform**.
""")

st.markdown("---")

# ───────────────────── Power BI Dashboard (Download Link) ─────────────────────
st.header("📈 Power BI Dashboard (Download)")

# Direct download from GitHub (raw file)
pbix_url = "https://github.com/sarahputhran/netflix-analysis-project/raw/main/docs/powerbi/Netflix_Titles_PowerBI.pbix.pbix"

st.markdown("""
The Power BI dashboard was created using:
- `data/cleaned/netflix_titles_clean.csv`
- `data/cleaned/agg_by_genre.csv`

You can download it directly below 👇
""")

# Streamlit download button from URL
try:
    import requests
    response = requests.get(pbix_url)
    if response.status_code == 200:
        st.download_button(
            label="📥 Download Power BI Dashboard (.pbix)",
            data=response.content,
            file_name="Netflix_Titles_PowerBI.pbix",
            mime="application/octet-stream",
        )
    else:
        st.warning("⚠️ Unable to fetch Power BI file from GitHub.")
except Exception as e:
    st.error(f"❌ Error fetching Power BI file: {e}")

# ───────────────────── Load data from absolute paths ─────────────────────
path_clean = os.path.join(BASE_DIR, "netflix_titles_clean.csv")
path_year_type = os.path.join(BASE_DIR, "agg_by_year_type.csv")
path_genre = os.path.join(BASE_DIR, "agg_by_genre.csv")
path_country = os.path.join(BASE_DIR, "agg_by_country.csv")

df_clean = pd.read_csv(path_clean)
agg_by_year_type = pd.read_csv(path_year_type)
agg_by_genre = pd.read_csv(path_genre)
agg_by_country = pd.read_csv(path_country)

# ───────────────────── Register Plotly theme ─────────────────────
pio.templates["netflix_dark"] = pio.templates["plotly_dark"]
pio.templates["netflix_dark"].layout.update(
    paper_bgcolor=THEME["background"],
    plot_bgcolor=THEME["background_alt"],
    font=dict(family="Aptos, sans-serif", color=THEME["text_primary"]),
    colorway=[THEME["highlight"], THEME["accent1"], THEME["secondary"], THEME["primary"]],
)
pio.templates.default = "netflix_dark"

# ───────────────────── Plotly 1 – Titles by Year and Type ─────────────────────
st.subheader("📅 Number of Titles by Year and Type")
fig_year_type = px.bar(
    agg_by_year_type,
    x="date_added_year", y="count", color="type",
    barmode="group",
    color_discrete_map={"Movie": THEME["highlight"], "TV Show": THEME["accent1"]},
    labels={"date_added_year": "Year", "count": "Number of Titles"},
)
st.plotly_chart(fig_year_type, use_container_width=True)

# ───────────────────── Insights: Yearly Trends ─────────────────────
st.markdown("### Insights: Titles Added by Year")
st.markdown("""
- Netflix’s content grew exponentially from **2015 to 2020**, peaking in **2019**.  
- After 2020, the number of new titles slightly declined, possibly due to **pandemic-related slowdowns**.  
- **Movies** consistently outnumber **TV Shows**, though shows are expanding more steadily each year.
""")

# ───────────────────── Plotly 2 – Titles by Rating and Type ─────────────────────
st.subheader("⭐ Number of Titles by Rating and Type")

# Remove runtime values (anything containing 'min')
rating_counts = (
    df_clean[~df_clean["rating"].str.contains("min", case=False, na=False)]
    .groupby(["rating", "type"])
    .size()
    .reset_index(name="count")
    .sort_values("count", ascending=False)
)

fig_ratings = px.bar(
    rating_counts,
    x="count", y="rating", color="type",
    orientation="h",
    barmode="stack",
    color_discrete_map={"Movie": THEME["highlight"], "TV Show": THEME["accent1"]},
    labels={"count": "Number of Titles", "rating": "Rating"},
)
st.plotly_chart(fig_ratings, use_container_width=True)

# ───────────────────── Insights: Rating Distribution ─────────────────────
st.markdown("### Insights: Ratings and Audience Target")
st.markdown("""
- Most content is rated **TV-MA** or **TV-14**, aimed primarily at **adult and teen audiences**.  
- Very few titles fall under children’s or family ratings like **TV-Y** and **PG**.
""")

# ───────────────────── Plotly 3 – Top 10 Countries ─────────────────────
st.subheader("🌍 Top 10 Countries by Number of Titles")

# Drop missing or 'Unknown' countries
country_counts = (
    df_clean["primary_country"]
    .dropna()
    .replace("Unknown", pd.NA)
    .dropna()
    .value_counts()
    .reset_index()
)

# Rename columns properly
country_counts.columns = ["country", "title_count"]

# Take top 10 countries
top_countries = country_counts.head(10)

fig_country = px.bar(
    top_countries,
    x="title_count", y="country",
    orientation="h",
    color="title_count",
    color_continuous_scale=[THEME["accent2"], THEME["accent1"], THEME["highlight"]],
    labels={"country": "Country", "title_count": "Number of Titles"},
)
st.plotly_chart(fig_country, use_container_width=True)

# ───────────────────── Insights: Country Contributions ─────────────────────
st.markdown("### Insights: Content by Country")
st.markdown("""
- The **United States** leads Netflix’s production catalog by a large margin.  
- **India** and the **United Kingdom** follow, showing Netflix’s investment in **regional storytelling**.  
- The inclusion of countries like **Japan** and **South Korea** reflects the growing **Asian content influence**.
""")

# ───────────────────── Plotly 4 – Top 15 Genres ─────────────────────
st.subheader("🎭 Top 15 Genres on Netflix")

# Safely rename columns based on what actually exists
if "count.1" in agg_by_genre.columns:
    agg_by_genre = agg_by_genre.rename(columns={"count": "genre", "count.1": "title_count"})
elif "count_1" in agg_by_genre.columns:
    agg_by_genre = agg_by_genre.rename(columns={"count": "genre", "count_1": "title_count"})
else:
    st.error("⚠️ Neither 'count.1' nor 'count_1' found in agg_by_genre — check CSV structure.")

# Take top 15 genres
top_genres = agg_by_genre.sort_values("title_count", ascending=False).head(15)

fig_genre = px.bar(
    top_genres,
    x="title_count", y="genre",
    orientation="h",
    color="title_count",
    color_continuous_scale=[THEME["accent2"], THEME["accent1"], THEME["highlight"]],
    labels={"genre": "Genre", "title_count": "Number of Titles"},
)
st.plotly_chart(fig_genre, use_container_width=True)

# ───────────────────── Insights: Genre Popularity ─────────────────────
st.markdown("### Insights: Top Genres on Netflix")
st.markdown("""
- **Dramas**, **International Movies**, and **Comedies** dominate Netflix’s catalog.  
- These genres make up nearly **half of all available titles**, aligning with global audience preferences.  
- The mix of international and emotional storytelling genres highlights Netflix’s **broad audience strategy**.
""")

# Button style (red buttons, white text) - re-declare to ensure page-level consistency
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
            st.switch_page("01_Home.py")
        except Exception:
            try:
                st.switch_page("01_Home")
            except Exception:
                pass
with col2:
    if st.button("Go to Recommender"):
        try:
            st.switch_page("03_Recommender.py")
        except Exception:
            try:
                st.switch_page("03_Recommender")
            except Exception:
                pass