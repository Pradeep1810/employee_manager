from django.contrib import admin
from django.urls import path , include
from .views import *

urlpatterns = [
   
   path('home/',emp_home ) ,

   path('add/',add_employee) ,

   path('view/' ,view_emps) , 

   path('delete_emp/<int:emp_id>',delete_emp) ,

   path('update_emp/<int:emp_id>',update_emp)  ,

   path('do_update/<int:emp_id>',do_update) ,

   path('reviews',emp_reviews)
]