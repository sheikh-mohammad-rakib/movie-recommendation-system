import pickle
import streamlit as st
import requests
import gdown
import io

def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
    data = requests.get(url).json()
    poster_path = data.get('poster_path')
    if poster_path:
        return "https://image.tmdb.org/t/p/w500/" + poster_path
    return "https://via.placeholder.com/150?text=No+Poster"

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

def load_pickle_from_drive(file_id):
    # Use gdown to get the content of large files directly
    url = f"https://drive.google.com/uc?id={file_id}"
    output = io.BytesIO()
    gdown.download(url, output, quiet=False, fuzzy=True)
    output.seek(0)
    return pickle.load(output)

# 🔁 Replace with your actual file IDs from Google Drive
movie_list_file_id = "1dBSf8HpSIfpl1IyH6Q_KkE1AaWd6JnCU"
similarity_file_id = "1sj5n62qMqNPZStD7t3CBiZZF6oayGCmm"

# Load pickles directly into memory (no disk write)
movies = load_pickle_from_drive(movie_list_file_id)
similarity = load_pickle_from_drive(similarity_file_id)

# UI
st.header('🎬 Movie Recommender System')
if movies is not None and similarity is not None:
    movie_list = movies['title'].values
    selected_movie = st.selectbox("Type or select a movie from the dropdown", movie_list)

    if st.button('Show Recommendation'):
        recommended_movie_names, recommended_movie_posters = recommend(selected_movie)
        cols = st.columns(5)
        for i in range(5):
            with cols[i]:
                st.text(recommended_movie_names[i])
                st.image(recommended_movie_posters[i])
