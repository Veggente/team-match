from django.conf.urls import url
from django.contrib.auth.views import logout_then_login


from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^create_user/$', views.create_user, name='create_user'),
    url(r'^calendar/$', views.calendar, name='calendar'),
    url(r'^auth/$', views.auth, name='auth'),
    url(r'^facultyconfig/$', views.facultyconfig, name='facultyconfig'),
]
