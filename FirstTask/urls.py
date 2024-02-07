from django.urls import path
from .views import task
from .views import home
from .views import url
urlpatterns = [
    path('',home,name="home"),
    path('url/',url,name='url'),
     path('url/task/', task, name='task'),
     path('url/task/home/', home, name='Rhome'),
     path('url/task/url/', url, name='Rurl'),
]