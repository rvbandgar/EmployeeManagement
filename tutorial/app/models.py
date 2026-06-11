from django.db import models

# Create your models here.


class Employee(models.Model):
    emp_id = models.AutoField(primary_key=True)
    emp_first_name = models.CharField(max_length=100, null=True, blank=True)
    emp_last_name = models.CharField(max_length=100, null=True, blank=True)
    emp_designation = models.CharField(max_length=100, null=True, blank=True)
    skills = models.CharField(max_length=100, null=True, blank=True)
    experience=models.FloatField(null=True)

    # class Meta:
    #     db_table='app_employee'
    #     managed=False

    def __str__(self) -> str:
        # return super().__str__()
        return self.emp_first_name


class EmployeeDirectory(models.Model):
    doc_id = models.AutoField(primary_key=True)
    directory_name = models.CharField(max_length=100)
    document_directory = models.CharField(max_length=200)
    updated_by = models.CharField(max_length=100)
    updated_at = models.DateTimeField(auto_now=True)

    # class Meta:
    #     managed=True
    #     db_table='employee_directory'


class EmployeeSkills(models.Model):
    skill_name = models.CharField(max_length=200)

    def __str__(self):
        return self.skill_name


class EducationalQualification(models.Model):
    qualification_name=models.CharField(max_length=100)

    def __str__(self):
        return self.qualification_name
    

