# coding=utf-8
BROKER_URL = 'redis://127.0.0.1:6379/1'
CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/0'
CELERY_TASK_SERIALIZER = 'msgpack'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_RESULT_EXPIRES = 60 * 60 * 24
CELERY_ACCEPT_CONTENT = ['json', 'msgpack']

CELERY_TIMEZONE = 'Asia/Shanghai'

from datetime import timedelta

# CELERYBEAT_SCHEDULE = {
#     'send-every-30-seconds': {
#         'task': 'tasks.sendmail',
#         #'schedule': timedelta(seconds=30),
#         'args': (dict(to='windard@windard.com'), )
#     }
# }


from kombu import Queue
CELERY_QUEUES = (
    Queue('default', routing_key='task.#'),
    Queue('web_tasks', routing_key='web.#'),
)


