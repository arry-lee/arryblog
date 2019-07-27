import django
from django.dispatch import receiver,Signal
from django.core.mail import EmailMultiAlternatives

send_email_signal = Signal(providing_args=['emailto', 'title', 'content'])

@receiver(send_email_signal)
def send_email_signal_handler(sender, **kwargs):
	emailto = kwargs['emailto']
    title = kwargs['title']
    content = kwargs['content']
    msg = EmailMultiAlternatives(title, content, from_email=settings.DEFAULT_FROM_EMAIL, to=emailto)
    msg.content_subtype = "html"

    try:
        result = msg.send()

    except Exception as e:
        pass



