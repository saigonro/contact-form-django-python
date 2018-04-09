from django.conf.urls import url, include
from .views import *

urlpatterns = [
    url(r'^$', contactform, name='contactform'),
    url(r'^thanks/$', thanks, name='thanks'),
]