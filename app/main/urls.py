from django.urls import path
from main import views


app_name = "main"
urlpatterns = [
    path("", views.index, name="index"),
    path("new/<slug:new_slug>", views.new, name="new"),
    path("info/", views.info, name="info")
]
