from django.http import HttpResponse  
from django.shortcuts import render

 
def home(request):
    
    print("entered the home views.py")

    # return HttpResponse("<h1> home page running through home def in views.py</h1>")

    #passing data from views to template 

    heading = "Employee Details Form"

    designations = ['SDE' , 'JAVA DEVLOPER' , 'FRONTEND']

   

    #creating a dictonary to pass

    data = {
               "heading" : heading ,

               "positions" : designations ,
               
        }

    return render(request,"home.html",data) #both the view and url are at same level 

#request at urls.py ( project level) -> views.py(project level)

def about(request):

   
    #passing a student dict object 

    doShow = False

    if request.method == 'POST':

        show = request.POST.get('checkbox') #for method is post when it is get remove post and use directly 

        if show == 'True':

            doShow = True

        elif show is None:
           
           
           
           doShow = False

    student = {

        "student_name" : "Ravi Krishna Daas" ,
        "student_subject" : "Devotional Service" ,
        "student_goal" : "Goloka"
    }

    #creating a dictonary to pass

    data = {
               
             "student_data" : student ,
             "doShow" : doShow
        }
    
  #  return HttpResponse("<h1> This is about page </h1>")
    return render(request,"about.html",data) #both the view and url are at same level (project level)


def homeEmployee(request):

    return render(request,"home2.html",{})