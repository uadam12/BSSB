from django.urls import path
from . import views

app_name = 'applicant-api'

urlpatterns = [
    path('personal-info/', views.save_personal_information, name='save-personal-info'),
    path('academic-info/', views.save_academic_information, name='save-academic-info'),
    path('bank-info/', views.save_account_details, name='save-bank-info'),
    path('documents/', views.save_documents, name='save-documents'),
    path('referees/', views.save_referees, name='save-referees'),
]