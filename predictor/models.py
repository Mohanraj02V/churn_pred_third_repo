from django.db import models

class PredictionRecord(models.Model):
    # Store all possible input fields (adjust according to your actual model)
    customerID = models.CharField(max_length=100, blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    SeniorCitizen = models.IntegerField(blank=True, null=True)
    Partner = models.CharField(max_length=10, blank=True, null=True)
    Dependents = models.CharField(max_length=10, blank=True, null=True)
    tenure = models.IntegerField(blank=True, null=True)
    PhoneService = models.CharField(max_length=10, blank=True, null=True)
    MultipleLines = models.CharField(max_length=50, blank=True, null=True)
    InternetService = models.CharField(max_length=50, blank=True, null=True)
    OnlineSecurity = models.CharField(max_length=50, blank=True, null=True)
    OnlineBackup = models.CharField(max_length=50, blank=True, null=True)
    DeviceProtection = models.CharField(max_length=50, blank=True, null=True)
    TechSupport = models.CharField(max_length=50, blank=True, null=True)
    StreamingTV = models.CharField(max_length=50, blank=True, null=True)
    StreamingMovies = models.CharField(max_length=50, blank=True, null=True)
    Contract = models.CharField(max_length=50, blank=True, null=True)
    PaperlessBilling = models.CharField(max_length=10, blank=True, null=True)
    PaymentMethod = models.CharField(max_length=50, blank=True, null=True)
    MonthlyCharges = models.FloatField(blank=True, null=True)
    TotalCharges = models.FloatField(blank=True, null=True)
    
    # Prediction results
    prediction = models.CharField(max_length=3)  # 'Yes' or 'No'
    probability = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Prediction for {self.customerID or 'anonymous'} - {self.prediction} ({self.probability:.2%})"