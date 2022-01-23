from flask import Flask,render_template
from os import system
app = Flask(__name__)

@app.route('/')
def index():
   return render_template("index.html")

@app.route('/build')
def build():
   system("cd Projects")
   system("git init")
   system("git add *")
   system("git commit -m 'Commited'")
   system("git remote add origin https://github.com/marirajayt508/Test-Commit.git")
   system("git branch -M main")
   system("git push -u origin main")
   return "Build Started"

if __name__ == '__main__':
   app.run(debug = True)