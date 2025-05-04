import pickle
import streamlit as st
import requests

# Set page configuration
st.set_page_config(
    page_title="Movie Recommender System",
    page_icon="🎬",
    layout="wide"
)

# Add custom CSS
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

# Functions
def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)
    return recommended_movie_names, recommended_movie_posters

# Main app
st.markdown("<h1 class='main-header'>🎬 Movie Recommender System</h1>", unsafe_allow_html=True)

# Load data
movies = pickle.load(open('movie_list.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

# Add description
st.markdown("""
This app recommends movies similar to your selection based on content features like genre, keywords, cast, and crew.
""")

# Create sidebar for additional info
with st.sidebar:
    st.header("About")
    st.info("This movie recommender uses content-based filtering to suggest similar movies.")
    st.header("How it works")
    st.write("1. Select a movie you like")
    st.write("2. Click 'Show Recommendations'")
    st.write("3. Discover 5 similar movies")
    
    # Add creator information
    st.markdown("---")
    st.header("Creator")
    st.markdown("<div style='text-align: center;'><h3>Made by Sankalp Jha</h3></div>", unsafe_allow_html=True)
    
    # Social links
    st.subheader("Connect with me")
    cols = st.columns(3)
    with cols[0]:
        st.markdown("[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/sankalp-jha-18a95a244/)")
    with cols[1]:
        st.markdown("[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/blackdragoon26)")
    with cols[2]:
        st.markdown("[![Twitter](https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/Sankalpjha26)")
    
    # Add a footer
    st.markdown("---")
    st.caption("© 2025 Sankalp Jha. All rights reserved.")

# Movie selection
movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

# Recommendation button
if st.button('Show Recommendations', key='recommend_button'):
    with st.spinner('Finding movies for you...'):
        recommended_movie_names, recommended_movie_posters = recommend(selected_movie)
        
        # Display recommendations in columns
        cols = st.columns(5)
        for i in range(5):
            with cols[i]:
                st.image(recommended_movie_posters[i], use_container_width=True)
                st.markdown(f"<p class='movie-title'>{recommended_movie_names[i]}</p>", unsafe_allow_html=True)

