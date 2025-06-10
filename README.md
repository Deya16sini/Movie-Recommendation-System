# Movie-Recommendation-System
This is a content-based movie recommendation system built with Streamlit. It takes a movie name as input and suggests similar movies by analyzing genres, keywords, cast, and director using TF-IDF vectorization and cosine similarity. The dataset and similarity matrix are preprocessed and stored with pickle for quick access during runtime.

## 📌 Description
A content-based movie recommendation system built with Python and Streamlit. It suggests similar movies based on user input using metadata like genres, keywords, cast, and director. The recommendations are powered by TF-IDF vectorization and cosine similarity.

## ✅ Features
- Suggests similar movies based on a given title
- Text-based input with close match detection
- Top 5/10 recommendations based on content similarity
- Clean, user-friendly Streamlit interface

## 🛠️ Tools Used
- **Python** for backend logic  
- **Pandas** & **NumPy** for data manipulation  
- **Scikit-learn** for TF-IDF and cosine similarity  
- **difflib** for fuzzy matching of movie titles  
- **Streamlit** for the web interface  
- **Pickle** for model/data serialization

## ⚙️ How It Works
1. The movie dataset (`Project19.csv`) is loaded and preprocessed.
2. Important metadata like genres, keywords, cast, and director are combined.
3. TF-IDF Vectorizer converts this text into numerical features.
4. Cosine similarity measures the closeness between movies.
5. Based on the user input, the system finds the closest title and suggests the most similar movies.
6. Preprocessed data and similarity matrix are stored using `pickle` for efficiency.

## 🚧 Future Improvements
- Add movie posters and overviews using the TMDB API
- Implement genre or year-based filtering
- Enable collaborative or hybrid filtering
- Improve fuzzy matching accuracy for title inputs
- Add user ratings and feedback mechanism

---

