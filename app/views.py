from flask import render_template
from app import app

@app.route('/')
def home():
    return "I love You Edna!!"

@app.route('/template')
def template():
    return render_template('home.html')





