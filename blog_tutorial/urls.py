from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^http://copelandia.pythonanywhere.com/', admin.site.urls),
    url(r'', include('blog.urls')),

]
