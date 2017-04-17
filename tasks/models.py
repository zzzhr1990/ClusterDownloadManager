from django.db import models

# Create your models here.

class DownloadTask(models.Model):
    """Download Task"""
    def __str__(self):
        return "TASK %d - %s" % (self.task_type, self.task_server,)
    task_type = models.IntegerField(default=0, db_index=True)
    task_server = models.CharField(max_length=80, db_index=True)
    task_server_name = models.CharField(max_length=255, default='')
    task_start_date = models.DateTimeField()
    task_update_date = models.DateTimeField()
    task_progress = models.IntegerField(default=0)
    task_status = models.IntegerField(default=0, db_index=True)
    task_type = models.IntegerField(default=0, db_index=True)
