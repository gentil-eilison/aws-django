from django.contrib import admin

from .models import Album, CeleryCompletedTasks

# Register your models here.
admin.site.register(Album)
admin.site.register(CeleryCompletedTasks)
