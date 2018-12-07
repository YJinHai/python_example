# coding=utf-8
from celery import Celery
app = Celery('app', include=['tasks'])
app.config_from_object('config')


if __name__ == '__main__':
    app.start()