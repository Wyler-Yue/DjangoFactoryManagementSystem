from django.contrib import admin
from . import models
# Register your models here.
from .models import MyUser
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
@admin.register(MyUser)
class MyUserAdmin(UserAdmin):
    list_display = ['username','email','mobilenumber', 'is_staff', 'is_active', 'is_superuser']
    # 新增用户时，在个人信息里添加'mobilenumber','qq','weChat'的信息录入
    # 将源码的UserAdmin.fieldsets转换成列表格式
    fieldsets = list(UserAdmin.fieldsets)
    # 重写UserAdmin的fieldsets，添加'mobilenumber','qq','weChat'的信息录入
    fieldsets[1] = (_('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'mobilenumber')})
