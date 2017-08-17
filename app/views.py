from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm

@app.route('/')
#@app.route('/index')
#def login():
#    return render_template('login.html',title='Home')
@app.route('/index')
#@app.route('/create')
def create():
	return render_template('create.html', title='Register new User')

@app.route('/shopping_list')
def shopping_list():
	return render_template('shopping_list.html', title='shopping lists')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
