from django.conf.urls import url

from app import views

urlpatterns = [
  url(r'^users/$', views.users, name='users'),
  url(r'^statuses/$', views.statuses, name='statuses'),
  url(r'^profile/$', views.profile, name='profile'),
]