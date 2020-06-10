from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('blog/', include('blog.urls')),
    path('about/', include('about.urls')),
]
