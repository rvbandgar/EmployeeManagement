import json
from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Employee, EmployeeSkills

baseUrl = "http://127.0.0.1:8000"


# Create your views here.
def home(request):
    # return HttpResponse("Python is easy")
    return render(request, "app/base.html")


@csrf_exempt
def add_employee_data(request):
    if request.method == "POST":
        response = {}
        print("in post method")
        print(f"requets data=====>{request.POST}")
        emp_first_name = request.POST.get("emp_first_name")
        emp_last_name = request.POST.get("emp_last_name")
        emp_designation = request.POST.get("emp_designation")
        skills = request.POST.getlist('skills[]')
        print(f"{skills=},{type(skills)=}")
        skills_str = ','.join(skills)

        Employee.objects.create(
            emp_first_name=emp_first_name,
            emp_last_name=emp_last_name,
            emp_designation=emp_designation,
            skills=skills_str
        ).save()
        response = {
            "status": True,
            "status_code": 200,
            "message": "Employee Details Added Successfully",
        }
        return JsonResponse(response, safe=False)
    else:
        print("pass the context required in front end")
        skills = EmployeeSkills.objects.all().order_by("id")
        return render(
            request, "app/addEmployee.html", {"baseUrl": baseUrl, "skills": skills}
        )


@csrf_exempt
def edit_employee_data(request, id):
    if request.method == "POST":
        response = {}
        emp_first_name = request.POST.get("emp_first_name")
        emp_last_name = request.POST.get("emp_last_name")
        emp_designation = request.POST.get("emp_designation")
        skills = request.POST.getlist('skills[]')
        print(f"{skills=},{type(skills)=}")
        skills_str = ','.join(skills)
        

        employee_object = Employee.objects.filter(emp_id=id).update(
            emp_first_name=emp_first_name,
            emp_last_name=emp_last_name,
            emp_designation=emp_designation,
            skills=skills_str
        )

        response = {
            "status": True,
            "status_code": 200,
            "message": "Employee Details Updated Successfully",
        }
        return JsonResponse(response, safe=False)
    else:
        skillarray=[]
        employee = Employee.objects.get(emp_id=id)  # Fetch employee details
        skills=employee.skills
        print(f"skills===>{skills}")
        if skills:
            skillarray=skills.split(',')
            print(f"skillarray===>{skillarray}")
        all_skills = list(EmployeeSkills.objects.all().order_by("id"))

        # baseUrl = 'your_base_url'  # Define your base URL
        return render(
            request,
            "app/editEmployee.html",
            {"baseUrl": baseUrl, "emp_id": id, "employee": employee,"skills":skillarray,
             "all_skills":all_skills}
        )


@csrf_exempt
def delete_employee_data(request, id):
    Employee.objects.filter(emp_id=id).delete()
    # return render(request, 'app/employee.html',{'baseUrl':baseUrl})
    return redirect("/showdata")


# @csrf_exempt
# def edit_employee_data(request,id):
#     # employee_object = Employee.objects.filter(emp_id=id)

#     if request.method=="POST":
#         response={}
#         print("in post method")
#         print(f'requets data=====>{request.POST}')
#         emp_first_name=request.POST.get('emp_first_name')
#         emp_last_name=request.POST.get('emp_last_name')
#         emp_designation=request.POST.get('emp_designation')

#         employee_object = Employee.objects.filter(emp_id=id).update(emp_first_name=emp_first_name,emp_last_name=emp_last_name,
#                                 emp_designation=emp_designation)

#         print(f'employee_obj=========>{employee_object}')

#         response={
#             'status':True,
#             'status_code':200,
#             'message':'Employee Details Updated Successfully'
#         }
#         return JsonResponse(response, safe=False)
#     else:
#         print('pass the context required in front end')
#         return render(request,'app/editEmployee.html',{'baseUrl':baseUrl,'emp_id':id})


@csrf_exempt
def show_data(request):
    if request.method == "POST":
        response = {}
        try:
            body_unicode = request.body.decode("utf-8")
            parsed_data = json.loads(body_unicode)
            print(f"parsed_data======>{parsed_data}")

            payload = parsed_data.get("payload")

            temp = json.loads(payload)

            print(f"temp========>{temp}")

            emp_id = temp.get("emp_id")

            print(f"{emp_id=}, {parsed_data=}")

            # payload = request.POST.get('payload')
            # parsed_data = json.loads(payload)

            # emp_id = parsed_data.get('emp_id')

            # print(f'{parsed_data=},{emp_id=}')

            emp_object = list(Employee.objects.filter(emp_id=emp_id).values())
            print(f"{emp_object=}")

            response = {"status": True, "message": "success", "data": emp_object}
        except Exception as e:
            print(f"Error: {e}")
            response = {"status": False, "message": str(e)}

        return JsonResponse(response, safe=False)
    else:
        employee_object = Employee.objects.all().values()
        print(f"employee_object==========>{employee_object}")
        return render(
            request, "app/employee.html", {"employee_object": employee_object}
        )
