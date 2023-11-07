from django.urls import re_path
from blogs import views

urlpatterns = [
    re_path(r'^blog/$', views.home, name='home'),
    re_path(r'^about/$', views.about, name='about'),
    re_path(r'^contact/$', views.contact, name='contact'),
    re_path(r'^article/(?P<article_id>[0-9]+)/$', views.show_article, name='article'),
]