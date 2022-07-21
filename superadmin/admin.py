from django.contrib import admin
from .models import  AdminProfileModel,FooterBackground, HeaderBackground,  Image, Logo, Notification, Title, Video

# Register your models here.
admin.site.register(AdminProfileModel)
admin.site.register(Video)
admin.site.register(Notification)
admin.site.register(Image)
admin.site.register(Logo)
admin.site.register(Title)
admin.site.register(HeaderBackground)
admin.site.register(FooterBackground)