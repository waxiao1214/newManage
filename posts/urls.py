from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomePageViewPost.as_view(), name = "home"),
]
