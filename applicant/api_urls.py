from django.urls import path
from . import views

app_name = 'applicant-api'

urlpatterns = [
    path('personal-info/', views.save_personal_information, name='save-personal-info'),
    path('academic-info/', views.save_academic_information, name='save-academic-info'),
]