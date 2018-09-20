from django.contrib import admin

# Register your models here.
from .models import ToDoList


@admin.register(ToDoList)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ('content', 'set_time')
    pass

