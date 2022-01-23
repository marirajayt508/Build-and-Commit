from flask import Flask,render_template
from os import system
app = Flask(__name__)

@app.route('/')
def index():
   return render_template("index.html")

@app.route('/build')
def build():
   system("cd..'")
   system("git add *")
   system("dir")
   system("git commit -m 'Commited'")
   return "Build Started"

if __name__ == '__main__':
   app.run(debug = True)