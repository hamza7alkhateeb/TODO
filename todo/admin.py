from django.contrib import admin
from .models import Task , Contact

# admin.site.register(Task)
# admin.site.register(Contact)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'is_complete', 'created_at')
    list_filter = ('is_complete', 'created_at')
    search_fields = ('title', 'description')



@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    search_fields = ('name', 'email')
