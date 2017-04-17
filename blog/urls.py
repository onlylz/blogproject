from django.conf.urls import url
from . import views, details
app_name = 'blog'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^post/(?P<pk>[0-9]+)/$', details.detail, name='detail'),
]