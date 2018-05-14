from django.contrib import admin
from .models import Profile


@admin.register(Profile)
class AdminAccount(admin.ModelAdmin):
    list_display = ['user', 'phone_number', 'address']
