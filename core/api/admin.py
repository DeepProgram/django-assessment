from django.contrib import admin
from .models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'phone', 'created_at', 'is_superuser')
    search_fields = ('email', 'first_name', 'last_name')

admin.site.register(CustomUser, CustomUserAdmin)