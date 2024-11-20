from django import forms  
from gestion.models import Employee, Material, Position

class EmployeeForm(forms.ModelForm):  
    class Meta:  
        model = Employee  
        fields = ['first_name', 'last_name', 'email','phone_number', 'hire_date', 'position', 'assigned_materials'] 
        labels = {
            'first_name': '',
            'last_name': '',
            'email': '',
            'phone_number': '',
            'hire_date': '',
            'position': '',
            'assigned_materials': '',
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control-input', 'placeholder': 'Firstname'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control-input', 'placeholder': 'Lastname'}),
            'email': forms.EmailInput(attrs={'class': 'form-control-input', 'placeholder': 'Email'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control-input', 'placeholder': 'Phone number'}),
            'hire_date': forms.DateInput(attrs={'class': 'form-control-input', 'placeholder': 'Hire date', 'type': 'date'}),
            'position': forms.Select(attrs={'class': 'form-control-select'}),
            'assigned_materials': forms.Select(attrs={'class': 'form-control-select'}),
        }


class MaterialForm(forms.ModelForm):  
    class Meta:  
        model = Material  
        fields = ['name', 'description'] 
        labels = {
            'name' : '',
            'description' : '',
        }
        widgets = { 
            'name': forms.TextInput(attrs={ 'class': 'form-control-input', 'placeholder': 'name' }), 
            'description': forms.Textarea(attrs={ 'class': 'form-control-textarea', 'placeholder': 'description' }),
        }


class PositionForm(forms.ModelForm):  
    class Meta:  
        model = Position  
        fields = ['title'] 
        labels = {
            'title' : '',
        }
        widgets = { 
            'title': forms.TextInput(attrs={ 'class': 'form-control-input', 'placeholder': 'title' }),
        }
    