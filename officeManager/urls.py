from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^officemanager$', views.om),
]