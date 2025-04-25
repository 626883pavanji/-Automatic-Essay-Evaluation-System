import pickle
# Load model and vectorizer
with open('feedback_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open('tfidf_vectorizer.pkl', 'rb') as vec_file:
    vectorizer = pickle.load(vec_file)

def get_feedback(essay):
    essay_vector = vectorizer.transform([essay])
    prediction = model.predict(essay_vector)
    return prediction[0]


