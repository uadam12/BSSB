from django.shortcuts import redirect
from django.contrib import messages
from django.http import JsonResponse
from users.forms import UserForm
from .forms import ApplicantForm, AcademicInformationForm, AccountBankForm, DocumentForm, RefereesForm
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
            return JsonResponse({
                'status': 'success',
                'message': 'Personal information save successfully!'
            })
    
    return JsonResponse({
        'status': 'danger',
        'message': 'Something went wrong'
    })

def save_academic_information(request):
    if is_post(request):
        form = AcademicInformationForm(request.POST)
        
        if form.is_valid():
            academic_info = form.save(False)
            academic_info.user = request.user
            academic_info.save()
            
            return JsonResponse({
                'status': 'success',
                'message': 'Academic information save successfully!'
            })
    
    return JsonResponse({
        'status': 'danger',
        'message': 'Something went wrong'
    })

def save_account_details(request):
    if is_post(request):
        form = AccountBankForm(request.POST)
        
        if form.is_valid():
            account_bank = form.save(False)
            account_bank.user = request.user
            account_bank.save
            
            return JsonResponse({
                'status': 'success',
                'message': 'Account bank details save successfully!'
            })
    
    return JsonResponse({
        'status': 'danger',
        'message': 'Something went wrong'
    })

def save_documents(request):
    if is_post(request):
        form = DocumentForm(request.POST)
        
        if form.is_valid():
            document = form.save(False)
            document.user = request.user
            document.save()
            
            return JsonResponse({
                'status': 'success',
                'message': 'Documents save successfully!'
            })
    
    return JsonResponse({
        'status': 'danger',
        'message': 'Something went wrong'
    })


def save_referees(request):
    if is_post(request):
        form = RefereesForm(request.POST)
        
        if form.is_valid():
            referees = form.save(False)
            referees.user = request.user
            referees.save()
            
            return JsonResponse({
                'status': 'success',
                'message': 'Referees information save successfully!'
            })
    
    return JsonResponse({
        'status': 'danger',
        'message': 'Something went wrong'
    })