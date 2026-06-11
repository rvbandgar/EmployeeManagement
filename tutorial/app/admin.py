from django.contrib import admin
from .models import Employee,EmployeeSkills,EmployeeDirectory,EducationalQualification




class EmployeeSkillsAdmin(admin.ModelAdmin):
    list_display=('id','skill_name')



# Register your models here.

admin.site.register(Employee)
admin.site.register(EmployeeSkills, EmployeeSkillsAdmin)
admin.site.register(EmployeeDirectory)
admin.site.register(EducationalQualification)