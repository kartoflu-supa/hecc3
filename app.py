from flask import Flask, render_template

app = Flask(__name__)

vorur = [{"nafn":"Buxur","verd":"1500","mynd":"N/A"},{"nafn":"Hettupeysa","verd":"3000","mynd":"N/A"},{"nafn":"Sokkar","verd":"1000","mynd":"N/A"},
{"nafn":"Brækur","verd":"1000","mynd":"N/A"},{"nafn":"Stutt erma bolur","verd":"2000","mynd":"N/A"},{"nafn":"Vinnagull","verd":"5000","mynd":"N/A"}]

karfa = []

@app.errorhandler(404)
def error404(error):
    return render_template("error.html"),404

@app.route("/")
def index():
    return render_template("index.html", listi = vorur, karfa = karfa)

@app.route("/kaupa/<nafn>")
def kaupa(nafn):
    for x in vorur:
        if x['nafn'] == nafn:
            karfa.append(x)
    return render_template("index.html", listi = vorur, karfa = karfa)

@app.route("/taema")
def taema():
    karfa = []
    return render_template("index.html", listi = vorur, karfa = karfa)