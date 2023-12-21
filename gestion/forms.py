from django import forms  
from gestion.models import Employee, Material, Position

class EmployeeForm(forms.ModelForm):  
    class Meta:  
        model = Employee  
        fields = ['first_name', 'last_name', 'email','phone_number', 'hire_date', 'position', 'assigned_materials'] 
        widgets = { 'first_name': forms.TextInput(attrs={ 'class': 'form-control' }), 
            'last_name': forms.TextInput(attrs={ 'class': 'form-control' }),
            'email': forms.EmailInput(attrs={ 'class': 'form-control' }),
            'phone_number': forms.TextInput(attrs={ 'class': 'form-control' }),
            'hire_date': forms.DateTimeInput(attrs={ 'class': 'form-control' }),
            #'position': forms.TextInput(attrs={ 'class': 'form-control' }),
        }


class MaterialForm(forms.ModelForm):  
    class Meta:  
        model = Material  
        fields = ['name', 'description'] 
        widgets = { 'name': forms.TextInput(attrs={ 'class': 'form-control' }), 
            'description': forms.Textarea(attrs={ 'class': 'form-control' }),
        }


class PositionForm(forms.ModelForm):  
    class Meta:  
        model = Position  
        fields = ['title'] 
        widgets = { 'title': forms.TextInput(attrs={ 'class': 'form-control' }),
        }
    