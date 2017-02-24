from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^signup$', views.signup),
    url(r'^login$', views.login),
    url(r'^customermanager$', views.customermanager),
    url(r'^officemanager$', views.officemanager),
    url(r'^help$', views.helppage),
    url(r'contact$', views.contact),
]