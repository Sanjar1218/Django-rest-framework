from django.contrib import admin
from django.urls import path
from api.views import echo, getting

urlpatterns = [
    path('', echo, name='echo'),
    path('home/', getting, name='echo'),
    path('admin/', admin.site.urls),
]
