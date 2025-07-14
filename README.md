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
# Field Explaination
  🧾 Input Fields Explanation
  {
    "gender": "Female",             // Customer’s gender
    "SeniorCitizen": 0,            // 1 if customer is a senior citizen, 0 otherwise
    "Partner": "Yes",             // Whether the customer has a partner
    "Dependents": "No",          // Whether the customer has dependents
    "tenure": 5,                // Number of months the customer has stayed with the company
    "PhoneService": "Yes",     // Whether the customer has phone service
    "MultipleLines": "No",    // Whether the customer has multiple phone lines
    "InternetService": "Fiber optic", // Type of internet service: DSL, Fiber optic, or No
    "OnlineSecurity": "No",  // Whether the customer has online security add-on
    "OnlineBackup": "Yes", // Whether the customer has online backup service
    "DeviceProtection": "Yes", // Whether the customer has device protection
    "TechSupport": "No", // Whether the customer has tech support service
    "StreamingTV": "No", // Whether the customer streams TV
    "StreamingMovies": "Yes", // Whether the customer streams movies
    "Contract": "Month-to-month", // Type of contract: Month-to-month, One year, or Two year
    "PaperlessBilling": "Yes", // 	Whether the customer uses paperless billing
    "PaymentMethod": "Electronic check", // 	Method of payment: Electronic check, Mailed check, Bank transfer, Credit card
    "MonthlyCharges": 80.35, // Monthly amount charged to the customer
    "TotalCharges": 401.75 // Total amount charged to the customer to date
  }

    
# 🛠 Tech Stack
  Backend: Django, Django REST Framework
  Machine Learning: scikit-learn, XGBoost
  Database: SQLite (due to free tier limitations on Render)
  Deployment: Render
