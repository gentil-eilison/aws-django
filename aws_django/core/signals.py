from celery.signals import task_failure, task_prerun, task_success

from .models import CeleryCompletedTasks


@task_failure.connect
def update_task_fail_status(task_id, *args, **kwargs):
    task = CeleryCompletedTasks.objects.get(task_id=task_id)
    task.status = CeleryCompletedTasks.Status.FAILED
    task.save()


@task_success.connect
def update_task_success_status(result, *args, **kwargs):
    task_id = kwargs.get("sender").request.id
    task = CeleryCompletedTasks.objects.get(task_id=task_id)
    task.status = CeleryCompletedTasks.Status.SUCCESS
    task.message = result
    task.save()


@task_prerun.connect
def create_task_model(task_id, task, *args, **kwargs):
    task_message = task.request.args[0]
    CeleryCompletedTasks.objects.create(
        message=task_message, status=CeleryCompletedTasks.Status.PROCESSING, task_id=task_id
    )
