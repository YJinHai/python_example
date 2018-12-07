# coding=utf-8
import time

from celery.schedules import crontab
from celery.task import periodic_task

from app import app


@app.task
def sendmail(mail, queue='default'):
    print('sending mail to %s ...' % mail['to'])
    time.sleep(2)
    print('mail send.')
    return 'Send Successful!'


# @periodic_task(run_every=crontab(hour='16', minute='58'))
# def schedule_sendmail():
#     print('sending mail task')
#     time.sleep(2)
#     print('mail send.')
#     return 'Send Successful!'


@app.task
def add(x=4, y=4, queue='default'):
    print('x+y:%s ' % (x+y))
    return x + y

@app.task
def take(x=4, y=4, queue='web_tasks'):
    print('x-y:%s ' % (x-y))
    return x - y

@app.task
def no_argument():
    print('No Argument')
    return 'No Argument'


@app.task
def xsum(values):
    print('sum:', sum(values))
    return sum(values)
