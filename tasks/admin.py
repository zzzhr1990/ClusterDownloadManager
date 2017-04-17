from django.contrib import admin
from .models import DownloadTask
# Register your models here.
### Download Admin
class DownloadTaskAdmin(admin.ModelAdmin):
    """Display"""
    list_display = ['task_type', 'task_server', 'task_update_date', 'task_progress', 'task_status']
    search_fields = ['task_server']
admin.site.register(DownloadTask, DownloadTaskAdmin)
