from flask import Flask
from flask import render_template
from database import get_all_cats

app = Flask(__name__)
app.config['SECRET_KEY'] = 'YOUR-VERY-SECRET-SHHH'

@app.route('/')
def catbook_home():
    cats = get_all_cats()
    return render_template("home.html", cats=cats)

@app.route('/cats/<string:cat_view>', methods = ['GET'])
def catbook(cat_view):
    cats = get_all_cats()
    # cat = get_cat(id)
    return render_template("cat.html", cats=cats)
if __name__ == '__main__':
   app.run(debug = True)
