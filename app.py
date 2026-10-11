from flask import Flask, render_template, request
from src.recommender import get_recommendations

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():

    recommendations = []
    movie_title = ""

    if request.method == "POST":

        movie_title = request.form.get("movie_title", "").strip()

        if movie_title:
            recommendations = get_recommendations(
                movie_title,
                5
            )

    return render_template(
        "index.html",
        recommendations=recommendations,
        movie_title=movie_title
    )


if __name__ == "__main__":
    app.run(debug=True)