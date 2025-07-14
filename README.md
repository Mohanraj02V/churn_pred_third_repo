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
input field explaination
{
  1. "gender": "Female",                     // ['Male', 'Female'] – Customer’s gender
  2. "SeniorCitizen": 0,                    // [0 or 1] – 1 if senior citizen, 0 otherwise
  3. "Partner": "Yes",                      // ['Yes', 'No'] – Whether the customer has a partner
  4. "Dependents": "No",                    // ['Yes', 'No'] – Whether the customer has dependents
  5. "tenure": 5,                           // Integer – Number of months the customer has stayed
  6. "PhoneService": "Yes",                 // ['Yes', 'No'] – Does the customer have phone service
  7. "MultipleLines": "No",                 // ['Yes', 'No', 'No phone service'] – Has multiple phone lines
  8. "InternetService": "Fiber optic",      // ['DSL', 'Fiber optic', 'No'] – Type of internet service
  9. "OnlineSecurity": "No",                // ['Yes', 'No', 'No internet service'] – Has online security
  10. "OnlineBackup": "Yes",                // ['Yes', 'No', 'No internet service'] – Has online backup
  11. "DeviceProtection": "Yes",            // ['Yes', 'No', 'No internet service'] – Has device protection
  12. "TechSupport": "No",                  // ['Yes', 'No', 'No internet service'] – Has tech support
  13. "StreamingTV": "No",                  // ['Yes', 'No', 'No internet service'] – Streams TV
  14. "StreamingMovies": "Yes",             // ['Yes', 'No', 'No internet service'] – Streams movies
  15. "Contract": "Month-to-month",         // ['Month-to-month', 'One year', 'Two year'] – Contract type
  16. "PaperlessBilling": "Yes",            // ['Yes', 'No'] – Uses paperless billing
  17. "PaymentMethod": "Electronic check",  // ['Electronic check', 'Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)']
  18. "MonthlyCharges": 80.35,              // Float – Monthly amount charged
  19. "TotalCharges": 401.75                // Float – Total amount charged to date
}


    
# 🛠 Tech Stack
  Backend: Django, Django REST Framework
  Machine Learning: scikit-learn, XGBoost
  Database: SQLite (due to free tier limitations on Render)
  Deployment: Render
