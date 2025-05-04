# Movie Recommender System

A content-based movie recommendation system that suggests similar movies based on your selection. The system analyzes movie features like genres, keywords, cast, and crew to find the most similar movies.

![Movie Recommender Screenshot](screenshots/app_screenshot.png)

## Features

- Interactive web interface built with Streamlit
- Content-based filtering using movie metadata
- Real-time movie poster fetching from TMDB API
- Responsive design that works on desktop and mobile

## How It Works

The recommendation engine uses:
- Natural Language Processing techniques
- Cosine similarity to find movies with similar content features
- The TMDB (The Movie Database) API for movie data and posters

## Installation

### Prerequisites

- Python 3.7+
- pip (Python package installer)

### Setup for macOS

1. Clone this repository:
   ```
   git clone https://github.com/sankalp-jha/movie-recommender.git
   cd movie-recommender
   ```

2. Create and activate a virtual environment (as used in development):
   ```
   python -m venv jupyter-env
   source jupyter-env/bin/activate
   ```

3. Install the required dependencies:
   ```
   pip install streamlit pandas numpy scikit-learn requests pickle-mixin
   ```

### Setup for Windows

1. Clone this repository:
   ```
   git clone https://github.com/sankalp-jha/movie-recommender.git
   cd movie-recommender
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv venv
   venv\Scripts\activate
   ```

3. Install the required dependencies:
   ```
   pip install streamlit pandas numpy scikit-learn requests pickle-mixin
   ```

## Running the Application

1. Make sure your virtual environment is activated
2. Run the Streamlit app:
   ```
   streamlit run app.py
   ```
3. The app will open in your default web browser at http://localhost:8501

## Project Structure

```
movie-recommender/
├── app.py                  # Streamlit web application
├── model/
│   ├── movie_list.pkl      # Preprocessed movie data
│   └── similarity.pkl      # Similarity matrix
├── model.ipynb             # Jupyter notebook for model development
└── README.md               # Project documentation
```

## Model Training

The recommendation model was trained using:
1. TMDB 5000 Movie Dataset
2. Text processing and vectorization with CountVectorizer
3. Cosine similarity calculation between movie feature vectors

For details on the model training process, see the `model.ipynb` file.

## Credits

- Created by Sankalp Jha
- Movie data from [TMDB 5000 Movie Dataset](https://www.kaggle.com/tmdb/tmdb-movie-metadata)
- Movie posters from [The Movie Database API](https://www.themoviedb.org/documentation/api)

## Connect with Me

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/sankalp-jha)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/sankalp-jha)
[![Twitter](https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/sankalp_jha)

## License

This project is licensed under the MIT License - see the LICENSE file for details.
