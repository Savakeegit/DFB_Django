from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from users.models.users import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    change_user_password_template = None
    fieldsets = (
        (None, {'fields': ( 'username',)}),
        (_('Личная информация'),
         {'fields': ('first_name', 'last_name',)}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'phone_number', 'password1', 'password2',),
        }),
    )
    list_display = ('telegram_id', 'username',)

    list_display_links = ('telegram_id',)
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('username', 'first_name', 'last_name', 'telegram_id', )
    ordering = ('-telegram_id',)
    filter_horizontal = ('groups', 'user_permissions',)
    readonly_fields = ('last_login', )