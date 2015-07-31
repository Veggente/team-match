from django.conf.urls import url
from django.contrib.auth.views import logout_then_login

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
