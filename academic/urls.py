from django.urls import path
from . import views

app_name = 'academic'

urlpatterns = [
    # Institution types
    path('institution-types/', views.institution_types, name='institution-types'),
    path('institution-types/<int:id>/update', views.update_institution_type, name='update-institution-type'),
    path('institution-types/<int:id>/delete', views.delete_institution_type, name='delete-institution-type'),

    # Institutions
    path('institutions/', views.institutions, name='institutions'),
    path('institutions/<int:id>/update', views.update_institution, name='update-institution'),
    path('institutions/<int:id>/delete', views.update_institution, name='delete-institution'),
    
    # Programs
    path('programs/', views.programs, name='programs'),
    path('programs/<int:id>/update', views.update_program, name='update-program'),
    path('programs/<int:id>/delete', views.delete_program, name='delete-program'),

    # Courses
    path('courses/', views.courses, name='courses'),
    path('courses/<int:id>/update', views.update_course, name='update-course'),
    path('courses/<int:id>/delete', views.delete_course, name='delete-course'),
    
    # Levels
    path('levels/', views.levels, name='levels'),
    path('levels/<int:id>/update', views.update_level, name='update-level'),
    path('levels/<int:id>/delete', views.delete_level, name='delete-level'),
]
