# 📰 Fake News Detection using NLP and Machine Learning

## 📌 Project Overview

This project detects whether a news article is **Fake** or **Real** using Natural Language Processing (NLP) and Machine Learning.

The text is preprocessed, converted into numerical features using **TF-IDF**, and classified using **Linear Support Vector Classifier (Linear SVC)**.

---

## 🚀 Features

- Data Cleaning and Preprocessing
- NLP Text Processing
- TF-IDF Feature Extraction
- Model Comparison
- Fake/Real News Prediction
- Saved Trained Model (.pkl)
- Saved TF-IDF Vectorizer
- Ready for Streamlit Deployment

---

## 📂 Dataset

Dataset consists of two files:

- Fake.csv
- True.csv

Each article is labeled as:

- **0 → Fake News**
- **1 → Real News**

---

## 🛠 Technologies Used

- Python
- Pandas
- NumPy
- NLTK
- Scikit-learn
- Joblib
- Jupyter Notebook

---

## 📊 Project Workflow

1. Load Dataset
2. Data Cleaning
3. Text Preprocessing
   - Lowercase
   - Remove URLs
   - Remove Punctuation
   - Remove Stopwords
   - Stemming
4. TF-IDF Vectorization
5. Train-Test Split
6. Train Multiple Models
7. Model Evaluation
8. Save Best Model
9. Predict New News Articles

---

## 🤖 Models Compared

| Model | Accuracy |
|--------|----------|
| Logistic Regression | 98.87% |
| Multinomial Naive Bayes | 94.00% |
| **Linear SVC** | **99.63%** ✅ |

---

## 📈 Final Model Performance (Linear SVC)

- Accuracy: **99.63%**
- Precision: **99.63%**
- Recall: **99.63%**
- F1-score: **99.63%**

Confusion Matrix:

| | Predicted Fake | Predicted Real |
|---|---:|---:|
| Actual Fake | 4704 | 20 |
| Actual Real | 13 | 4201 |

---

## 📁 Project Structure

```
Fake-News-Detection/
│
├── data/
│   ├── Fake.csv
│   └── True.csv
│
├── notebooks/
│   └── fake_news_detection.ipynb
│
├── fake_news_model.pkl
├── tfidf_vectorizer.pkl
├── test_model.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ▶️ How to Run

Clone the repository

```bash
git clone https://github.com/Asif6106/Fake-News-Detection.git
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run

```bash
python test_model.py
```

---

## 🔮 Future Improvements

- Build a Streamlit Web Application
- Deploy the application online
- Use Lemmatization instead of Stemming for comparison
- Experiment with Transformer models such as BERT

---

## 👨‍💻 Author

**Asif Sheikh**

GitHub: https://github.com/Asif6106
