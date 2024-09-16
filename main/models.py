from django.db import models
from django.core.validators import RegexValidator


# Create your models here.
class Bank(models.Model):
    name = models.CharField(max_length=70, unique=True)
    code = models.CharField(max_length=4, primary_key=True, validators=[
        RegexValidator('^[0-9]{3}$', message='Bank code must be exactly 3 digits.')
    ])

    def __str__(self) -> str:
        return self.name
    
class LGA(models.Model):
    name = models.CharField(max_length=70, unique=True)
    
    def __str__(self) -> str:
        return f"{self.name} local government"

class Article(models.Model):
    headline = models.CharField(max_length=100)
    headline_image = models.ImageField(upload_to='articles', null=True, blank=True)
    content = models.TextField()
    publish_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.headline