This project is a movie recommender system that suggests movies based on similarity. It utilizes a dataset of movie information and credits to provide personalized recommendations.
Features
Movie Recommendation: Get recommendations for movies similar to a selected one.
Poster Display: View movie posters for recommended films.
Installation

To set up and run this project locally, follow these steps:
Clone the repository:
git clone <your-repository-url>
cd Movie_Recommender
Create a virtual environment (recommended):
python -m venv env
source env/bin/activate  # On Windows, use `env\Scripts\activate`
Install dependencies:

The project requires the following Python libraries:
streamlit
requests
pickle
You can install them using pip:
pip install -r requirements.txt
(The requirements.txt file contains streamlit and other dependencies.)
Set up Streamlit configuration:

A setup.sh script is provided to configure Streamlit. This script creates a .streamlit directory and sets the port.
./setup.sh
Usage

To run the movie recommender application:
Ensure all dependencies are installed.
Run the Streamlit application:
streamlit run app.py
This will open the application in your web browser.
Project Structure
app.py: The main Streamlit application file containing the recommendation logic and UI.
setup.py: Used for packaging the project.
requirements.txt: Lists the Python dependencies.
tmdb_5000_movies.csv: Dataset containing movie information (budget, genres, overview, etc.).
tmdb_5000_credits.csv: Dataset containing movie credits (cast, crew).
env/: (If created) Virtual environment for the project.
.git/hooks/: Contains various Git hook samples.
Data Sources

The project uses the following datasets:
TMDB 5000 Movie Dataset

