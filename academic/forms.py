from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column
from .models import InstitutionType, Institution, Program, Course, Level

class InstitutionTypeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(InstitutionTypeForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = 'Enter Institution Type Name here...'
    
    class Meta:
        model = InstitutionType
        fields = ("name",)
    
    
class InstitutionForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(InstitutionForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = 'Enter Institution Name here...'
        self.fields['type'].empty_label = 'Select Institution Type'
        self.fields['matrix_number_format'].widget.attrs['placeholder'] = 'Enter student(s) matrix number format...'
        
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('name', css_class='form-group col-md-6 mb-0'),
                Column('type', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('programs', css_class='form-group col-md-6 mb-0'),
                Column('courses', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            'matrix_number_format', 'is_internal'
        )

    class Meta:
        model = Institution
        fields = ("name", "type", 'matrix_number_format', 'is_internal', 'programs', 'courses')


class ProgramForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProgramForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = 'Enter Program Name here...'

    class Meta:
        model = Program
        fields = ("name",)

class LevelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(LevelForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = 'Enter Level Name here...'
        self.fields['code'].widget.attrs['placeholder'] = 'Enter Level Code here...'
    
    class Meta:
        model = Level
        fields = ("name", "code", "program")

class CourseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CourseForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['placeholder'] = 'Enter Course Title here...'

    class Meta:
        model = Course
        fields = ("title",)
