from django.contrib import admin
from home.models import User, Admin, Principal, Staff, Student, Teacher

# Register your models here.
admin.site.register(User)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Principal)
admin.site.register(Staff)
admin.site.register(Admin)