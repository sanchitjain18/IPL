from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('js/', views.js, name="js"),
]
