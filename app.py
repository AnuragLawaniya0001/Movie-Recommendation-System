import streamlit as st
import pickle
import requests

def fetch_data(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=bfdbafa3c53f890976e1cf78ce1a0f5c&append_to_response=videos,images"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(data)
        poster_path = data.get('poster_path')  # Use .get() to safely retrieve the value
        if poster_path:
            return "https://image.tmdb.org/t/p/w500/" + poster_path
        else:
            return "Poster path not found"
    else:
        return "Failed to fetch data"

def recommend(movie):
    movie_index = movies_list[movies_list['title'] == movie].index[0]
    distance = similarity[movie_index]
    movie_lists = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:16]
    recommended_movies = []
    recommended_movies_poster = []
    for i in movie_lists:
        movie_id = movies_list.iloc[i[0]].movie_id
        recommended_movies.append(movies_list.iloc[i[0]].title)
        recommended_movies_poster.append(fetch_data(movie_id))
    return recommended_movies, recommended_movies_poster

similarity = pickle.load(open('similarity.pkl', 'rb'))
movies_list = pickle.load(open('movies.pkl', 'rb'))
movies_lists = pickle.load(open('movies.pkl', 'rb'))
movies_lists = movies_lists['title'].values

st.set_page_config(page_title="Movie Recommendation System", layout="wide")

st.title('🎬 Movie Recommendation System')
st.markdown("## Find movies similar to your favorites")

selected_movie_name = st.selectbox("Search Movie", movies_lists)

if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)  # Use st.columns instead of st.beta_columns for Streamlit 1.0 and later

    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])

    col1, col2, col3, col4, col5 = st.columns(5)  # Use st.columns instead of st.beta_columns for Streamlit 1.0 and later

    with col1:
        st.text(names[5])
        st.image(posters[5])
    with col2:
        st.text(names[6])
        st.image(posters[6])
    with col3:
        st.text(names[7])
        st.image(posters[7])
    with col4:
        st.text(names[8])
        st.image(posters[8])
    with col5:
        st.text(names[9])
        st.image(posters[9])

    col1, col2, col3, col4, col5 = st.columns(
        5)  # Use st.columns instead of st.beta_columns for Streamlit 1.0 and later

    with col1:
        st.text(names[10])
        st.image(posters[10])
    with col2:
        st.text(names[11])
        st.image(posters[11])
    with col3:
        st.text(names[12])
        st.image(posters[12])
    with col4:
        st.text(names[13])
        st.image(posters[13])
    with col5:
        st.text(names[14])
        st.image(posters[14])


st.markdown("---")

