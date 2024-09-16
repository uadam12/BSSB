from app.views import details_view, update_view, delete_view
from .forms import (
    Institution, InstitutionForm,
    InstitutionType, InstitutionTypeForm,
    Program, ProgramForm,
    Course, CourseForm,
    Level, LevelForm
)

# Institution type
def institution_types(request):
    return details_view(
        request, InstitutionTypeForm, 
        header="Institution Type",
        data_template='academic/institution-types.html',
        institution_types = InstitutionType.objects.order_by('name')
    )

def update_institution_type(request, id):
    inst_type = InstitutionType.objects.get(id=id)
    
    return update_view(
        request, 
        model=inst_type, 
        form_class=InstitutionTypeForm, 
        success_url='academic:institution-types', 
        header='Institution Type'
    )

    
def delete_institution_type(request, id):
    inst_type = InstitutionType.objects.get(id=id)
    
    return delete_view(
        request, 
        model=inst_type,
        success_url='academic:institution-types', 
        header='Institution Type'
    )

# Institutions
def institutions(request):
    return details_view(
        request, InstitutionForm, 
        header="Institution",
        data_template='academic/institutions.html',
        institutions = Institution.objects.order_by('type', 'name')
    )

def update_institution(request, id):
    institution = Institution.objects.get(id=id)
    
    return update_view(
        request, 
        model=institution, 
        form_class=InstitutionForm, 
        success_url='academic:institutions', 
        header='Institution'
    )

    
def delete_institution(request, id):
    institution = Institution.objects.get(id=id)
    
    return delete_view(
        request, 
        model=institution,
        success_url='academic:institutions', 
        header='Institution'
    )
    
# Programs
def programs(request):
    return details_view(
        request, ProgramForm, 
        header="Program",
        data_template='academic/programs.html',
        programs = Program.objects.order_by('name')
    )

def update_program(request, id):
    program = Program.objects.get(id=id)
    
    return update_view(
        request, 
        model=program, 
        form_class=ProgramForm, 
        success_url='academic:programs', 
        header='Program'
    )

    
def delete_program(request, id):
    program = Program.objects.get(id=id)
    
    return delete_view(
        request, 
        model=program,
        success_url='academic:programs', 
        header='Program'
    )
    
# Courses
def courses(request):
    return details_view(
        request, CourseForm, 
        header="Course",
        data_template='academic/courses.html',
        courses = Course.objects.order_by('title')
    )

def update_course(request, id):
    course = Course.objects.get(id=id)
    
    return update_view(
        request, 
        model=course, 
        form_class=CourseForm, 
        success_url='academic:courses', 
        header='Course'
    )

    
def delete_course(request, id):
    course = Course.objects.get(id=id)
    
    return delete_view(
        request, 
        model=course,
        success_url='academic:courses', 
        header='Course'
    )
    
# Levels
def levels(request):
    return details_view(
        request, LevelForm, 
        header="Level",
        data_template='academic/levels.html',
        levels = Level.objects.order_by('program', 'code', 'name')
    )

def update_level(request, id):
    level = Level.objects.get(id=id)
    
    return update_view(
        request, 
        model=level, 
        form_class=LevelForm, 
        success_url='academic:levels', 
        header='Level'
    )

    
def delete_level(request, id):
    level = Level.objects.get(id=id)
    
    return delete_view(
        request, 
        model=level,
        success_url='academic:levels', 
        header='Level'
    )