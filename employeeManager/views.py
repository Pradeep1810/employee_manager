from django.shortcuts import render , redirect
from employeeManager.models import *

# Create your views here.

#our employee manager view function 

def emp_home(request):

    return render(request,'emp_home.html',{})

def add_employee(request):

    #setting default value of isOnBench 

   


     #fetch data 

    name = request.GET.get('empName')

    phone_number = request.GET.get('empNumber')

    adddress = request.GET.get('empAddress')
    
    isOnBench = request.GET.get('isOnBenchCheck')

    if isOnBench is None:

        isOnBench = False

    age = request.GET.get('empAge')

    #create the model class object 

    emp = Employee()

    emp.name = name

    emp.phone_number = phone_number

    emp.address = adddress

    emp.isOnTable = isOnBench

    emp.age = age

    #save the employee 

    emp.save()

    print(emp.name)

    return render(request,'emp_home.html',{})

def view_emps(request):

    all_emps = Employee.objects.all()

    data = {

        'all_emps' : all_emps
    }

    return render(request,'view_emps.html',data)

def delete_emp(request , emp_id):

    emp = Employee.objects.get(pk = emp_id)

    emp.delete()

    return redirect("/emp/view/")

   # return render(request,'view_emps.html',{}) # when we are directly trying to return it returns just the temolate and not the data loaded template

#for achieving the latter we need to redirect it to the url so that url gets fired up and data gets loaded 

def update_emp(request,emp_id):

    emp = Employee.objects.get(pk = emp_id)

    print(emp.name)

    data = {

        "emp" : emp
    }   

    return render(request,'update_emp.html',data)

def do_update(request, emp_id):

    #since the name and age is non changeable we don't get it 

    #also making the field disabled stops the field to be included in form submission
    
    emp = Employee.objects.get(pk=emp_id)

    phone_number = request.GET.get('empNumber')

    adddress = request.GET.get('empAddress')
    
    isOnBench = request.GET.get('isOnBenchCheck')

    if isOnBench is None:

        isOnBench = False

    

    emp.phone_number = phone_number

    emp.address = adddress

    emp.isOnTable = isOnBench

    #save the employee 

    emp.save()

    return redirect("/emp/view/")


def emp_reviews(request):

    reviews = EmpReview.objects.all()

    return render(request,'emp_review.html',{'review' : reviews})

    

   

    