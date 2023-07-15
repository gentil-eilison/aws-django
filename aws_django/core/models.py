from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Album(models.Model):
    title = models.CharField(max_length=50)
    cover = models.ImageField()


class CeleryCompletedTasks(models.Model):
    class Status(models.TextChoices):
        SUCCESS = "OK", _("SUCCESS")
        FAILED = "FAILED", _("FAILED")
        PROCESSING = "PROCESSING", _("PROCESSING")

    message = models.CharField(max_length=100)
    status = models.CharField(choices=Status.choices)
    task_id = models.CharField(max_length=256)
