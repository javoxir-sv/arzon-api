from django.contrib import admin
from .models import *
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display=('title', 'slug')
    prepopulated_fields = {'slug' : ("title", "store",)}


admin.site.register(Product, ProductAdmin)
