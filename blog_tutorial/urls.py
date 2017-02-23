from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^http://copelandia.pythonanywhere.com/', admin.site.urls),
    url(r'', include('blog.urls')),

]
