from django.db import models
from django.utils import timezone

# Create your models here.
class Position(models.Model):
    title = models.CharField(max_length=255, unique=True)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
    

class Material(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class Employee(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    hire_date = models.DateTimeField()
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(default=timezone.now)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    assigned_materials = models.ManyToManyField(Material, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
