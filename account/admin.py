from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserModelAdmin(UserAdmin):
    model = CustomUser
    list_display = [field.name for field in CustomUser._meta.fields]
    list_filter = ["is_superuser"]
    search_fields = ["user_name"]
    ordering = ["user_name", "id"]
    fieldsets = (
        (None, {'fields': ('user_name', 'password')}),
        ('Personal Info', {'fields': ('role',)}),
        ('Permissions', {'fields': (
            'is_active',
            'is_staff',
            'is_superuser',
            'groups',
            'user_permissions',
        )}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'user_name',
                'password1',
                'password2',
                'role',
                'is_staff',
                'is_superuser',
            ),
        }),
    )

    filter_horizontal = ['groups', 'user_permissions']

admin.site.register(CustomUser, CustomUserModelAdmin)