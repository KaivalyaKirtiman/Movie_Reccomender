from surprise import Dataset, Reader, SVD
from surprise.model_selection import train_test_split, accuracy
import pandas as pd

def train_svd_model(merged_df):
    """
    Trains an SVD model using the Surprise library and returns the trained model.
    """
    reader = Reader(rating_scale=(0.5, 5.0))
    data = Dataset.load_from_df(merged_df[['userId', 'movieId', 'rating']], reader)

    trainset, testset = train_test_split(data, test_size=0.2)
    algo = SVD()  # Or any other Surprise algorithm

    algo.fit(trainset)
    predictions = algo.test(testset)
    rmse = accuracy.rmse(predictions)
    print(f"Model trained with RMSE: {rmse:.4f}")

    return algo
