from django.urls import path
from . import views

app_name = "doctor"

urlpatterns = [
    path('', views.doctor_home, name='doctor_home'),
    path('appointments/', views.appointment_list, name='appointment_list'),
    path('approve/<int:pk>/', views.approve_appointment, name='approve_appointment'),
]
