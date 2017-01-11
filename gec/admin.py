from django.contrib import admin
from .models import Departement

@admin.register(Departement)
class DepartementModelAdmin(admin.ModelAdmin):

    list_display = ('name', 'description')

    search_fields = ('name',)
