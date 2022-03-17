from flask import Flask
from flask import render_template, request
import pandas as pd

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")
    
@app.route("/data", methods=["GET", "POST"])
def data():
    if request.method == "POST":
        file = request.form["upload-file"]
        data = pd.read_excel(file)
        return render_template("data.html", data=data)  

if __name__ == "__main__":
    app.run(debug=True)    