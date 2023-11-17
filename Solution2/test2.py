# 2. Build a Flask app with static HTML pages and navigate between them.
from flask import Flask,request,jsonify,render_template
app = Flask(__name__)

@app.route("/")
def html_page():
    return render_template('index2.html')

@app.route("/process_form",methods = ['POST'])
def display_message():
    username = request.form.get('username')
    password = request.form.get('password')
    return f"Successfully received username and password"

if __name__ == "__main__":
    app.run(host ="0.0.0.0",port = 8002)