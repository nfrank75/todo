# -- coding: UTF-8 --
from django.contrib.admin.sites import AlreadyRegistered

# from import_export import resources
from django.contrib import admin
from .models import Todo


class TodoAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
        'File',
        'complete'
        )
    fields = ('name', 'description', 'File', 'complete')
    search_fields = ('name', 'complete')



admin.site.register(Todo, TodoAdmin)