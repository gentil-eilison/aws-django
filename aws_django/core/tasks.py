import time

from celery import shared_task


@shared_task
def add(x, y):
    return f"Message sent: {x+y}"


@shared_task
def lowercase_string(string):
    time.sleep(10)
    return string.lower()
