from django.db import models
from django.core.validators import RegexValidator
from users.models import User
from main.models import LGA, Bank
from academic.models import Institution, Program, Level, Course

# Create your models here.
class Applicant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    guardian_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15, unique=True)
    date_of_birth = models.DateField()
    place_of_birth = models.CharField(max_length=100)
    bvn = models.CharField(max_length=11, unique=True, validators=[
        RegexValidator('^[0-9]{11}$', message='BVN must be exactly 11 digits.')
    ])
    nin = models.CharField(max_length=10, unique=True, validators=[
        RegexValidator('^[0-9]{10}$', message='NIN must be exactly 10 digits.')
    ])
    local_government_area = models.ForeignKey(LGA, on_delete=models.CASCADE)
    contact_address = models.TextField()

class AcademicInformation(models.Model):
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    id_number = models.CharField(max_length=20)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['institution', 'id_number'], name='unique_id_number_per_institution')
        ]

class AccountBank(models.Model):
    account_name = models.CharField(max_length=50)
    account_number = models.CharField(max_length=10, unique=True, validators=[
        RegexValidator('^[0-9]{10}$', message='Account number must be exactly 10 digits.')
    ])
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
class Referees(models.Model):
    fullname = models.CharField(max_length=50)
    occupation = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=15)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Document(models.Model):
    admission_letter = models.ImageField()
    national_id_card = models.ImageField()
    indigen_letter = models.ImageField()
    primary_certificate = models.ImageField()
    ssce_certificate = models.ImageField()
    reciept = models.ImageField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)