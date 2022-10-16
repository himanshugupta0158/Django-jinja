from django.urls import path
from .views import index, post, sendEmailCode

urlpatterns = [
    path("<int:n>", index, name="index"),
    path("post", post, name="post"),
    path("mail/", sendEmailCode, name="mail"),

]
