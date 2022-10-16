from django.urls import path
from .views import index, post

urlpatterns = [
    path("<int:n>", index, name="index"),
    path("post", post, name="post"),

]
