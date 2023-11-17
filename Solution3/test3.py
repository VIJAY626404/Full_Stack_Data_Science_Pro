# 3.Develop a Flask app that uses URL parameters to display dynamic content
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index3.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    if request.method == 'POST':
        try:
            expression = request.form['expression']
            result = eval(expression)
            return render_template('index3.html', result=result, expression=expression)
        except Exception as e:
            error_message = f"Error: {str(e)}"
            return render_template('index3.html', error_message=error_message)

if __name__ == '__main__':
    app.run(host ='0.0.0.0',port = 4004)
