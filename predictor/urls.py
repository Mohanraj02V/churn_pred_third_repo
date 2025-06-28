from django.urls import path
from .views import PredictView, PredictionHistoryView
# Temporary view for testing
def home(request):
    return HttpResponse("Churn Prediction API is running!")
urlpatterns = [
    path('', home),
    path('predict/', PredictView.as_view(), name='predict'),
    path('history/', PredictionHistoryView.as_view(), name='prediction-history'),
]
