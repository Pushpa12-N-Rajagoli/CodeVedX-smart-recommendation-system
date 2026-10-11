import os
import joblib

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from preprocess import load_data


# Load movie dataset
data = load_data()


# Create TF-IDF vectorizer
vectorizer = TfidfVectorizer(
    stop_words="english"
)


# Convert movie features into TF-IDF vectors
tfidf_matrix = vectorizer.fit_transform(
    data["combined_features"]
)


# Calculate cosine similarity
similarity_matrix = cosine_similarity(
    tfidf_matrix
)


# Create models folder if it does not exist
os.makedirs("../models", exist_ok=True)


# Save TF-IDF vectorizer
joblib.dump(
    vectorizer,
    "../models/tfidf_vectorizer.pkl"
)


# Save similarity matrix
joblib.dump(
    similarity_matrix,
    "../models/similarity_matrix.pkl"
)


# Save movie data
joblib.dump(
    data,
    "../models/movie_data.pkl"
)


print("Model trained successfully!")
print("TF-IDF vectorizer saved.")
print("Similarity matrix saved.")
print("Movie data saved.")