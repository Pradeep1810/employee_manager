from django.contrib import admin
from employeeManager.models import *


#to modify the viewing style 

#creating a class for our app

class EmployeeAdmin(admin.ModelAdmin):

    #these properties helps us to modify the style 

    list_filter =('isOnTable',)

    search_fields = ('name','address')

    list_display = ('name','address','isOnTable')

# Register your models here.

admin.site.register(Employee,EmployeeAdmin)

admin.site.register(EmpReview)