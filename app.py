from flask import Flask
from flask import render_template
from database import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'YOUR-VERY-SECRET-SHHH'

@app.route('/')
def catbook_home():
    cats = get_all_cats()
    return render_template("home.html", cats=cats)

@app.route('/cats/<int:cat_view>', methods = ['GET', 'POST'])
def catbook(cat_view):
    if request.method == 'GET':
        return render_template("cat.html", cat= get_cat_by_id(cat_view))
    else :
        cat_vote(cat_view)
        return Redirect('/')
if __name__ == '__main__':
   app.run(debug = True)