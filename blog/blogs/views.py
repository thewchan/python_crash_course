from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import BlogPost
from .forms import BlogPostForm


# Create your views here.
def index(request):
    """The home page for your Blog."""
    return render(request, 'blogs/index.html')


def check_blockpost_owner(owner, user):
    if owner != user:
        raise Http404


@login_required
def blogposts(request):
    """Show all blog posts."""
    blogposts = (
        BlogPost.objects.filter(owner=request.user).order_by('date_added')
        )
    context = {'blogposts': blogposts}
    return render(request, 'blogs/blogposts.html', context)


@login_required
def blogpost(request, blogpost_id):
    """Show the text of a single blog post."""
    blogpost = BlogPost.objects.get(id=blogpost_id)
    check_blockpost_owner(blogpost.owner, request.user)
    texts = blogpost.text
    context = {'blogpost': blogpost, 'texts': texts}
    return render(request, 'blogs/blogpost.html', context)


@login_required
def new_blogpost(request):
    """Add a new blog post."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = BlogPostForm()
    else:
        # POST data submitted; process data.
        form = BlogPostForm(data=request.POST)
        if form.is_valid():
            new_blogpost = form.save(commit=False)
            new_blogpost.owner = request.user
            new_blogpost.save()
            return redirect('blogs:blogposts')
    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'blogs/new_blogpost.html', context)


@login_required
def edit_blogpost(request, blogpost_id):
    """Edit an existing blog post."""
    blogpost = BlogPost.objects.get(id=blogpost_id)
    check_blockpost_owner(blogpost.owner, request.user)

    if request.method != 'POST':
        # Initial request; pre-fill form with the current blog post.
        form = BlogPostForm(instance=blogpost)
    else:
        # POST data submitted; process data.
        form = BlogPostForm(instance=blogpost, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:blogpost', blogpost_id=blogpost.id)

    context = {'blogpost': blogpost, 'form': form}
    return render(request, 'blogs/edit_blogpost.html', context)
