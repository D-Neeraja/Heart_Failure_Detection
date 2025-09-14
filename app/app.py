import pickle
from flask import Flask, render_template, request

app = Flask(__name__)

model = pickle.load(open("/home/neeeraja/Documents/self_learning/data science/practice/classification/ml_model.pkl", "rb"))

@app.route("/", methods=["GET", "POST"])
def heart_failure_predictor():
    prediction_message = None

    if request.method == "POST":
        try:
            # Fetch form data with fallback default values
            age = request.form.get("age", "0")
            cpk = request.form.get("creatinine_phosphokinase", "0")
            ef = request.form.get("ejection_fraction", "0")
            sc = request.form.get("serum_creatinine", "0")
            sex = request.form.get("gender", "0")
            time = request.form.get("time", "0")

            # Convert inputs and make prediction
            input_features = [[float(age), float(cpk), float(ef), float(sc), int(sex), float(time)]]
            prediction = model.predict(input_features)[0]

            if prediction == 1:
                prediction_message = "There may be a potential risk of heart failure (86% accuracy). Please consult a medical professional."
            else:
                prediction_message = "The risk of heart failure appears low (86% accuracy). Maintain a healthy lifestyle."
        
        except ValueError:
            prediction_message = "Invalid input detected. Please provide valid numeric values."

    return render_template("index.html", prediction=prediction_message)

if __name__ == "__main__":
    app.run(debug=True)
