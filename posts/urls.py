from django.urls import path

from .views import HomePageView, DeletePostView

urlpatterns = [
    path("", HomePageView.as_view(), name="index"),
    path("post/<int:pk>/delete/", DeletePostView.as_view(), name="post_delete")
]
