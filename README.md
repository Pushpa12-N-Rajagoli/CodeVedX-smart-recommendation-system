# 🎬 Smart Movie Recommendation System

An AI-powered movie recommendation system built using Python, Machine Learning, TF-IDF, and Cosine Similarity.

The system recommends movies similar to a movie selected by the user based on movie genres, keywords, and descriptions.

---

## 📌 Project Overview

The Smart Movie Recommendation System uses a content-based filtering approach to recommend movies.

The system analyzes the features of movies and calculates their similarity using **TF-IDF Vectorization** and **Cosine Similarity**.

Users can select a movie from the web interface and receive a list of similar movie recommendations.

---

## ✨ Features

- Movie selection through a web interface
- AI-based movie recommendations
- Content-based filtering
- TF-IDF feature extraction
- Cosine Similarity calculation
- Top 5 similar movie recommendations
- Genre information for recommended movies
- Similarity score for recommendations
- Interactive movie cards
- Hover animation on recommendation cards
- Responsive web interface

---

## 🛠️ Technologies Used

- Python
- Flask
- Pandas
- NumPy
- Scikit-learn
- TF-IDF
- Cosine Similarity
- Joblib
- HTML
- CSS

---

## 🧠 How the System Works

The recommendation system follows these steps:

1. The movie dataset is loaded.
2. Missing values are handled.
3. Movie genre, keywords, and description are combined.
4. TF-IDF converts the movie information into numerical vectors.
5. Cosine Similarity calculates similarity between movies.
6. The similarity matrix is saved.
7. The user selects a movie.
8. The system finds the selected movie.
9. Movies with the highest similarity scores are identified.
10. The top 5 recommendations are displayed.

---

## 📂 Project Structure

```text
smart_recommendation_system/
│
├── data/
│   └── movies.csv
│
├── models/
│   ├── tfidf_vectorizer.pkl
│   ├── similarity_matrix.pkl
│   └── movie_data.pkl
│
├── src/
│   ├── preprocess.py
│   ├── train_model.py
│   └── recommender.py
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
