from .models import Comment
from django import forms
from .models import Subscriber

# Forms below


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        labels = {
            'body': '',
        }
        widgets = {
            'body': forms.Textarea(
                attrs={'placeholder': 'Enter your comment here...'}
            ),
        }


class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['email']
        widgets = {
            'email': forms.EmailInput(
                attrs={'placeholder': 'Enter your email to subscribe...'}
            ),
        }
