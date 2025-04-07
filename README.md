
📚 Student Placement Prediction 🎓
This project uses Machine Learning to predict whether a student is likely to be placed or not based on academic and soft skill attributes. The model is deployed using Flask and provides a simple web interface for input and result display.

🚀 Features
Predict student placement outcome using:

IQ

CGPA

10th Marks

12th Marks

Communication Skills

Trained with Random Forest Classifier

Hyperparameter tuning with GridSearchCV

Flask web app for interactive prediction

Deployment-ready structure

📂 Project Structure
bash
Copy
Edit
stu_placement_prediction/
├── app.py                  # Flask backend
├── placement_model.pkl     # Trained ML model
├── requirements.txt        # Dependencies
└── templates/
    └── index.html          # HTML form for user input
🧠 Model Details
Algorithm: Random Forest Classifier

Techniques Used: Data Cleaning, Feature Engineering, Grid Search

Evaluation Metrics: Accuracy, Classification Report

💻 How to Run Locally
Clone the repository:

bash
Copy
Edit
git clone https://github.com/your-username/student-placement-prediction.git
cd student-placement-prediction
Create and activate a virtual environment:

bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Run the app:

bash
Copy
Edit
python app.py
Open your browser:

cpp
Copy
Edit
http://127.0.0.1:5000
🌐 Demo
If you’ve deployed the project (e.g. on Render, Heroku, etc.), you can link it here:

👉 Live Demo

🛠 Technologies Used
Python

Pandas & NumPy

Scikit-learn

Flask

HTML/CSS

📌 Future Enhancements
Add more features like internship experience, projects, certifications

Add user authentication

Track and log user input and predictions

🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to change.

📄 License
This project is open source and free to use under the MIT License.

