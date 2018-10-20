from flask import Flask, render_template
from random import randint
app = Flask(__name__)

@app.route("/")
def one():
    return "<h1>Hello World!</h1>"

@app.route("/something")
def two():
    return "something"

@app.route("/alpha/<string:name>/")
def three(name):
    return render_template(
            'test1.html', name=name, greeting="Good Morning")

@app.route("/beta/<string:name>/")
def four(name):
    return render_template(
            'test2.html', name=name)

@app.route("/charlie")
def five():
    quotes = [ "'If people do not believe that mathematics is simple, it is only because they do not realize how complicated life is.' -- John Louis von Neumann ",
               "'Computer science is no more about computers than astronomy is about telescopes' --  Edsger Dijkstra ",
               "'To understand recursion you must first understand recursion..' -- Unknown",
               "'You look at things that are and ask, why? I dream of things that never were and ask, why not?' -- Unknown",
               "'Mathematics is the key and door to the sciences.' -- Galileo Galilei",
               "'Not everyone will understand your journey. Thats fine. Its not their journey to make sense of. Its yours.' -- Unknown"  ]
    names = ["Alfred","Bob", "Charles", "Daniel", "Elias", "Francis"];
    randomNumber = randint(0,len(quotes)-1)
    quote = quotes[randomNumber]
    randomNumber = randint(0,5)
    name = names[randomNumber]

    return render_template(
        'test3.html',**locals())

if __name__ == "__main__":
    app.run()
