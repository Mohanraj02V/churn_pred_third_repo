from django.urls import path
from .views import PredictView, PredictionHistoryView

urlpatterns = [
    path('predict/', PredictView.as_view(), name='predict'),
    path('history/', PredictionHistoryView.as_view(), name='prediction-history'),
]