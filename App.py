# from flask import Flask, render_template, request
# import joblib
# import numpy as np

# app = Flask(__name__)
# model = joblib.load('model1.pkl')

# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/predict', methods=['POST'])
# def predict():
#     if request.method == 'POST':
#         # Get all 11 input features from the form
#         input_features = [float(request.form[f]) for f in [
#             'age', 'anaemia', 'creatinine_phosphokinase', 'diabetes', 
#             'ejection_fraction', 'high_blood_pressure', 'platelets', 
#             'serum_creatinine', 'serum_sodium', 'sex', 'smoking','time'
#         ]]
        
#         input_array = np.array([input_features])
#         prediction = model.predict(input_array)[0]

#         result = "⚠️ Patient is likely to DIE due to heart failure." if prediction == 1 else "✅ Patient is NOT likely to die (Low Risk)."
#         return render_template('index.html', prediction_text=result)

# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load('model1.pkl')  # Your trained model

@app.route('/', methods=['GET', 'POST'])
def predict():
    prediction_message = None

    if request.method == 'POST':
        try:
            input_features = [float(request.form[f]) for f in [
                'age', 'anaemia', 'creatinine_phosphokinase', 'diabetes',
                'ejection_fraction', 'high_blood_pressure', 'platelets',
                'serum_creatinine', 'serum_sodium', 'sex', 'smoking', 'time'
            ]]

            input_array = np.array([input_features])
            prediction = model.predict(input_array)[0]

            # Prediction message
            prediction_message = (
                "❌ Patient is likely to DIE due to heart failure."
                if prediction == 1
                else "✅ Patient is NOT likely to die (Low Risk)."
            )

        except Exception as e:
            prediction_message = f"⚠️ Error: {str(e)}"

    return render_template('index.html', prediction_message=prediction_message)

if __name__ == '__main__':
    app.run(debug=False)
