# accounts/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import UserProfile


class UserProfileInline(admin.StackedInline):
    """Hiển thị Profile trong trang User Admin"""
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'Hồ sơ'


class UserAdmin(BaseUserAdmin):
    """Tùy chỉnh User Admin để hiển thị Profile"""
    inlines = (UserProfileInline,)
    list_display = ('username', 'email', 'first_name', 'last_name', 'get_role', 'is_staff')
    
    def get_role(self, obj):
        if hasattr(obj, 'profile'):
            return obj.profile.get_role_display()
        return '-'
    get_role.short_description = 'Vai trò'


# Đăng ký lại User với UserAdmin tùy chỉnh
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
