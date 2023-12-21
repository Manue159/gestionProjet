from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('employee/list', views.employee_list, name='employee_list'),
    path('employee/new/', views.employee_new, name='employee_new'),
    path('employee/<int:pk>/edit/', views.employee_edit, name='employee_edit'),
    path('employee/<pk>/remove/', views.employee_remove, name='employee_remove'),

    path('material/list', views.material_list, name='material_list'),
    path('material/new/', views.material_new, name='material_new'),
    path('material/<int:pk>/edit/', views.material_edit, name='material_edit'),
    path('material/<pk>/remove/', views.material_remove, name='material_remove'),
    
    path('position/list', views.position_list, name='position_list'),
    path('position/new/', views.position_new, name='position_new'),
    path('position/<int:pk>/edit/', views.position_edit, name='position_edit'),
    path('position/<pk>/remove/', views.position_remove, name='position_remove'),

]
