from django.urls import path

from .views import AlbumListView, CeleryCompletedTasksListView, create_celery_task

app_name = "core"
urlpatterns = [
    path("list/", AlbumListView.as_view(), name="list"),
    path("tasks/", CeleryCompletedTasksListView.as_view(), name="tasks"),
    path("celery_task/", create_celery_task, name="create-celery-task"),
]
