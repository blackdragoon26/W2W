import pickle
import streamlit as st
import requests

# ---------------- Page Config ----------------
st.set_page_config(
    page_title="Movie Recommender System",
    page_icon="🎬",
    layout="wide"
)

# ---------------- Custom CSS ----------------
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #FF4B4B;
        text-align: center;
    }
    .movie-title {
        font-weight: bold;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# ---------------- Functions ----------------
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        r = requests.get(url, headers=headers, timeout=5)
        r.raise_for_status()
        data = r.json()

        poster_path = data.get("poster_path")
        if poster_path:
            return "https://image.tmdb.org/t/p/w500/" + poster_path
        else:
            return "https://via.placeholder.com/300x450?text=No+Poster"

    except Exception as e:
        print("Poster error:", e)
        return "https://via.placeholder.com/300x450?text=Error"

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])

    names = []
    posters = []

    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        posters.append(fetch_poster(movie_id))
        names.append(movies.iloc[i[0]].title)

    return names, posters

# ---------------- Cache Data ----------------
@st.cache_data
def load_data():
    movies = pickle.load(open('movie_list.pkl', 'rb'))
    similarity = pickle.load(open('similarity.pkl', 'rb'))
    return movies, similarity

movies, similarity = load_data()

# ---------------- Main UI ----------------
st.markdown("<h1 class='main-header'>🎬 Movie Recommender System</h1>", unsafe_allow_html=True)

st.markdown("""
This app recommends movies similar to your selection based on content features like genre, keywords, cast, and crew.
""")

# Sidebar
with st.sidebar:
    st.header("About")
    st.info("This movie recommender uses content-based filtering to suggest similar movies.")
    st.header("How it works")
    st.write("1. Select a movie you like")
    st.write("2. Click 'Show Recommendations'")
    st.write("3. Discover 5 similar movies")

    st.markdown("---")
    st.markdown("<div style='text-align:center'><h3>Made by Sankalp Jha</h3></div>", unsafe_allow_html=True)
    st.markdown("---")
    st.caption("© 2025 Sankalp Jha")

# Movie selector
movie_list = movies['title'].values
selected_movie = st.selectbox("Type or select a movie from the dropdown", movie_list)

placeholder = st.empty()

# Button
if st.button("Show Recommendations"):
    with st.spinner("Finding movies for you..."):
        names, posters = recommend(selected_movie)

    with placeholder.container():
        cols = st.columns(5)
        for i in range(5):
            with cols[i]:
                st.image(posters[i], width=250)
                st.markdown(f"<p class='movie-title'>{names[i]}</p>", unsafe_allow_html=True)

