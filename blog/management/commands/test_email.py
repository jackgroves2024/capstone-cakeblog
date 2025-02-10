from django.core.mail import send_mail
from django.core.management.base import BaseCommand

# This command is used to test the email configuration.


class Command(BaseCommand):
    help = 'Test email configuration'

    def handle(self, *args, **kwargs):
        send_mail(
            'Test Email',
            'This is a test email.',
            'capstonecakeblogtest@gmail.com',
            ['jackgroves2@outlook.com'],
            fail_silently=False,
        )
        self.stdout.write(self.style.SUCCESS('Test email sent successfully'))
