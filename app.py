from flask import Flask, request, render_template
import pickle
import pandas as pd

# Load the trained model
model_path = 'placement_model.pkl'
with open(model_path, 'rb') as file:
    model = pickle.load(file)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extract and map form data to correct features
        data = pd.DataFrame([{
            'iq': float(request.form['IQ']),
            'cgpa': float(request.form['CGPA']),
            '10th_marks': float(request.form['10th_Marks']),
            '12th_marks': float(request.form['12th_Marks']),
            'communication_skills': float(request.form['Communication_Skills'])
        }])

        # Make prediction
        prediction = model.predict(data)[0]
        output = '✅ PLACED' if prediction == 1 or prediction == 'Yes' else '❌ NOT PLACED'

        return render_template('index.html', prediction_text=f"Prediction: {output}")
    
    except Exception as e:
        return render_template('index.html', prediction_text=f"Error: {str(e)}")

if __name__ == "__main__":
    app.run(debug=True)
