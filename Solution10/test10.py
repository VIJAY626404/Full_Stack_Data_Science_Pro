#  10 Design a Flask app with proper error handling for 404 and 500 errors
from flask import Flask, render_template

app = Flask(__name__)

# Route for a sample page
@app.route('/')
def home():
    return render_template('index10.html')

# Custom 404 error handler
@app.errorhandler(404)
def not_found_error(error):
    return render_template('index_404.html'), 404

# Custom 500 error handler
@app.errorhandler(500)
def internal_server_error(error):
    return render_template('index_500.html'), 500

if __name__ == '__main__':
    app.run(debug=True)
