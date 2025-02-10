import logging
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse
from django.contrib.sites.models import Site
from .models import Post, Subscriber

# Set up logging
logger = logging.getLogger(__name__)


@receiver(post_save, sender=Post)
def send_new_post_email(sender, instance, created, **kwargs):
    if created and instance.status == 1:  # Status 1 means published
        current_site = Site.objects.get_current()
        domain = current_site.domain
        subscribers = Subscriber.objects.all()
        for subscriber in subscribers:
            try:
                post_url = f"http://{domain}{instance.get_absolute_url()}"
                unsubscribe_url = f"http://{domain}{reverse('unsubscribe', args=[subscriber.email])}"  # noqa
                send_mail(
                    'New Blog Post Published',
                    (
                        f'A new blog post: "{instance.title}" has been published. '  # noqa
                        f'Check it out at {post_url}\n\n'
                        f'If you wish to unsubscribe from these updates, click here: {unsubscribe_url}'  # noqa
                    ),
                    settings.DEFAULT_FROM_EMAIL,
                    [subscriber.email],
                )
                logger.info(f'Email sent to {subscriber.email}')
            except Exception as e:
                logger.error(f'Error sending email to {subscriber.email}: {e}')
