import pandas as pd


def load_data():

    data = pd.read_csv("../data/movies.csv")

    # Replace missing values
    data = data.fillna("")

    # Combine important movie information
    data["combined_features"] = (
        data["genre"] + " "
        + data["keywords"] + " "
        + data["description"]
    )

    return data