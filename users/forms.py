from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from crispy_forms.layout import Layout, Row, Column
from crispy_forms.helper import FormHelper


class UserForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['first_name'].widget.attrs['placeholder'] = 'Enter your firstname here...'
        self.fields['first_name'].widget.attrs['required'] = True
        self.fields['last_name'].widget.attrs['placeholder'] = 'Enter your lastname here...'
        self.fields['last_name'].widget.attrs['required'] = True
        
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('first_name', css_class='form-group col-md-6 mb-0'),
                Column('last_name', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            )
        )


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['first_name'].widget.attrs['placeholder'] = 'Enter your firstname here...'
        self.fields['first_name'].widget.attrs['required'] = True
        self.fields['last_name'].widget.attrs['placeholder'] = 'Enter your lastname here...'
        self.fields['last_name'].widget.attrs['required'] = True
        self.fields['email'].widget.attrs['placeholder'] = 'Enter your email address here...'
        self.fields['username'].widget.attrs['placeholder'] = 'Enter your username here...'
        self.fields['password1'].widget.attrs['placeholder'] = 'Create strong password here...'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm your password here...'

        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('first_name', css_class='form-group col-md-6 mb-0'),
                Column('last_name', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            
            Row(
                Column('email', css_class='form-group col-md-6 mb-0'),
                Column('username', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            
            Row(
                Column('password1', css_class='form-group col-md-6 mb-0'),
                Column('password2', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            )
        )


class UserAddForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('email', )

class UserEditForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('email', )

class LoginForm(forms.Form):
    email = forms.EmailField(label='Email address', widget=forms.EmailInput(attrs={
        'required': True,
        'placeholder': 'Enter your email address here...'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'required': True,
        'placeholder': 'Enter your password here...'
    }))
