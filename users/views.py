from django.contrib import messages
from django.contrib.auth import login as login_user, logout as logout_user, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from app import render, is_post, get_or_none
from .forms import RegisterForm, LoginForm, UserForm
from applicant.forms import (
    ApplicantForm, Applicant, 
    AcademicInformationForm, AcademicInformation,
    AccountBankForm, AccountBank,
    DocumentForm, Document,
    RefereesForm, Referees
)

# Create your views here.
def register(request):
    form = RegisterForm
    
    if is_post(request):
        form = RegisterForm(request.POST)

        if form.is_valid() and form.save():
            messages.success(request, 'Account created successfully!')
            return redirect('user:login')
    
    return render(
        request, 'users/register',
        title = 'BSSB Registration',
        form = form
    )

# Create your views here.
def login(request):
    form = LoginForm()
    
    if is_post(request):
        form = LoginForm(request.POST)

        if form.is_valid():
            email = form.data.get('email')
            password = form.data.get('password')
            user = authenticate(request, email=email, password=password)
            
            if user is None:
                messages.error(request, "Invalid password and/or email address." )
            else:
                login_user(request, user)
                messages.success(request, 'You have login successfully!!!')
                return redirect('user:dashboard')
        else: messages.error(request, str(form.error_messages))
            
    return render(
        request, 'users/login', 
        title = 'BSSB Login',
        form=form
    )

def logout(request):
    if is_post(request):
        messages.success(request, 'You have logout successfully!')
        logout_user(request)
    
    return redirect('user:login')

def forgot_password(request):
    return render(request, 'forgot-password', title='BSSB Forgot password')

@login_required
def dashboard(request):
    return render(request, 'users/dashboard', title='BSSB Dashboard')

@login_required
def profile(request):
    user = request.user
    applicant = get_or_none(Applicant, user=user)
    academic_info = get_or_none(AcademicInformation, user=user)
    account_bank = get_or_none(AccountBank, user=user)
    documents = get_or_none(Document, user=user)
    referees = get_or_none(Referees, user=user)

    return render(
        request, 'users/profile', 
        title='BSSB Dashboard',
        user_form = UserForm(instance=request.user),
        applicant_form = ApplicantForm(instance=applicant),
        academic_form = AcademicInformationForm(instance=academic_info),
        bank_form = AccountBankForm(instance=account_bank),
        documents_form = DocumentForm(instance=documents),
        referees_form = RefereesForm(instance=referees)
    )