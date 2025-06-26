from flask import Flask, render_template, request
import requests

app = Flask(__name__)

BACKEND_URL = "http://backend:5000/submit"

@app.route('/')
def home():
    return render_template('feedback.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = {
        "name": request.form['name'],
        "rating": request.form['rating'],
        "comment": request.form['comment']
    }
    response = requests.post(BACKEND_URL, json=data)
    return "Submitted successfully!" if response.status_code == 200 else "Submission failed"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)
