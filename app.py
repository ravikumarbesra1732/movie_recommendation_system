import streamlit as st
import pickle
import pandas as pd
import requests
#0ebe499825735294e229a6e2d4bb9d04
import requests

def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=0ebe499825735294e229a6e2d4bb9d04&language=en-US"
    data = requests.get(url).json()
    poster_path = data.get("poster_path")  # safer than data['poster_path']
    if poster_path:
        return "https://image.tmdb.org/t/p/w500" + poster_path
    else:
        return "https://via.placeholder.com/500x750?text=No+Image"



def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movie_names = []
    recommended_movie_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_names.append(movies.iloc[i[0]].title)
        recommended_movie_posters.append(fetch_poster(movie_id))

    return recommended_movie_names, recommended_movie_posters


movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('Movie Recommender System')


selected_movie_name  = st.selectbox('How would you like to connected?',movies['title'].values)

if st.button("Recommend"):
    names, posters = recommend(selected_movie_name)

    cols = st.columns(5)
    for idx, col in enumerate(cols):
        with col:
            st.text(names[idx])
            st.image(posters[idx])

# import streamlit as st
# import pickle
# import pandas as pd
# import requests
#
# # -------- Fetch Poster --------
# def fetch_poster(movie_id):
#     url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=0ebe499825735294e229a6e2d4bb9d04&language=en-US"
#     data = requests.get(url).json()
#     poster_path = data.get("poster_path")
#     if poster_path:
#         return "https://image.tmdb.org/t/p/w500" + poster_path
#     else:
#         return "https://via.placeholder.com/500x750?text=No+Image"
#
# # -------- Recommend Function --------
# def recommend(movie):
#     movie_index = movies[movies['title'] == movie].index[0]
#     distances = similarity[movie_index]
#     movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
#
#     recommended_movie_names = []
#     recommended_movie_posters = []
#     for i in movies_list:
#         movie_id = movies.iloc[i[0]].movie_id
#         recommended_movie_names.append(movies.iloc[i[0]].title)
#         recommended_movie_posters.append(fetch_poster(movie_id))
#
#     return recommended_movie_names, recommended_movie_posters
#
# # -------- Load Data --------
# movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
# movies = pd.DataFrame(movies_dict)
# similarity = pickle.load(open('similarity.pkl', 'rb'))
#
# # -------- Streamlit UI --------
# st.title("🎬 Movie Recommender System")
#
# selected_movie = st.selectbox(
#     "How would you like to connected?",
#     movies['title'].values
# )
#
# if st.button("Recommend"):
#     names, posters = recommend(selected_movie)
#
#     cols = st.columns(5)
#     for idx, col in enumerate(cols):
#         with col:
#             st.text(names[idx])
#             st.image(posters[idx])
