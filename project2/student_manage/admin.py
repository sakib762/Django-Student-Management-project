from django.contrib import admin
from .models import Student
@admin.register(Student)
class studentAdmin((admin.ModelAdmin)):
    list_display = [fields.name for fields in Student._meta.fields]
# Register your models here.
