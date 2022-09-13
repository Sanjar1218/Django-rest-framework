from django.contrib import admin
from django.urls import path
from api.views import echo

urlpatterns = [
    path('', echo, name='echo'),
    path('admin/', admin.site.urls),
]
