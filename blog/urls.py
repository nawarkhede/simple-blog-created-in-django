from django.urls import path
from .views import post_list, post_details

app_name = "blog"

urlpatterns = [
    path("", post_list, name="post_list"),
    path(
        "<int:year>/<int:month>/<int:day>/<slug:post>/",
        post_details,
        name="post_detail",
    ),
]