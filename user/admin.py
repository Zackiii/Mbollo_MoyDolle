from django.contrib import admin
from .models import *


# Register your models here.
admin.site.register(User)
admin.site.register(Association)
admin.site.register(Demandeur)


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)


class SubCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(SubCategory, SubCategoryAdmin)
