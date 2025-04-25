
#  with data based integration 

# from flask import Flask, request, jsonify
# from flask_cors import CORS
# from flask_sqlalchemy import SQLAlchemy
# from datetime import datetime
# from feedback_predictor import get_feedback  # ML model file

# app = Flask(__name__)
# CORS(app)

# # SQLite config
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///essays.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)

# # Database model
# class EssaySubmission(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     essay_text = db.Column(db.Text, nullable=False)
#     score = db.Column(db.Integer, nullable=False)
#     feedback = db.Column(db.String(255), nullable=False)
#     timestamp = db.Column(db.DateTime, default=datetime.utcnow)

# # Create the table (run once)
# with app.app_context():
#     db.create_all()

# @app.route('/grade_essay', methods=['POST'])
# def grade_essay():
#     essay = request.json.get('essay', '').strip()
    
#     if not essay:
#         return jsonify({"error": "Essay cannot be empty"}), 400

#     # Step 1: Process locally (without saving yet)
#     MIN_WORDS = 50
#     MAX_WORDS = 500
#     word_count = len(essay.split())
#     score = max(1, min(10, round(1 + 9 * (word_count - MIN_WORDS) / (MAX_WORDS - MIN_WORDS))))
    
#     # Step 2: Predict feedback
#     feedback = get_feedback(essay)

#     # Step 3: Return results to user
#     response = {
#         "score": score,
#         "feedback": feedback
#     }

#     # Step 4: Save to DB *after* processing (optional/local control)
#     try:
#         submission = EssaySubmission(
#             essay_text=essay,
#             score=score,
#             feedback=feedback
#             # Timeout = 100000
#         )
#         db.session.add(submission)
#         db.session.commit()
#     except Exception as e:
#         print("Error saving to DB:", e)

#     return jsonify(response)

# if __name__ == '__main__':
#     app.run(debug=True)



#  withoud data based data stor in local data based 
from flask import Flask, request, jsonify
from flask_cors import CORS
from feedback_predictor import get_feedback 

app = Flask(__name__)
CORS(app)

@app.route('/grade_essay', methods=['POST'])
def grade_essay():
    essay = request.json.get('essay', '').strip()
    
    if not essay:
        return jsonify({"error": "Essay cannot be empty"}), 400

    # Word counting  logic
    MIN_WORDS = 50
    MAX_WORDS = 500
    word_count = len(essay.split())
    score = max(1, min(10, round(1 + 9 * (word_count - MIN_WORDS) / (MAX_WORDS - MIN_WORDS))))

    # Get feedback using ML model
    feedback = get_feedback(essay)

    return jsonify({"score": score, "feedback": feedback})

if __name__ == '__main__':
    app.run(debug=True)


















# sample code for practis 








# from flask import Flask, request, jsonify
# from flask_cors import CORS

# app = Flask(__name__)
# CORS(app)  # Enable CORS

# @app.route('/grade_essay', methods=['POST'])
# def grade_essay():
#     essay = request.json.get('essay', '').strip()
    
#     if not essay:
#         return jsonify({"error": "Essay cannot be empty"}), 400

#     # Define word count limits for normalization
#     MIN_WORDS = 50   # Minimum words for 1/10
#     MAX_WORDS = 500  # Maximum words for 10/10

#     # Calculate score (scaled between 1 and 10)
#     word_count = len(essay.split())
#     score = max(1, min(10, round(1 + 9 * (word_count - MIN_WORDS) / (MAX_WORDS - MIN_WORDS))))

#     # Provide simple feedback
#     if score == 8:
#         feedback = "Excellent. improve you structure and your grammer is very good "
#     elif score >8:
#         feedback = "exelent work you did ."
#     elif score >=7:
#         feedback = "Good job! Improve grammar and structure for better clarity."
    
#     elif score >= 5:
#         feedback = "Good job! Improve grammar and structure for better clarity."
#     else:
#         feedback = "Needs improvement. Work on grammar, sentence structure, and content."

    
#     return jsonify({"score": score, "feedback": feedback})

# if __name__ == '__main__':
#     app.run(debug=True)




#  actual working prototype

# from flask import Flask, request, jsonify
# from flask_cors import CORS
# from feedback_predictor import get_feedback  # our feedback function or modul

# app = Flask(__name__)
# CORS(app)

# @app.route('/grade_essay', methods=['POST'])
# def grade_essay():
#     essay = request.json.get('essay', '').strip()
    
#     if not essay:
#         return jsonify({"error": "Essay cannot be empty"}), 400

#     # Word count logic
#     MIN_WORDS = 50
#     MAX_WORDS = 500
#     word_count = len(essay.split())
#     score = max(1, min(10, round(1 + 9 * (word_count - MIN_WORDS) / (MAX_WORDS - MIN_WORDS))))

#     # feedback using ML model
#     feedback = get_feedback(essay)

#     return jsonify({"score": score, "feedback": feedback})

# if __name__ == '__main__':
#     app.run(debug=True)






# # .\venv\Scripts\Activate.ps1






# from flask import Flask, request, jsonify
# from flask_cors import CORS
# # import spacy
# from textblob import TextBlob
# # import textsta

# # Load spaCy model
# # nlp = spacy.load("en_core_web_sm")

# # Initialize Flask app
# app = Flask(__name__)
# CORS(app)

# @app.route('/grade_essay', methods=['POST'])
# def grade_essay():
#     data = request.json
#     essay = data.get('essay', '').strip()

#     if not essay:
#         return jsonify({"error": "Essay cannot be empty"}), 400

#     # **1️⃣ Word Count Scoring (1-10)
#     word_count = len(essay.split())
#     word_score = max(1, min(10, word_count // 50))  # 50 words → 1 point, 500+ words → 10 points

#     # **2️⃣ Grammar & Spelling Score (1-10)
#     blob = TextBlob(essay)
#     corrected_text = blob.correct()
#     mistakes = sum(1 for orig, corr in zip(essay.split(), corrected_text.split()) if orig != corr)
#     grammar_score = max(1, 10 - mistakes)  # More mistakes → lower score

#     # **3️⃣ Final Score (1-10)
#     final_score = round((word_score + grammar_score) / 2)

#     # **4️⃣ Generate Feedback
#     if final_score >= 8:
#         feedback = "Excellent! Your essay is well-written with minimal errors."
#     elif final_score >= 5:
#         feedback = "Good job! Improve grammar and structure for better clarity."
#     else:
#         feedback = "Needs improvement. Work on grammar, sentence structure, and content."

#     return jsonify({"score": final_score, "feedback": feedback})

# if __name__ == '__main__':
#     app.run(debug=True)









# from flask import Flask, request, jsonify # type: ignore
# from flask_cors import CORS # type: ignore
# from flask_sqlalchemy import SQLAlchemy # type: ignore

# app = Flask(__name__)
# CORS(app)  # Enable CORS

# # SQLite Database Configration 
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///essays.db"
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# db = SQLAlchemy(app)

# # Essay Model
# class Essay(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     content = db.Column(db.Text, nullable=False)

# # Create the database
# with app.app_context():
#     db.create_all()

# # ✅ Grade and Save Essay
# @app.route('/grade_essay', methods=['POST'])
# def grade_essay():
#     essay = request.json.get('essay', '').strip()
    
#     if not essay:
#         return jsonify({"error": "Essay cannot be empty"}), 400

#     # Define word count limits for normalization
#     MIN_WORDS = 50   # Minimum words for 1/10
#     MAX_WORDS = 500  # Maximum words for 10/10

#     # Calculate score (scaled between 1 and 10)
#     word_count = len(essay.split())
#     score = max(1, min(10, round(1 + 9 * (word_count - MIN_WORDS) / (MAX_WORDS - MIN_WORDS)) ))

#     # Provide simple feedback
#     feedback = "Good job! Try improving your grammar and structure."

#     #  Save the essay in the database
#     new_essay = Essay(content=essay)
#     db.session.add(new_essay)
#     db.session.commit()

#     return jsonify({"score": score, "feedback": feedback})

# #  Get History (All Essays)
# @app.route("/get_essays", methods=["GET"])
# def get_essays():
#     essays = Essay.query.order_by(Essay.id.desc()).all()  # Latest first
#     return jsonify([{"id": e.id, "content": e.content} for e in essays])

# if __name__ == '__main__':
#     app.run(debug=True)



