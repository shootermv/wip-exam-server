from django.conf.urls import url

from app import views

urlpatterns = [
  url(r'^$', views.index, name='index'),
  url(r'^users/$', views.users, name='users'),
  url(r'^profile/$', views.profile, name='profile'),
]