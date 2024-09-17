from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column
from .models import Applicant, AcademicInformation, AccountBank, Document, Referees


class ApplicantForm(forms.ModelForm):
    class Meta:
        model = Applicant
        exclude = ('user', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['guardian_name'].widget.attrs['placeholder'] = 'Enter guardian name here...'
        self.fields['phone_number'].widget.attrs['placeholder'] = 'Enter phone number here...'
        self.fields['date_of_birth'].widget.attrs['placeholder'] = 'Enter date of birth here...'
        self.fields['place_of_birth'].widget.attrs['placeholder'] = 'Enter place of birth here...'
        self.fields['bvn'].widget.attrs['placeholder'] = 'Enter bank varification number here...'
        self.fields['nin'].widget.attrs['placeholder'] = 'Enter national identification number here...'
        self.fields['local_government_area'].empty_label = 'Select Local Government Area'
        self.fields['contact_address'].widget.attrs['placeholder'] = 'Enter contact address here...'
        
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Row(
                Column('guardian_name', css_class='form-group col-md-6 mb-0'),
                Column('phone_number', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            
            Row(
                Column('date_of_birth', css_class='form-group col-md-6 mb-0'),
                Column('place_of_birth', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            
            Row(
                Column('bvn', css_class='form-group col-md-6 mb-0'),
                Column('nin', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            
            Row(
                Column('local_government_area', css_class='form-group col-md-6 mb-0'),
                Column('contact_address', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            )
        )
        
class AcademicInformationForm(forms.ModelForm):
    
    class Meta:
        model = AcademicInformation
        exclude = ('user', )
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['id_number'].widget.attrs['placeholder'] = 'Enter your ID number here...'
        self.fields['institution'].empty_label = 'Select institution'
        self.fields['program'].empty_label = 'Select program'
        self.fields['course'].empty_label = 'Select course of study'
        
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Row(
                Column('institution', css_class='form-group col-md-6 mb-0'),
                Column('program', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('course', css_class='form-group col-md-6 mb-0'),
                Column('id_number', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
        )

class AccountBankForm(forms.ModelForm):
    
    class Meta:
        model = AccountBank
        exclude = ('user', )
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['bank'].empty_label = 'Select your bank'
        self.fields['account_number'].widget.attrs['placeholder'] = 'Enter your account number here...'
        self.fields['account_name'].widget.attrs['placeholder'] = 'Enter your account name here...'
        
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Row(
                Column('bank', css_class='form-group col-md-6 mb-0'),
                Column('account_number', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            'account_name'
        )
        
class DocumentForm(forms.ModelForm):
    
    class Meta:
        model = Document
        exclude = ('user',)
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Row(
                Column('national_id_card', css_class='form-group col-md-6 mb-0'),
                Column('indigen_letter', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('ssce_certificate', css_class='form-group col-md-6 mb-0'),
                Column('primary_certificate', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('admission_letter', css_class='form-group col-md-6 mb-0'),
                Column('reciept', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            
        )


class RefereesForm(forms.ModelForm):
    
    class Meta:
        model = Referees
        exclude = ("user",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['fullname'].widget.attrs['placeholder'] = 'Enter referees fullname here...'
        self.fields['occupation'].widget.attrs['placeholder'] = 'Enter occupation here...'
        self.fields['phone_number'].widget.attrs['placeholder'] = 'Enter referees fullname here...'
        
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            'fullname',
            Row(
                Column('phone_number', css_class='form-group col-md-6 mb-0'),
                Column('occupation', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            )
        )