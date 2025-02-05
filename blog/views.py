from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.contrib import messages
from .models import Post
from django.core.mail import send_mail
from django.conf import settings
from .models import Subscriber
from .forms import CommentForm
from .forms import SubscriptionForm


# Create your views here.

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1)
    template_name = "blog/index.html"
    paginate_by = 6


def post_detail(request, slug):
    """
    Display an individual :model:`blog.Post`.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.

    **Template:**

    :template:`blog/post_detail.html`
    """

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
            )
            # Send email notifications to subscribers
            subscribers = Subscriber.objects.all()
            for subscriber in subscribers:
                send_mail(
                    'New Blog Post Published',
                    (
                        f'A new blog post: "{post.title}" has been published. '
                        'Check it out at '
                        f'{request.build_absolute_uri(post.get_absolute_url())}'
                        ),
                    settings.DEFAULT_FROM_EMAIL,
                    [subscriber.email],
                    [subscriber.email],
                )

    comment_form = CommentForm()

    return render(
        request,
        "blog/post_detail.html",
        {
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
        }
    )


def subscribe(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'You have successfully subscribed to email updates.'
            )
            return redirect('home')
    else:
        form = SubscriptionForm()
    return render(request, 'blog/subscribe.html', {'form': form})
