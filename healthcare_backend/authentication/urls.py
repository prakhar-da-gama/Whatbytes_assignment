from django.urls import path
from .views import RegisterView
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('register/', RegisterView),
    path('login/', TokenObtainPairView.as_view()),
]
