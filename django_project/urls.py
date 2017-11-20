from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^ormuco/', include('ormuco.urls', namespace="ormuco")),
    url(r'^admin/', admin.site.urls),
]
