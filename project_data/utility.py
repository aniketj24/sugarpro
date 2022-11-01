import pickle
import json
import numpy as np

import config

class Diabetes():
    def __init__(self, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age):
        self.Glucose = Glucose
        self.BloodPressure = BloodPressure
        self.SkinThickness = SkinThickness
        self.Insulin = Insulin
        self.BMI = BMI
        self.DiabetesPedigreeFunction = DiabetesPedigreeFunction
        self.Age = Age

    def Loadmodel(self):
        with open (config.MODEL_FILE_PATH, "rb") as f:
            self.lg_model = pickle.load(f)

        with open (config.JSON_FILE_PATH, "r") as f:
            self.json_data = json.load(f)

    def Result(self):
        self.Loadmodel()

        test_array = np.zeros(len(self.json_data["columns"]))

        test_array[0] = self.Glucose
        test_array[1] = self.BloodPressure
        test_array[2] = self.SkinThickness
        test_array[3] = self.Insulin
        test_array[4] = self.BMI
        test_array[5] = self.DiabetesPedigreeFunction
        test_array[6] = self.Age

        print("Predicting result for values: ", test_array)

        pred_result = self.lg_model.predict([test_array])
        print("Result is :", pred_result)

        return pred_result


if "__name__" == "main":

    Glucose = 145
    BloodPressure = 80
    SkinThickness = 46
    Insulin = 130
    BMI = 37.9
    DiabetesPedigreeFunction = 0.637
    Age = 40

    report = Diabetes(Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age)
    report.Result()


