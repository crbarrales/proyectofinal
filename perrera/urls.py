
from django.conf.urls import url, include
from django.contrib import admin

from django.contrib.auth.views import login


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^mascota/', include('mascota.urls', namespace='mascota')),
    url(r'^adopcion/', include('adopcion.urls', namespace='adopcion')),
    url(r'^usuario/', include('usuario.urls', namespace='usuario')),
    url(r'^$', login, {'template_name':'index.html'}, name='login'),
    

]
