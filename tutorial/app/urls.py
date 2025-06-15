from django.urls import path
from . import views


urlpatterns = [
    path('home', views.home),
    path('addemployee',views.add_employee_data, name="addEmployee"),
    path('editemployee/<int:id>', views.edit_employee_data, name="editEmployee"),
    path('deleteemployee/<int:id>', views.delete_employee_data, name='deleteemployee'),
    path('showdata',views.show_data, name='showData'),
]