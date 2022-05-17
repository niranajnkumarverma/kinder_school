from django.contrib import admin
from product.models import Author, Book,Publisher

# Register your models here.
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Publisher)


