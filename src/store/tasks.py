from celery import Celery

app = Celery('tasks', broker='pyamqp://guest@localhost//')

app = Celery('src.store')

app.conig_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

@app.task
def add(x, y):
    return print(x + y)
