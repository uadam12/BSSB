from django.urls import include, path

urlpatterns = [
    path('', include('applicant.api_urls')),
]