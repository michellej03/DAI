# DAI/urls.py

from django.contrib import admin
from django.urls import path, include
from bawbab.views import verify, setup

urlpatterns = [
    path('admin/', admin.site.urls),
    path('verify/', verify, name='verify'),
    path('setup/', setup, name='setup'),
    
    
]
