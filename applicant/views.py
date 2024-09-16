from django.shortcuts import redirect
from django.contrib import messages
from users.forms import UserForm
from .forms import ApplicantForm, AcademicInformationForm
from app import is_post


# Create your views here.
def save_personal_information(request):
    if is_post(request):
        user_form = UserForm(instance=request.user, data=request.POST)
        applicant_form = ApplicantForm(request.POST)
        
        if user_form.is_valid() and applicant_form.is_valid():
            user_form.save()
            applicant = applicant_form.save(False)
            applicant.user = request.user
            applicant.save()
            messages.success(request, 'Personal information save successfully!')
    
    return redirect('user:profile')

def save_academic_information(request):
    if is_post(request):
        academic_form = AcademicInformationForm(request.POST)
        
        if academic_form.is_valid():
            academic_info = academic_form.save(False)
            academic_info.user = request.user
            academic_info.save()
            messages.success(request, 'Academic information save successfully!')
    
    return redirect('user:profile')
            