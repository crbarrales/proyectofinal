
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^mascota/', include('mascota.urls', namespace='mascota')),
    url(r'^adopcion/', include('adopcion.urls', namespace='adopcion')),

]
