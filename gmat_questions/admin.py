from django.contrib import admin
from .models import Questions, Choices
# Register your models here.

@admin.register(Questions, Choices)
class PersonAdmin(admin.ModelAdmin):
    pass