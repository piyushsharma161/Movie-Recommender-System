import pickle
import streamlit as st
import pandas as pd
import requests

def recommend(movie):
    index = movies[movies['title_x'] == movie].index[0]
    distances = similarity[index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in movies_list:
        recommended_movie_posters.append(movies.iloc[i[0]].poster_path)
        recommended_movie_names.append(movies.iloc[i[0]].title_x)
    return recommended_movie_names,recommended_movie_posters


st.header('Movie Recommender System')
similarity = pd.read_pickle(open('similarity.pkl','rb'))
#movies_dict = pd.read_pickle(open('/Users/IN22904490/PycharmProjects/movie-recommender-system/movie_dict.pkl','rb'))
movies = pd.read_pickle(open('movie.pkl','rb'))


movie_list = movies['title_x'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    recommended_movie_names,recommended_movie_posters = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])








