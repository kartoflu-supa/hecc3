from flask import Flask, render_template

app = Flask(__name__)

vorur = {1:{"nafn":"Buxur","verd":"1500","mynd":"N/A"},2:{"nafn":"Hettupeysa","verd":"3000","mynd":"N/A"},3:{"nafn":"Sokkar","verd":"1000","mynd":"N/A"},
4:{"nafn":"Brækur","verd":"1000","mynd":"N/A"},5:{"nafn":"Stutt erma bolur","verd":"2000","mynd":"N/A"},6:{"nafn":"Vinnagull","verd":"5000","mynd":"N/A"}}

karfa = []

@app.errorhandler(404)
def error404(error):
    return render_template("error.html"),404

@app.route("/")
def index():
    return render_template("index.html", vorur = vorur, karfa = karfa)