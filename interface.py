from flask import Flask , request, render_template
from project_data import utility
import config

app = Flask(__name__)

@app.route("/")
def Home():

    return render_template("User_input.html")

@app.route("/Result", methods = ["POST", "GET"])
def Result():
    if request.method == "POST":
        data = request.form
        Glucose = data["Glucose"]
        BloodPressure = data["BloodPressure"]
        SkinThickness = data["SkinThickness"]
        Insulin = data["Insulin"]
        BMI = data["BMI"]
        DiabetesPedigreeFunction = data["DiabetesPedigreeFunction"]
        Age = data["Age"]


    report_find = utility.Diabetes(Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age)
    predicted_result = report_find.Result()


    return  render_template("User_input.html",prediction = predicted_result)


if __name__ == "__main__":
    app.run(host = "0.0.0.0",port = config.PORT_NUMBER,debug = True)
