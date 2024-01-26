from django.contrib import admin

# Register your models here.

# User.objects.create_superuser(username="admin", full_name="adminadmin", password="Admin@123", email = "admin@admin.com")
from authentication.models import UserData, Role
admin.site.register(UserData)
admin.site.register(Role)
