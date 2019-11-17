from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseAdminUser

from core import models

# Register your models here.


class AdminUser(BaseAdminUser):
    ordering = ['id']
    list_display = ['email', 'name']


admin.site.register(models.User, AdminUser)
