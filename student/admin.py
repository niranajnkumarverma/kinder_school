
from django.contrib import admin
from student.models import Code, Country, Student, UserOTP,State,City


   
admin.site.register(Country)
admin.site.register(Student)
admin.site.register(State)
admin.site.register(City)
admin.site.register(UserOTP)
admin.site.register(Code)