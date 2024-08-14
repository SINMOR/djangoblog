from django.urls import path , include
from . import views

urlpatterns = [
    path("", views.home, name="blog-home"),  #make sure the naming is specific so as not to collide with other app 
    path("about/", views.about, name="blog-about"),  #make sure the naming is specific so as not to collide with other app 
]
