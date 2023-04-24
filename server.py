from flask import Flask, render_template, url_for, redirect
from cupcakes import get_cupcakes, find_cupcake, add_cupcake_dictionary, add_individual_cupcake_dictionary
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", cupcakes = get_cupcakes("cupcakes.csv"))

@app.route("/add-cupcake/<name>")
def add_cupcake(name):
    cupcake = find_cupcake("cupcakes.csv", name)

    if cupcake:
        add_cupcake_dictionary("orders.csv", cupcake)
        return redirect(url_for("home"))
    else:
        return "Sorry cupcake not found."

@app.route("/add-cupcake-individual/<name>")
def add_individual_cupcake(name):
    cupcake = find_cupcake("cupcakes.csv", name)

    if cupcake:
        add_individual_cupcake_dictionary("individual.csv", cupcake)
        return redirect(url_for("individual_cupcake"))
    else:
        return "Sorry cupcake not found."

@app.route('/cupcakes')
def all_cupcakes():
    return render_template('cupcakes.html')

@app.route('/cupcake_individual')
def individual_cupcake():
    return render_template('individual_cupcake.html', individual= get_cupcakes("individual.csv"))

@app.route('/order')
def order():
    return render_template('order.html', order = get_cupcakes("orders.csv"))

if __name__ == '__main__':
    app.env = 'development'
    app.run(debug= True, port= 8000, host='localhost')

