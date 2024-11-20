from django.shortcuts import render, redirect, get_object_or_404
from gestion.forms import EmployeeForm, MaterialForm, PositionForm
from gestion.models import Employee, Material, Position
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.
#employees
def home(request):
    return render(request, 'gestion/home.html')


def employee_list(request):
    employee = Employee.objects.all()
    return render(request, 'gestion/employe_list.html', {'employees': employee})


@login_required
def employee_new(request):
    material = Material.objects.all()
    position = Position.objects.all()
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            employee = form.save(commit=False)
            employee.author = request.user
            employee.save()

            assigned_materials = form.cleaned_data['assigned_materials']
            employee.assigned_materials.set(assigned_materials)

            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'gestion/employe_new.html', {'form': form, 'materials': material, 'positions': position})


@login_required
def employee_edit(request, pk):
    material = Material.objects.all()
    position = Position.objects.all()
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == "POST":
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            employee = form.save(commit=False)
            employee.author = request.user
            employee.save()

            assigned_materials = form.cleaned_data['assigned_materials']
            employee.assigned_materials.set(assigned_materials)

            return redirect('employee_list')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'gestion/employe_edit.html', {'form': form, 'materials': material, 'positions': position})


@login_required
def employee_remove(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    employee.delete()
    return redirect('employee_list')


def material_list(request):
    material = Material.objects.all()
    return render(request, 'gestion/material_list.html', {'materials': material})


@login_required
def material_new(request):
    if request.method == "POST":
        form = MaterialForm(request.POST)
        if form.is_valid():
            material = form.save(commit=False)
            material.author = request.user
            material.save()
            return redirect('material_list')
    else:
        form = MaterialForm()
    return render(request, 'gestion/material_new.html', {'form': form})

@login_required
def material_edit(request, pk):
    material = get_object_or_404(Material, pk=pk)
    if request.method == "POST":
        form = MaterialForm(request.POST, instance=material)
        if form.is_valid():
            material = form.save(commit=False)
            material.author = request.user
            material.save()
            return redirect('material_list')
    else:
        form = MaterialForm(instance=material)
    return render(request, 'gestion/material_edit.html', {'form': form})


@login_required
def material_remove(request, pk):
    material = get_object_or_404(Material, pk=pk)
    material.delete()
    return redirect('material_list')


def position_list(request):
    position = Position.objects.all()
    return render(request, 'gestion/position_list.html', {'positions': position})


@login_required
def position_new(request):
    if request.method == "POST":
        form = PositionForm(request.POST)
        if form.is_valid():
            position = form.save(commit=False)
            position.author = request.user
            position.save()
            return redirect('position_list')
    else:
        form = PositionForm()
    return render(request, 'gestion/position_new.html', {'form': form})


@login_required
def position_edit(request, pk):
    position = get_object_or_404(Position, pk=pk)
    if request.method == "POST":
        form = PositionForm(request.POST, instance=position)
        if form.is_valid():
            position = form.save(commit=False)
            position.author = request.user
            position.save()
            return redirect('position_list')
    else:
        form = PositionForm(instance=position)
    return render(request, 'gestion/position_edit.html', {'form': form})


@login_required
def position_remove(request, pk):
    position = get_object_or_404(Position, pk=pk)
    position.delete()
    return redirect('position_list')

@login_required
def signout(request):
    logout(request)
    return redirect('/')


