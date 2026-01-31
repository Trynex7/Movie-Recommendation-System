import streamlit as st
import  pickle

def recommendation(movie):
  m_index = movies[movies['original_title'] == movie].index[0]
  similarity_score = sorted(list(enumerate(similarity[m_index])), reverse=True, key=lambda x:x[1])[1:6]
  recommended_movies = []
  for i in similarity_score:
      recommended_movies.append(movies['original_title'][i[0]])

  return recommended_movies

st.title('Movie Recommendation System')

movies = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

movie = st.selectbox(
    "Select a movie to find similar movies",
    (movies['original_title']))

if st.button("Recommended Movies:"):
    recommendations = recommendation(movie)

    cols = st.columns(len(recommendations))

    for idx, r in enumerate(recommendations):
        with cols[idx]:
            #st.write(r)
            st.markdown(
                f"""
                            <div style="
                                background-color: rgba(255,255,255,0.9);
                                padding: 16px;
                                border-radius: 14px;
                                text-align: center;
                                color: black;
                                font-weight: 600;
                                box-shadow: 0 6px 15px rgba(0,0,0,0.25);
                            ">
                                {r}
                            </div>
                            """,
                unsafe_allow_html=True
            )

image_path = "https://static.vecteezy.com/system/resources/thumbnails/043/555/146/small_2x/cinema-background-realistic-film-strip-in-perspective-3d-isometric-film-strip-design-cinema-movie-festival-poster-template-for-festival-modern-cinema-with-place-for-text-film-industry-concept-vector.jpg"  # replace with your image path

st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("{image_path}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    </style>
    """,
    unsafe_allow_html=True
)