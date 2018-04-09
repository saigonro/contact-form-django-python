from django.conf.urls import url, include
from django.contrib import admin
from home.views import index
from contactform import urls as urls_contactform

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name="index"),
    url(r'^contactform/', include(urls_contactform)),
]
