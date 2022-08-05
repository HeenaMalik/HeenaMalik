from django.conf.urls import url
from Birthday_app import views

app_name = 'Birthday_app'

urlpatterns=[
    url(r'^relative/$', views.relative, name="relative"),
    url(r'^other/$', views.other, name="other"),
    url(r'^base/$', views.base, name="base"),
]
