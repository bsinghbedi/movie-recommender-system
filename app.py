import streamlit as st
import pickle
import pandas as pd

movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

cosine_sim = pickle.load(open('cosine_sim.pkl', 'rb'))


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = cosine_sim[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:11]

    recommended_movies = []
    for i in movie_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

st.title('Movie Recommender System')


selected_movie_name = st.selectbox(
'Select movie name below for recommendations.',
movies['title'].values)

if st.button('Recommend'):
    recommendations =recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)

