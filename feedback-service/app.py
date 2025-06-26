from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:pass@db:5432/feedback_db'
db = SQLAlchemy(app)

class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    rating = db.Column(db.Integer)
    comment = db.Column(db.String(255))

@app.route('/submit', methods=['POST'])
def submit_feedback():
    data = request.json
    feedback = Feedback(name=data['name'], rating=data['rating'], comment=data['comment'])
    db.session.add(feedback)
    db.session.commit()
    return jsonify({"message": "Feedback submitted"}), 200

@app.route('/all', methods=['GET'])
def get_feedback():
    feedbacks = Feedback.query.all()
    return jsonify([{ "name": f.name, "rating": f.rating, "comment": f.comment } for f in feedbacks])

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5000)
