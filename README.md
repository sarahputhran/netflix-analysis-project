🎬 Netflix Data Analysis & Recommender System

An end-to-end data analysis and recommendation system built using Python, featuring interactive dashboards, content insights, and a TF-IDF–based recommender model integrated into a Streamlit web app.


---

🚀 Live App

🔗 Streamlit Cloud Deployment:
👉 https://netflix-analysis-project-qpb78kdd5ljd2xc6abgn85.streamlit.app/


---

💻 Run Locally

1. Clone the Repository

git clone https://github.com/sarahputhran/netflix-analysis-project.git
cd netflix-analysis-project

2. Create and Activate Virtual Environment

python -m venv venv
venv\Scripts\activate   # on Windows
# or
source venv/bin/activate  # on macOS/Linux

3. Install Dependencies

pip install -r requirements.txt

4. Run the Streamlit App

streamlit run app/App.py

Then open the link shown in your terminal (usually http://localhost:8501) to view the app locally.


---

📊 Features

Data Cleaning & Preprocessing using Pandas and Scikit-learn

Interactive Visualizations built with Plotly, Tableau, and Power BI

Content-Based Recommender System using TF-IDF Vectorization and Cosine Similarity

Streamlit Multipage Application with consistent theming and cloud-hosted model integration

Hugging Face Model Hosting for persistent and reliable access



---

🧠 Tech Stack

Category	Tools / Libraries

Language	Python
Frameworks	Streamlit, scikit-learn
Visualization	Plotly, Tableau, Power BI
Model Hosting	Hugging Face
Version Control	Git & GitHub
Deployment	Streamlit Cloud



---

📁 Project Structure

netflix-analysis-project/
│
├── app/
│   ├── App.py
│   ├── pages/
│   │   ├── 01_Home.py
│   │   ├── 02_Dashboards.py
│   │   └── 03_Recommender.py
│   ├── models/ (model files hosted on Hugging Face)
│   ├── theme.py
│   └── utils.py
│
├── data/cleaned/
│   ├── netflix_titles_clean.csv
│   ├── agg_by_country.csv
│   ├── agg_by_genre.csv
│   └── agg_by_year_type.csv
│
├── docs/powerbi/
│   └── Netflix_Titles_PowerBI.pbix
│
├── notebooks/ (data cleaning, EDA, model building)
│
├── requirements.txt
└── README.md


---

📚 Dataset

Source: Netflix Titles Dataset on Kaggle
👉 https://www.kaggle.com/shivamb/netflix-shows

Cleaned and preprocessed for analysis and modeling.


---

🧠 Model Files (Hosted on Hugging Face)

TF-IDF Vectorizer: https://huggingface.co/sarahputhran/Netflix_Project_Models/blob/main/tfidf_vectorizer.pkl

Cosine Similarity Matrix: https://huggingface.co/sarahputhran/Netflix_Project_Models/blob/main/cosine_similarity.pkl

Data Reference: https://huggingface.co/sarahputhran/Netflix_Project_Models/blob/main/data_reference.pkl



---

📈 Insights

Content growth peaked between 2015–2020.

Movies dominate Netflix’s catalog, but TV Shows have grown steadily.

The U.S., India, and the U.K. lead in total Netflix titles.

Drama, International Movies, and Comedies are the most common genres.



---

🧩 Future Improvements

Integrate collaborative filtering for personalized recommendations

Add dynamic filters in Power BI dashboard

Replace CSVs with a database-backed pipeline for scalability



---

🪪 License

This project is open-source and available under the MIT License.


---

✅ GitHub Repository:
https://github.com/sarahputhran/netflix-analysis-project

✅ Live Streamlit App:
https://netflix-analysis-project-qpb78kdd5ljd2xc6abgn85.streamlit.app/

✅ Dataset Source (Kaggle):
https://www.kaggle.com/shivamb/netflix-shows

✅ Model Hosting (Hugging Face):
https://huggingface.co/sarahputhran/Netflix_Project_Models
