from django.urls import path
from .views import (
    PostListCreateView,
    PostRetrieveUpdateDestroyView,
    CommentListCreateView,
    UserRegistrationView,
)

urlpatterns = [
    path("posts/", PostListCreateView.as_view(), name="post-list-create"),
    path(
        "posts/<int:pk>/", PostRetrieveUpdateDestroyView.as_view(), name="post-detail"
    ),
    path(
        "posts/<int:post_pk>/comments/",
        CommentListCreateView.as_view(),
        name="comment-list-create",
    ),
    path("register/", UserRegistrationView.as_view(), name="user-registration"),
]
