from django.urls import path
from .views import create_doctor, list_doctors, doctor_detail

urlpatterns = [
    path('', list_doctors),
    path('<int:id>/', doctor_detail),
    path('create', create_doctor),
]
