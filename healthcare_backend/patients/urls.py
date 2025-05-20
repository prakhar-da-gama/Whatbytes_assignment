from django.urls import path
from .views import create_patient, list_patients, patient_detail

urlpatterns = [
    path('', list_patients),
    path('<int:id>/', patient_detail),
    path('', create_patient),
]
