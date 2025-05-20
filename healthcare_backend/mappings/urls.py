from django.urls import path
from .views import assign_doctor, list_mappings, get_doctors_for_patient, delete_mapping

urlpatterns = [
    path('', list_mappings),
    path('<int:patient_id>/', get_doctors_for_patient),
    path('assign/', assign_doctor),
    path('delete/<int:id>/', delete_mapping),
]
