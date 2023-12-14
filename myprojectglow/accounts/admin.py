from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Registra tus modelos aquí.
admin.site.register(CustomUser, UserAdmin)

