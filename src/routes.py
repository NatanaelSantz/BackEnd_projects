from flask import Flask
app = Flask(__name__)

@app.route('/database')
def database_list():
 pass

@app.route('/home')
def home_page():
 pass