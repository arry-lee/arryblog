from __future__ import absolute_import, unicode_literals
from celery import shared_task,task
from django.core.mail import send_mail

from arryblog import settings

@task
def send_a_email(message):
	subject = "LOG"
	sender =settings.EMAIL_FROM
	recipients = ['lixiaorui@seu.edu.cn']
	send_mail(subject,message,sender,recipients)

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