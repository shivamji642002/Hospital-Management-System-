from django.urls import path
from . import views
# Create your views here.
app_name = "patient"

urlpatterns = [
    path('', views.patient_home, name='patient_home'),
    path('list/', views.patient_list, name='patient_list'),
    path('create/', views.patient_create, name='patient_create'),
    path('update/<int:pk>/', views.patient_update, name='patient_update'),
    path('delete/<int:pk>/', views.patient_delete, name='patient_delete'),
    path('appointment/request/', views.appointment_request, name='appointment_request'),
     path('appointments/', views.appointment_list, name='appointment_list'),
    path('appointments/<int:pk>/approve/', views.approve_appointment, name='approve_appointment'),  # NE
]
