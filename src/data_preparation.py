import pandas as pd
from src.db_connection import get_connection

def load_data():
    """Fetches data from MySQL tables and returns Pandas DataFrames."""
    cnx = get_connection()
    movies_df = pd.read_sql("SELECT * FROM movies;", cnx)
    ratings_df = pd.read_sql("SELECT * FROM ratings;", cnx)
    tags_df = pd.read_sql("SELECT * FROM tags;", cnx)
    cnx.close()
    return movies_df, ratings_df, tags_df

def prepare_data(movies_df, ratings_df):
    """
    Merges movies & ratings for easier analysis.
    Cleans/handles missing values if needed.
    Returns a merged DataFrame.
    """
    merged_df = pd.merge(ratings_df, movies_df, on='movieId', how='inner')
    # Example: drop duplicates or missing values if any
    merged_df.dropna(inplace=True)
    return merged_df
