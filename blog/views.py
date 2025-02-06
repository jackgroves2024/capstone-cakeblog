import logging
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.contrib import messages
from .models import Post, Subscriber
from .forms import CommentForm, SubscriptionForm

# Set up logging
logger = logging.getLogger(__name__)

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


def unsubscribe(request, email):
    subscriber = get_object_or_404(Subscriber, email=email)
    if request.method == 'POST':
        subscriber.delete()
        messages.success(request, 'You have successfully unsubscribed from email updates.') # noqa
        return redirect('home')
    return render(request, 'blog/unsubscribe.html', {'subscriber': subscriber})
