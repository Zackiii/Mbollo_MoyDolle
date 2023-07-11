from django.contrib import admin
from .models import Aide
# Register your models here.


class AideAdmin(admin.ModelAdmin):
    list_display = ('category', 'user', 'support', 'IsArnaque')
    list_filter = ('support', 'IsArnaque', 'category')
    search_fields = ('user__username', 'context', 'category')

admin.site.register(Aide, AideAdmin)