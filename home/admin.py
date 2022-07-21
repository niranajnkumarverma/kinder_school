from django.contrib import admin
from home.models import  Contact, User

# Register your models here.
admin.site.register(User)

admin.site.register(Contact)