from flask import Flask, render_template, redirect, jsonify


app = Flask(__name__)

@app.route('/')
def homepage():
    title = 'Saluton, Mondo!'
    return render_template('index.html', title=title)

