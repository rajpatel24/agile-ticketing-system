from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    date_hierarchy = ('date_joined')
    list_display = ('id', 'name', 'email', 'date_joined', 'update_date', 'is_active')
    search_fields = ['title', 'status']


admin.site.register(User, UserAdmin)
