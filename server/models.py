from django.db import models

# Create your models here.

class OnlineServer(models.Model):
    """Download Task Server"""
    def __str__(self):
        return "Server %d - %s" % (self.server_type, self.server_uid,)
    server_type = models.IntegerField(default=0, db_index=True)
    server_uid = models.CharField(max_length=80, db_index=True)
    server_name = models.CharField(max_length=255, default='')
    start_date = models.DateTimeField()
    update_date = models.DateTimeField()
    current_download = models.IntegerField(default=0)
    finish_count = models.IntegerField(default=0)
    error_count = models.IntegerField(default=0)
