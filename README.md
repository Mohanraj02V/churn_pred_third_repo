# 🔁 Churn Prediction API
  This project provides a RESTful API for predicting telecom customer churn using a machine learning model built with scikit-learn. 
  The backend is powered by Django REST Framework and deployed on Render.
# 🌐 Deployment Notice
  1. This project is hosted on Render's free tier, which does not support persistent data storage.
  2. The app uses SQLite, which resets when the server restarts or goes to sleep.
  3. Unlike PostgreSQL, data will be lost after inactivity.
  4. When the web service is inactive, the first request after waking may take 1–2 minutes to respond. Please be patient.
# 🚀 API Endpoints
🔍 1. Predict Churn
      URL: POST https://churn-pred-third-repo-2.onrender.com/api/predict/
      
      Request Body (JSON):
      
        {
        "gender": "Female",
        "SeniorCitizen": 0,
        "Partner": "Yes",
        "Dependents": "No",
        "tenure": 5,
        "PhoneService": "Yes",
        "MultipleLines": "No",
        "InternetService": "Fiber optic",
        "OnlineSecurity": "No",
        "OnlineBackup": "Yes",
        "DeviceProtection": "Yes",
        "TechSupport": "No",
        "StreamingTV": "No",
        "StreamingMovies": "Yes",
        "Contract": "Month-to-month",
        "PaperlessBilling": "Yes",
        "PaymentMethod": "Electronic check",
        "MonthlyCharges": 80.35,
        "TotalCharges": 401.75
      }
      Response:
      {
        "prediction": "Yes",
        "probability": 0.7490594387054443,
        "created_at": "2025-07-14T07:43:46.287349Z"
      }
      
      📜 2. View Prediction History
      
            URL: GET https://churn-pred-third-repo-2.onrender.com/api/history/
      
            Response Example:
            {
            "id": 1,
            "customerID": null,
            "gender": "Female",
            "SeniorCitizen": 0,
            "Partner": "Yes",
            "Dependents": "No",
            "tenure": 5,
            "PhoneService": "Yes",
            "MultipleLines": "No",
            "InternetService": "Fiber optic",
            "OnlineSecurity": "No",
            "OnlineBackup": "Yes",
            "DeviceProtection": "Yes",
            "TechSupport": "No",
            "StreamingTV": "No",
            "StreamingMovies": "Yes",
            "Contract": "Month-to-month",
            "PaperlessBilling": "Yes",
            "PaymentMethod": "Electronic check",
            "MonthlyCharges": 80.35,
            "TotalCharges": 401.75,
            "prediction": "Yes",
            "probability": 0.7490594387054443,
            "created_at": "2025-07-14T07:43:46.287349Z"
          }

    
# 🛠 Tech Stack
  Backend: Django, Django REST Framework
  Machine Learning: scikit-learn, XGBoost
  Database: SQLite (due to free tier limitations on Render)
  Deployment: Render
