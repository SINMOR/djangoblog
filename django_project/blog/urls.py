from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="blog-home"),  #make sure the naming is specific so as not to colide with other app 
    path("about/", views.about, name="blog-about"),  #make sure the naming is specific so as not to colide with other app 
]
