from django.urls import path

from .import views

urlpatterns = [
    path("",views.starting_page, name="starting-page"),
    path("posts",views.posts, name="posts-page"),
    path("post/<slug:slug>",views.post_datail, name="post-detail-page") #/posts/my-first-post
]