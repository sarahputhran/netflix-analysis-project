🎬 Netflix Data Analysis & Recommender System

An end-to-end data analysis and recommendation system built using Python, featuring interactive dashboards, content insights, and a TF-IDF–based recommender model integrated into a Streamlit web app.


---

🚀 Live App

🔗 Streamlit Cloud Deployment:
https://netflix-analysis-project-qpb78kdd5ljd2xc6abgn85.streamlit.app/


---

💻 Run Locally

1️⃣ Clone the Repository

git clone https://github.com/sarahputhran/netflix-analysis-project.git
cd netflix-analysis-project

2️⃣ Create and Activate Virtual Environment

python -m venv venv
venv\Scripts\activate   # on Windows

or

source venv/bin/activate  # on macOS/Linux

3️⃣ Install Dependencies

pip install -r requirements.txt

4️⃣ Run the Streamlit App

streamlit run app/App.py

Then open the link shown in your terminal (usually http://localhost:8501) to view the app locally.


---

📊 Features

Data Cleaning & Preprocessing using Pandas and Scikit-learn

Interactive Visualizations with Plotly, Tableau, and Power BI

Content-Based Recommender System using TF-IDF Vectorization + Cosine Similarity

Streamlit Multipage App with consistent red-themed UI

Cloud-Hosted Models for reliable deployment (via Hugging Face)



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
│   ├── models/                # model files hosted externally on Hugging Face
│   ├── theme.py
│   └── utils.py
│
├── data/
│   └── cleaned/
│       ├── netflix_titles_clean.csv
│       ├── agg_by_country.csv
│       ├── agg_by_genre.csv
│       └── agg_by_year_type.csv
│
├── docs/
│   └── powerbi/
│       └── Netflix_Titles_PowerBI.pbix
│
├── notebooks/
│   ├── 01_initial_exploration.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_eda_analysis.ipynb
│   └── 04_recommender.ipynb
│
├── requirements.txt
└── README.md


---

📚 Dataset

Source: Netflix Titles Dataset (Kaggle)
https://www.kaggle.com/shivamb/netflix-shows

Cleaned and processed for analysis and model training.


---

🧠 Model Files (Hosted on Hugging Face)

TF-IDF Vectorizer: https://huggingface.co/sarahputhran/Netflix_Project_Models/blob/main/tfidf_vectorizer.pkl

Cosine Similarity Matrix: https://huggingface.co/sarahputhran/Netflix_Project_Models/blob/main/cosine_similarity.pkl

Data Reference: https://huggingface.co/sarahputhran/Netflix_Project_Models/blob/main/data_reference.pkl



---

📈 Insights

Content growth peaked between 2015–2020

Movies dominate, but TV Shows are rising steadily

The US, India, and UK lead in total Netflix titles

Drama, International Movies, and Comedies are the most prevalent genres



---

🧩 Future Improvements

Integrate collaborative filtering for personalized recommendations

Add dynamic filtering options in Power BI dashboard

Replace CSVs with a database-backed pipeline for scalability



---

🪪 License

This project is open-source and available under the MIT License.


---

✅ Links Summary

GitHub Repository:
https://github.com/sarahputhran/netflix-analysis-project

Live Streamlit App:
https://netflix-analysis-project-qpb78kdd5ljd2xc6abgn85.streamlit.app/

Dataset Source (Kaggle):
https://www.kaggle.com/shivamb/netflix-shows

Model Hosting (Hugging Face):
https://huggingface.co/sarahputhran/Netflix_Project_Models
