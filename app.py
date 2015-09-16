from flask import Flask, render_template, redirect, jsonify


app = Flask(__name__)

@app.route('/')
def homepage():
    title = 'Saluton, Mondo!'
    return render_template('index.html', title=title)

@app.route('/page/<page_id>')
def page(page_id):
    page = Page.objects(pk=page_id)
    return render_template('page.html', page=page)

if __name__ == '__main__':
    app.run(debug=True)
