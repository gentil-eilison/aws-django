from celery import shared_task
# from aws_django.core.models import Album
# import time
# import timedef run_job(product_id):
# 	update_field.delay(product_id)@shared_task
# def update_field(product_id):
@shared_task
def add(x, y):
    return f"Message sent: {x+y}"
