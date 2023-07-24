from django.contrib import admin
from .models import *


# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('username','is_association', 'is_demandeur', 'is_admin')


admin.site.register(User, UserAdmin)


class DemandeurAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'address', 'number')
    search_fields = ('full_name', 'number', 'address')


admin.site.register(Demandeur, DemandeurAdmin)


class AssociationAdmin(admin.ModelAdmin):
    list_display = ('user', 'email', 'numero', 'address', 'category')
    list_filter = ('category', 'address')
    search_fields = ('user__username', 'email', 'numero')


admin.site.register(Association, AssociationAdmin)


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)


class SubCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(SubCategory, SubCategoryAdmin)
