from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.signup, name='Sign up') 
]
