from django.urls import path
from . import views
urlpatterns=[
    path("get_data", views.get_data, name="get_data"),
    path("", views.home2, name="home2"),
    
]
