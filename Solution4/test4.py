# 4. Create a Flask app with a form that accepts user input and displays it.
from flask import Flask,request,render_template
app = Flask(__name__)

@app.route('/')
def show_form():
    return render_template('index4.html')

@app.route('/userForm',methods = ['POST'])
def show_message():
    firstname = request.form.get('firstname')
    lastname = request.form.get('lastname')
    print("Congratualation!, First name and Last name received")
if __name__ == '__main__':
    app.run(host ='0.0.0.0',port = 4000)