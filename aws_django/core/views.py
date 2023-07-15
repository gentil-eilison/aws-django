from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import ListView

from .models import Album, CeleryCompletedTasks
from .tasks import lowercase_string


# Create your views here.
class AlbumListView(ListView):
    model = Album

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)


class CeleryCompletedTasksListView(ListView):
    model = CeleryCompletedTasks


def create_celery_task(request):
    task_message = request.POST.get("task_message")
    lowercase_string.delay(task_message)
    return redirect(reverse("albums:tasks"))
