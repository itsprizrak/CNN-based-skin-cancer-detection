from flask import Flask,request,render_template
app = Flask(__name__)
from projecttest1 import detect
import json


with open("types.json", "r") as read_file:
    data = json.load(read_file)

@app.route("/detectCancer",methods=['POST'])
def detectCancer():
    try:
        f_name = request.files['file']
        category = detect(f_name)
        return "<h1>Cancer Category: </h1><h3>"+data[category]["name"] + "</h3><br>" + "<h1>Description: </h1>" + "<h3>"+data[category]["description"]+"</h3>"
    except:
        return str("File Not Found!")

@app.route('/', methods =["GET"])
def defaultroute():
    
    return render_template("SkinCancer.html")

if __name__ == "__main__":
    app.run(debug=True)

