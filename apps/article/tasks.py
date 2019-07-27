from __future__ import absolute_import, unicode_literals
from celery import shared_task,task
import time


@task
def test():
	print('hello......')
	time.sleep(2)
	print('world......')


@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)