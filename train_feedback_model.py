import nltk
import pickle
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
# Download NLTK data if needed
nltk.download('punkt')
# Sample training data (add more data as needed)
# essays = [
#     "This essay is terrible. So many grammar mistakes and poor structure.",
#     "Excellent writing, very clear and well structured. Grammar is perfect.",
#     "Good effort, but grammar and sentence structure need improvement.",
#     "Fair attempt, but lacks clarity and good language usage.",
#     "Outstanding essay! Very well written and highly structured.",
#     "Needs improvement. Too many errors in grammar and weak arguments." ,
# ]
# feedbacks = [
#     "Needs improvement. Work on grammar, sentence structure, and content.",
#     "Excellent. Improve your structure and your grammar is very good.",
#     "Good job! Improve grammar and structure for better clarity.",
#     "Good job! Improve grammar and structure for better clarity.",
#     "Excellent work you did.",
#     "Needs improvement. Work on grammar, sentence structure, and content."
# ]

df = pd.read_csv(r"C:\Users\pavan rajpali\OneDrive\Desktop\flask\flask_app\venv\training_data.csv")


essays = df['essay'].values
feedbacks = df['feedback'].values

if df.isnull().values.any():
    print("Warning: Missing values found in the dataset. Dropping missing rows.")
    df.dropna(inplace=True)
    
# Convert text to TF-IDF features
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(essays)

# Train model
model = LogisticRegression()
model.fit(X, feedbacks)

# Save model and vectorizer using pickle
with open('feedback_model.pkl', 'wb') as model_file:
    pickle.dump(model, model_file)

with open('tfidf_vectorizer.pkl', 'wb') as vec_file:
    pickle.dump(vectorizer, vec_file)

print("Model and vectorizer saved successfully.")



# import nltk
# import pickle
# import pandas as pd
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.linear_model import LogisticRegression

# # Download NLTK tokenizer if not already downloaded
# nltk.download('punkt')

# # Load training data from CSV
# data_path = r"C:\Users\pavan rajpali\OneDrive\Desktop\flask\flask_app\venv\training_data.csv"
# df = pd.read_csv(data_path)

# # Check for missing values
# if df.isnull().values.any():
#     print("Warning: Missing values found in the dataset. Dropping missing rows.")
#     df.dropna(inplace=True)

# # Extract essays and feedbacks
# essays = df['essay'].values
# feedbacks = df['feedback'].values

# # Convert text to TF-IDF features
# vectorizer = TfidfVectorizer()
# X = vectorizer.fit_transform(essays)

# # Train logistic regression model
# model = LogisticRegression(max_iter=1000)
# model.fit(X, feedbacks)

# # Save model and vectorizer using pickle
# with open('feedback_model.pkl', 'wb') as model_file:
#     pickle.dump(model, model_file)

# with open('tfidf_vectorizer.pkl', 'wb') as vec_file:
#     pickle.dump(vectorizer, vec_file)

# print("✅ Model and vectorizer saved successfully.")
