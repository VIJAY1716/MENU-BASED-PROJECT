from flask import Flask, request, render_template
import joblib
import numpy as np

app = Flask(__name__)

# Load model and label encoders
model = joblib.load('model.pkl')
label_encoders = joblib.load('label_encoders.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    age = float(request.form['age'])
    department = request.form['department']

    # Encode department
    department_encoded = label_encoders['Department'].transform([department])[0]

    # Prepare features
    features = np.array([[age, department_encoded]])

    # Make prediction
    prediction = model.predict(features)[0]

    return render_template('index.html', prediction_text=f'Predicted Salary: ${prediction:.2f}')

if __name__ == "__main__":
    app.run(debug=True)
