## Overview

This project is a movie recommender system that suggests movies based on similarity. It utilizes a dataset of movie information and credits to provide personalized recommendations.

## Features

*   **Movie Recommendation:** Get recommendations for movies similar to a selected one.
*   **Poster Display:** View movie posters for recommended films.

## Installation

To set up and run this project locally, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone <your-repository-url>
    cd Movie_Recommender
    ```
2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows, use `env\Scripts\activate`
    ```
3.  **Install dependencies:**
    The project requires the following Python libraries:
    *   `streamlit`
    *   `requests`
    *   `pickle`

    You can install them using pip:
    ```bash
    pip install -r requirements.txt
    ```
    (The `requirements.txt` file contains `streamlit` and other dependencies.)
4.  **Set up Streamlit configuration:**
    A `setup.sh` script is provided to configure Streamlit. This script creates a `.streamlit` directory and sets the port.
    ```bash
    ./setup.sh
    ```

## Usage

To run the movie recommender application:

1.  **Ensure all dependencies are installed.**
2.  **Run the Streamlit application:**
    ```bash
    streamlit run app.py
    ```
    This will open the application in your web browser.

## Project Structure

*   `app.py`: The main Streamlit application file containing the recommendation logic and UI.
*   `setup.py`: Used for packaging the project.
*   `requirements.txt`: Lists the Python dependencies.
*   `tmdb_5000_movies.csv`: Dataset containing movie information (budget, genres, overview, etc.).
*   `tmdb_5000_credits.csv`: Dataset containing movie credits (cast, crew).
*   `env/`: (If created) Virtual environment for the project.
*   `.git/hooks/`: Contains various Git hook samples.

## Data Sources

The project uses the following datasets:

*   [TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)

## API Key

The `app.py` file uses an API key for The Movie Database (TMDb) to fetch movie posters. Please ensure you have a valid API key if you plan to modify or extend the functionality.

## Authors

*   Khang Quang (khangquang305@gmail.com)
*   Pal Dunganari (dungaranipal@gmail.com)
