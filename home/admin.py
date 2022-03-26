from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from home.forms import UserCreationForm
from home.models import User,Video,Image

class MyUserAdmin(UserAdmin):
    add_form = UserCreationForm
    model = User
    list_display = ['username', 'email']
 


admin.site.register(User, MyUserAdmin)
admin.site.register(Video)
admin.site.register(Image)

