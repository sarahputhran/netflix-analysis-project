import pandas as pd
from pathlib import Path

clean_path = Path("data/cleaned/netflix_titles_clean.csv")
out_dir = Path("data/cleaned")
out_dir.mkdir(parents=True, exist_ok=True)

if not clean_path.exists():
    raise SystemExit(f"ERROR: cleaned CSV not found at {clean_path}. Run notebooks/02 first.")

df = pd.read_csv(clean_path)

# Aggregation 1: Titles added by year/type
agg_by_year_type = (
    df.groupby(['date_added_year', 'type']) # Group by year and type
      .size() # Counts occurrences in each group
      .reset_index(name='count') # Convert Series to DataFrame
      .sort_values(['date_added_year','type']) # Sort by year and type
)
agg_by_year_type.to_csv(out_dir / "agg_by_year_type.csv", index=False)

# Aggregation 2: Titles by genre (exploded)
df_genres = df.dropna(subset=['genres_str']).copy() # Drop rows with NaN genres
df_genres['genres_list'] = df_genres['genres_str'].str.split('|') # Split pipe-joined genres into lists
df_genres = df_genres.explode('genres_list') # Explode lists into separate rows
# Now aggregate by genre
agg_by_genre = (
    df_genres['genres_list'].value_counts() # Count occurrences of each genre
    .reset_index() # Convert Series to DataFrame
    .rename(columns={'index': 'genre', 'genres_list': 'count'}) # Rename columns
)
agg_by_genre.to_csv(out_dir / "agg_by_genre.csv", index=False)

# Aggregation 3: Titles by primary country (top N)
agg_by_country = (
    df['primary_country'].value_counts()
      .reset_index() # Convert Series to DataFrame
      .rename(columns={'index':'primary_country','primary_country':'count'})
)
agg_by_country.to_csv(out_dir / "agg_by_country.csv", index=False)

print("Saved helper files:")
print("-", out_dir / "agg_by_year_type.csv")
print("-", out_dir / "agg_by_genre.csv")
print("-", out_dir / "agg_by_country.csv")
