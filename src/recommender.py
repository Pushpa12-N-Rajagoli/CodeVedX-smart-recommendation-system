import joblib
from pathlib import Path


# Project folder
BASE_DIR = Path(__file__).resolve().parent.parent


# Load saved files
similarity_matrix = joblib.load(
    BASE_DIR / "models" / "similarity_matrix.pkl"
)

movie_data = joblib.load(
    BASE_DIR / "models" / "movie_data.pkl"
)


def get_recommendations(movie_title, number_of_recommendations=5):

    # Find selected movie
    matches = movie_data[
        movie_data["title"].str.strip().str.lower()
        == movie_title.strip().lower()
    ]

    # Movie not found
    if matches.empty:
        return []

    # Get selected movie index
    movie_index = matches.index[0]

    # Get similarity scores
    scores = list(
        enumerate(similarity_matrix[movie_index])
    )

    # Sort from highest to lowest similarity
    scores = sorted(
        scores,
        key=lambda x: x[1],
        reverse=True
    )

    recommendations = []

    # Skip the selected movie itself
    for index, score in scores:

        if index == movie_index:
            continue

        recommendations.append({
            "title": movie_data.iloc[index]["title"],
            "genre": movie_data.iloc[index]["genre"],
            "score": round(float(score) * 100, 2)
        })

        if len(recommendations) == number_of_recommendations:
            break

    return recommendations