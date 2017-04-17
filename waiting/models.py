from django.db import models

# Create your models here.

class WaitingTask(models.Model):
    """Download Task"""
    def __str__(self):
        return "WAIT_TASK %d - %d" % (self.task_type, self.task_server,)
    task_type = models.IntegerField(default=0, db_index=True)
    task_server = models.IntegerField(default=0, db_index=True)
    task_start_date = models.DateTimeField()
    task_update_date = models.DateTimeField()
    task_wait_confirm = models.BooleanField()
    task_url = models.CharField(max_length=2048)
    task_addon_type = models.IntegerField(default=0)
    task_addon_bucket = models.CharField(max_length=255)
    task_addon_key = models.CharField(max_length=1024)
    task_addon_cookie = models.CharField(max_length=2048)
