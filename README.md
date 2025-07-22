# 🫀 Heart Failure Risk Predictor

This is a Flask-based web application that predicts the risk of heart failure based on user-provided clinical information. It uses a machine learning model trained on medical data and provides immediate feedback based on the prediction result.

---

## 🚀 Features

- Predicts heart failure risk based on 12 health-related input parameters.
- Built using **Python**, **Flask**, and **HTML/CSS**.
- Easy-to-use web interface.
- Model loaded from `model1.pkl`.
- Provides instant prediction feedback via browser alert.

---

## 🏗️ Tech Stack

- **Frontend**: HTML, CSS
- **Backend**: Python, Flask
- **ML Model**: scikit-learn
- **Deployment Ready**: Can be deployed on Render, Replit, or any WSGI-supported host.

---

## 📸 Screenshot

![Screenshot of Heart Failure Risk Predictor](images/screenshot.png) <!-- Optional if you have a screenshot -->

---

## 📁 Project Structure
heart-failure-predictor/
│
├── app.py # Flask application
├── model1.pkl # Pre-trained ML model
├── templates/
│ └── index.html # Main HTML page
├── static/
│ └── style.css # Styling for the form
│ └── images.png # Background image
├── README.md # This file

---

## 🧪 Input Fields

- Age
- Sex
- Chest Pain Type
- Blood Pressure
- Cholesterol
- Fasting Blood Sugar
- ECG Result
- Max Heart Rate
- Exercise Induced Angina
- Oldpeak (ST depression)
- Slope
- Thal

All fields are required and must be filled accurately for prediction.

---
### Prerequisites

- Python 3.7+
- `pip` installed
### Install dependencies
pip install -r requirements.txt

## 🔧 How to Run Locally
write in terminal:  python app.py 

Open your browser and go to:
http://127.0.0.1:5000/
# After entering input field the output is being predicted like this (pop-up window appears)
![alt text](image.png)
![alt text](image-1.png)
![alt text](image-2.png)
![alt text](image-3.png)

# 📬 Output
If prediction is 0: You are not at risk of heart failure.

If prediction is 1: You are at risk of heart failure. Please consult a doctor.

# 🧠 Credits
Machine Learning Model: Trained on UCI Heart Disease dataset.


# ###################################### 
Built by: Hafsa Sheeraz
Special thanks to: [Sir Lakshya Sachdeva]
# ######################################### 
