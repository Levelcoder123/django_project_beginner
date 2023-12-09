from django.urls import path

from api import views

urlpatterns = [
    path('banks', views.BankListAPIView.as_view(), name='api_banks'),
    path('token', views.CreateUserTokenAPIView.as_view(), name='api_users')
]
