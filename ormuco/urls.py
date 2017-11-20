from django.conf.urls import url

from . import views

app_name = "ormuco"
urlpatterns = [
    url(r'^post$', views.post, name='post'),
    url(r'^$', views.index, name='index'),
    url(r'^(?P<post_id>[0-9]+)/$', views.detail, name='detail'),
]
