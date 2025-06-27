from rest_framework import serializers
from .models import PredictionRecord

class PredictionInputSerializer(serializers.Serializer):
    # Define all possible input fields (adjust according to your actual model)
    customerID = serializers.CharField(required=False, allow_null=True)
    gender = serializers.CharField(required=False, allow_null=True)
    SeniorCitizen = serializers.IntegerField(required=False, allow_null=True)
    Partner = serializers.CharField(required=False, allow_null=True)
    Dependents = serializers.CharField(required=False, allow_null=True)
    tenure = serializers.IntegerField(required=False, allow_null=True)
    PhoneService = serializers.CharField(required=False, allow_null=True)
    MultipleLines = serializers.CharField(required=False, allow_null=True)
    InternetService = serializers.CharField(required=False, allow_null=True)
    OnlineSecurity = serializers.CharField(required=False, allow_null=True)
    OnlineBackup = serializers.CharField(required=False, allow_null=True)
    DeviceProtection = serializers.CharField(required=False, allow_null=True)
    TechSupport = serializers.CharField(required=False, allow_null=True)
    StreamingTV = serializers.CharField(required=False, allow_null=True)
    StreamingMovies = serializers.CharField(required=False, allow_null=True)
    Contract = serializers.CharField(required=False, allow_null=True)
    PaperlessBilling = serializers.CharField(required=False, allow_null=True)
    PaymentMethod = serializers.CharField(required=False, allow_null=True)
    MonthlyCharges = serializers.FloatField(required=False, allow_null=True)
    TotalCharges = serializers.FloatField(required=False, allow_null=True)

class PredictionRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = PredictionRecord
        fields = '__all__'