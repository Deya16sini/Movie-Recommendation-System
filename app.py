import streamlit as st
import pandas as pd
import difflib
import pickle

# Load your movie data and similarity matrix
df = pickle.load(open('movies_df.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Set page config
st.set_page_config(page_title="Movie Recommender", page_icon="🎬", layout="centered")

# Add background and styling
st.markdown("""
    <style>
    .main {
        background-color: #E6E6FA;
        padding: 2rem;
        border-radius: 10px;
    }
    .movie-title {
        font-size: 20px;
        font-weight: bold;
        color: #2c3e50;
    }
    .stApp {
        background-image: linear-gradient(to right, #e0eafc, #cfdef3);
    }
    </style>
""", unsafe_allow_html=True)

# App title
st.markdown("<h1 style='text-align: center; color: #4B0082;'>🎬 Movie Recommendation System</h1>", unsafe_allow_html=True)

# Input section
st.markdown("### 🤔 Enter your favourite movie:")
movie_name = st.text_input("")

# Recommendation logic
if movie_name:
    list_of_all_titles = df['title'].tolist()
    find_close_match = difflib.get_close_matches(movie_name, list_of_all_titles)

    if find_close_match:
        close_match = find_close_match[0]
        index_of_the_movie = df[df.title == close_match]['index'].values[0]
        similarity_score = list(enumerate(similarity[index_of_the_movie]))
        sorted_similar_movies = sorted(similarity_score, key=lambda x: x[1], reverse=True)

        st.markdown(f"<h3 style='color:#2E8B57;'>🎯 Top Recommendations based on <u>{close_match}</u>:</h3>", unsafe_allow_html=True)

        for i, movie in enumerate(sorted_similar_movies[1:11], start=1):
            index = movie[0]
            title = df[df.index == index]['title'].values[0]
            st.markdown(f"""
                <div class='main'>
                    <p class='movie-title'>🎞️ {i}. {title}</p>
                </div>
            """, unsafe_allow_html=True)

    else:
        st.error("⚠️ Sorry, no close match found. Please try another movie name.")
