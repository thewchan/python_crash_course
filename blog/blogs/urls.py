"""Defines URL patterns for learning_logs."""

from django.urls import path

from . import views


app_name = 'blogs'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Page that shows all blog posts.
    path('blogposts/', views.blogposts, name='blogposts'),
    # Page that show text of a blog post.
    path('blogposts/<int:blogpost_id>/', views.blogpost, name='blogpost'),
    # Page for adding a new blog post.
    path('new_blogpost/', views.new_blogpost, name='new_blogpost'),
    # Page for editing a blog post.
    path(
        'edit_blogpost/<int:blogpost_id>/',
        views.edit_blogpost,
        name='edit_blogpost',
        )
]
