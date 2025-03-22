def get_top_n_recommendations(algo, user_id, movies_df, n=5):
    """
    For a given user_id, returns top-n recommended movies using the trained model.
    """
    all_movie_ids = movies_df['movieId'].unique()
    predictions = []

    for movie_id in all_movie_ids:
        pred = algo.predict(uid=user_id, iid=movie_id)
        predictions.append((movie_id, pred.est))

    # Sort by predicted rating
    predictions.sort(key=lambda x: x[1], reverse=True)
    top_n = predictions[:n]

    # Map movieId to title
    top_n_titles = []
    for (movie_id, pred_rating) in top_n:
        title = movies_df.loc[movies_df['movieId'] == movie_id, 'title'].values[0]
        top_n_titles.append((title, pred_rating))

    return top_n_titles
