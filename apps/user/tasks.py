from __future__ import absolute_import, unicode_literals
from celery import shared_task,task
from django.core.mail import send_mail

from arryblog import settings

@task
def send_email(subject,content,sender):
	recipients = ['me@zezo.cc']
	send_mail(subject,content,sender,recipients)

@task
def send_active_email(subject,receiver,content):
	'''异步发送邮件'''
	message = ''
	sender = settings.EMAIL_FROM
	send_mail(subject,
				message, 
				sender,
				receiver,
				html_message=content)

@task
def generate_user_activity():
	from user.models import Activity
	Activity.fake_activity(days=1)