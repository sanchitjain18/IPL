from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('js/', views.js, name="js"),
    path('match/', views.match_details, name="match_details")
]
