# import joblib
# import pandas as pd
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# import os
# import xgboost as xgb  # Import xgboost explicitly
# from .models import PredictionRecord
# from .serializers import PredictionInputSerializer, PredictionRecordSerializer
# import warnings

# # Suppress specific warnings
# warnings.filterwarnings("ignore", category=UserWarning, module="sklearn")
# warnings.filterwarnings("ignore", category=UserWarning, module="xgboost")

# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# MODEL_DIR = os.path.join(BASE_DIR, '../model')

# def safe_load_joblib(path):
#     """Helper function to safely load joblib files with version handling"""
#     try:
#         return joblib.load(path)
#     except Exception as e:
#         warnings.warn(f"Error loading {path}: {str(e)}")
#         raise

# class ModelLoader:
#     """Singleton class to load and cache model artifacts"""
#     _instance = None
    
#     def __new__(cls):
#         if cls._instance is None:
#             cls._instance = super().__new__(cls)
#             cls._instance.load_artifacts()
#         return cls._instance
    
#     def load_artifacts(self):
#         """Load all required model artifacts"""
#         try:
#             # Load XGBoost model using native method if available
#             xgb_model_path = os.path.join(MODEL_DIR, 'xgb_churn_model.json')
#             if os.path.exists(xgb_model_path):
#                 self.model = xgb.Booster()
#                 self.model.load_model(xgb_model_path)
#             else:
#                 self.model = safe_load_joblib(os.path.join(MODEL_DIR, 'xgb_churn_model.pkl'))
            
#             # Load preprocessing artifacts
#             self.scaler = safe_load_joblib(os.path.join(MODEL_DIR, 'scaler.pkl'))
#             self.encoder = safe_load_joblib(os.path.join(MODEL_DIR, 'encoder.pkl'))
#             self.imputer = safe_load_joblib(os.path.join(MODEL_DIR, 'imputer.pkl'))
#             self.numeric_features = safe_load_joblib(os.path.join(MODEL_DIR, 'numeric_features.pkl'))
#             self.categorical_features = safe_load_joblib(os.path.join(MODEL_DIR, 'categorical_features.pkl'))
#             self.encoded_cols = safe_load_joblib(os.path.join(MODEL_DIR, 'encoded_columns.pkl'))
            
#         except Exception as e:
#             raise RuntimeError(f"Failed to load model artifacts: {str(e)}")

# class PredictView(APIView):
#     def __init__(self):
#         super().__init__()
#         self.artifacts = ModelLoader()
    
#     def post(self, request):
#         # Validate input data
#         serializer = PredictionInputSerializer(data=request.data)
#         if not serializer.is_valid():
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
#         # Get the input data
#         single_input = serializer.validated_data
        
#         # Make prediction
#         try:
#             result = self.predict_input(single_input)
#         except Exception as e:
#             return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
#         # Store the prediction
#         prediction_record = PredictionRecord(
#             **single_input,
#             prediction=result[0],
#             probability=result[1]
#         )
#         prediction_record.save()
        
#         # Return the prediction
#         return Response({
#             'prediction': result[0],
#             'probability': result[1],
#             'record_id': prediction_record.id
#         })
    
#     def predict_input(self, single_input):
#         """Process input and make prediction"""
#         input_df = pd.DataFrame([single_input])
#         self.categorical_features = [col for col in self.categorical_features if col not in ['customerID', 'Churn']]
#         # Feature engineering
#         input_df['Avg_Monthly_Charge'] = input_df['TotalCharges'] / (input_df['tenure'] + 1)
        
#         # Preprocessing
#         input_df[self.artifacts.numeric_features] = self.artifacts.imputer.transform(
#             input_df[self.artifacts.numeric_features]
#         )
#         input_df[self.artifacts.numeric_features] = self.artifacts.scaler.transform(
#             input_df[self.artifacts.numeric_features]
#         )
        
#         # Handle categorical encoding
#         encoded_data = self.artifacts.encoder.transform(
#             input_df[self.artifacts.categorical_features]
#         ).toarray()
#         input_df[self.artifacts.encoded_cols] = encoded_data
        
#         # Prepare final features
#         x_inputs = input_df[self.artifacts.numeric_features + self.artifacts.encoded_cols]
        
#         # Convert to DMatrix if using XGBoost native model
#         if isinstance(self.artifacts.model, xgb.Booster):
#             dmatrix = xgb.DMatrix(x_inputs)
#             pred = int(self.artifacts.model.predict(dmatrix)[0] > 0.5)
#             proba = self.artifacts.model.predict(dmatrix)[0]
#         else:
#             # For scikit-learn API models
#             pred = self.artifacts.model.predict(x_inputs)[0]
#             proba = self.artifacts.model.predict_proba(x_inputs)[0][1]
        
#         return ['Yes' if pred == 1 else 'No', float(proba)]

# class PredictionHistoryView(APIView):
#     def get(self, request):
#         records = PredictionRecord.objects.all().order_by('-created_at')
#         serializer = PredictionRecordSerializer(records, many=True)
#         return Response(serializer.data)

# import joblib
# import pandas as pd
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# import os
# from .models import PredictionRecord
# from .serializers import PredictionInputSerializer, PredictionRecordSerializer

# BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# # Load model artifacts
# model = joblib.load(os.path.join(BASE_DIR, '../model/xgb_churn_model.pkl'))
# scaler = joblib.load(os.path.join(BASE_DIR, '../model/scaler.pkl'))
# encoder = joblib.load(os.path.join(BASE_DIR, '../model/encoder.pkl'))
# imputer = joblib.load(os.path.join(BASE_DIR, '../model/imputer.pkl'))
# numeric_features = joblib.load(os.path.join(BASE_DIR, '../model/numeric_features.pkl'))
# categorical_features = joblib.load(os.path.join(BASE_DIR, '../model/categorical_features.pkl'))
# encoded_cols = joblib.load(os.path.join(BASE_DIR, '../model/encoded_columns.pkl'))

# class PredictView(APIView):
#     def post(self, request):
#         # Validate input data
#         serializer = PredictionInputSerializer(data=request.data)
#         if not serializer.is_valid():
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
#         # Get the input data
#         single_input = serializer.validated_data
        
#         # Make prediction
#         result = self.predict_inputss(single_input)
        
#         # Store the prediction
#         prediction_record = PredictionRecord(
#             **single_input,
#             prediction=result[0],
#             probability=result[1]
#         )
#         prediction_record.save()
        
#         # Return the prediction
#         return Response({
#             'prediction': result[0],
#             'probability': result[1],
#             'record_id': prediction_record.id
#         })
    
#     def predict_inputss(self, single_input):
#         input_df = pd.DataFrame([single_input])
#         categorical_feature = [col for col in categorical_features if col not in ['customerID', 'Churn']]
#         input_df['Avg_Monthly_Charge'] = input_df['TotalCharges'] / (input_df['tenure'] + 1)
#         input_df[numeric_features] = imputer.transform(input_df[numeric_features])
#         input_df[numeric_features] = scaler.transform(input_df[numeric_features])
#         input_df[encoded_cols] = encoder.transform(input_df[categorical_feature])
#         x_inputs = input_df[numeric_features + encoded_cols]
#         pred = model.predict(x_inputs)[0]
#         proba = model.predict_proba(x_inputs)[0][1]  # Probability of churn (class 1)
#         return_val = ['Yes' if pred == 1 else 'No', float(proba)]
#         return return_val

# class PredictionHistoryView(APIView):
#     def get(self, request):
#         records = PredictionRecord.objects.all().order_by('-created_at')
#         serializer = PredictionRecordSerializer(records, many=True)
#         return Response(serializer.data)


import joblib
import pandas as pd
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import os
from .models import PredictionRecord
from .serializers import PredictionInputSerializer, PredictionRecordSerializer

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Load model artifacts
model = joblib.load(os.path.join(BASE_DIR, '../model/xgb_churn_model.pkl'))
scaler = joblib.load(os.path.join(BASE_DIR, '../model/scaler.pkl'))
encoder = joblib.load(os.path.join(BASE_DIR, '../model/encoder.pkl'))
imputer = joblib.load(os.path.join(BASE_DIR, '../model/imputer.pkl'))
numeric_features = joblib.load(os.path.join(BASE_DIR, '../model/numeric_features.pkl'))
categorical_features = joblib.load(os.path.join(BASE_DIR, '../model/categorical_features.pkl'))
encoded_cols = joblib.load(os.path.join(BASE_DIR, '../model/encoded_columns.pkl'))

class PredictView(APIView):
    def post(self, request):
        # Validate input data
        serializer = PredictionInputSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        # Get the input data
        single_input = serializer.validated_data
        
        # Make prediction
        result = self.predict_input(single_input)
        
        # Store the prediction
        prediction_record = PredictionRecord(
            **single_input,
            prediction=result[0],
            probability=result[1]
        )
        prediction_record.save()
        
        # Return the prediction
        return Response({
            'prediction': result[0],
            'probability': result[1],
            'record_id': prediction_record.id
        })
    
    def predict_input(self, single_input):
        input_df = pd.DataFrame([single_input])
        
        # Filter out columns that might not exist in the input
        categorical_feature = [col for col in categorical_features 
                             if col in input_df.columns and col not in ['customerID', 'Churn']]
        
        # Feature engineering
        input_df['Avg_Monthly_Charge'] = input_df['TotalCharges'] / (input_df['tenure'] + 1)
        
        # Preprocessing
        input_df[numeric_features] = imputer.transform(input_df[numeric_features])
        input_df[numeric_features] = scaler.transform(input_df[numeric_features])
        
        # Handle categorical encoding
        encoded_data = encoder.transform(input_df[categorical_feature])
        
        # Ensure we have the right number of encoded columns
        if encoded_data.shape[1] != len(encoded_cols):
            raise ValueError(
                f"Number of encoded columns ({encoded_data.shape[1]}) "
                f"doesn't match expected ({len(encoded_cols)})"
            )
        
        # Assign encoded data to dataframe
        input_df[encoded_cols] = encoded_data
        
        # Prepare final features
        x_inputs = input_df[numeric_features + encoded_cols]
        
        # Make prediction
        pred = model.predict(x_inputs)[0]
        proba = model.predict_proba(x_inputs)[0][1]  # Probability of churn (class 1)
        
        return ['Yes' if pred == 1 else 'No', float(proba)]

class PredictionHistoryView(APIView):
    def get(self, request):
        records = PredictionRecord.objects.all().order_by('-created_at')
        serializer = PredictionRecordSerializer(records, many=True)
        return Response(serializer.data)