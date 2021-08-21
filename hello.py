from flask import Flask, render_template

# this is to start a flask project
app = Flask(__name__)

# create a route a decorator .html (home page)
@app.route('/')

#def index():
 #   return "<h1>Hello World!</h1>"

#FILTERS
#safe
#capitalize
#lower
#upper
#title
#trim
#striptags

def index():
    first_name = 'Mansur'
    stuff = "This is <strong>Bold</strong> Text"
    stuff2 = "another bold text"
    favorite_pizza = ['funghi','olive','mozzarella',41]
    return render_template("index.html",
                           first_name=first_name,
                           stuff=stuff,
                           stuff2=stuff2,
                           favorite_pizza=favorite_pizza)


#localhost:5000/user/Mansur
@app.route('/user/<name>')

#def user(name):
 #   return "<h1>Hello {}!!!</h1>".format(name)

def user(name):
    return render_template("user.html", user_name=name)

#CREATE A CUSTOM ERROR PAGE

# INVALID URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

# INTERNAL SERVER ERROR
@app.errorhandler(500)
def page_not_found(e):
    return render_template("(500.html"), 500

