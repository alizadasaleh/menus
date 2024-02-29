from django.contrib import admin
from .models import MenuItem

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'menu_name', 'parent', 'url', 'name')
    list_filter = ('menu_name', 'parent') 
    search_fields = ['title', 'menu_name']
