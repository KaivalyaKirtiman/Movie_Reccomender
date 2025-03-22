# main.py
from src.data_preparation import load_data, prepare_data
from src.model_training import train_svd_model
from src.recommendation import get_top_n_recommendations

def main():
    # 1) Load data from MySQL
    movies_df, ratings_df, tags_df = load_data()

    # 2) Prepare/merge data
    merged_df = prepare_data(movies_df, ratings_df)

    # 3) Train model
    algo = train_svd_model(merged_df)

    # 4) Generate recommendations for a sample user (e.g., userId = 1)
    user_id = 1
    top_5 = get_top_n_recommendations(algo, user_id, movies_df, n=5)

    # 5) Print or log the recommendations
    print(f"Top 5 recommendations for user {user_id}:")
    for title, rating in top_5:
        print(f" - {title} (pred: {rating:.2f})")

if __name__ == "__main__":
    main()
