import logging
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from .models import Post, Subscriber

# Set up logging
logger = logging.getLogger(__name__)


@receiver(post_save, sender=Post)
def send_new_post_email(sender, instance, created, **kwargs):
    if created and instance.status == 1:  # Assuming status 1 means published
        subscribers = Subscriber.objects.all()
        for subscriber in subscribers:
            try:
                send_mail(
                    'New Blog Post Published',
                    (
                        f'A new blog post: "{instance.title}" has been '
                        'published. '
                        'Check it out at '
                        f'{instance.get_absolute_url()}'
                    ),
                    settings.DEFAULT_FROM_EMAIL,
                    [subscriber.email],
                )
                logger.info(f'Email sent to {subscriber.email}')
            except Exception as e:
                logger.error(f'Error sending email to {subscriber.email}: {e}')
