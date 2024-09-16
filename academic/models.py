from django.db import models

# Create your models here.
class Program(models.Model):
    name = models.CharField(max_length=25, unique=True)
    
    class Meta:
        verbose_name = "program"
        verbose_name_plural = "programs"
        
    def __str__(self):
        return self.name

class Course(models.Model):
    title = models.CharField(max_length=100, unique=True)    

    class Meta:
        verbose_name = "course"
        verbose_name_plural = "courses"

    def __str__(self):
        return self.title
    
class Level(models.Model):
    name = models.CharField(max_length=20)
    code = models.PositiveIntegerField()
    program = models.ForeignKey(Program, on_delete=models.CASCADE, related_name='levels')
    

    class Meta:
        verbose_name = "level"
        verbose_name_plural = "levels"
        constraints = [
            models.UniqueConstraint(fields=['program', 'code'], name='unique_level_code_per_program')
        ]

    def __str__(self):
        return self.name

class InstitutionType(models.Model):
    name = models.CharField(max_length=30, unique=True)
    
    class Meta:
        verbose_name = "institution_type"
        verbose_name_plural = "institution_types"

    def __str__(self):
        return self.name
    

class Institution(models.Model):
    name = models.CharField(max_length=50)
    matrix_number_format = models.CharField(max_length=50)
    is_internal = models.BooleanField(default=True)
    type = models.ForeignKey(InstitutionType, on_delete=models.CASCADE, related_name='institutions')
    programs = models.ManyToManyField(Program, related_name='institutions')
    courses = models.ManyToManyField(Course, related_name='institutions')

    class Meta:
        verbose_name = "institution"
        verbose_name_plural = "institutions"
        
    def __str__(self):
        return self.name
