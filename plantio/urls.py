from django.urls import path
from django.conf.urls import include

from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/area/', include('area.urls')),
    path('api/v1/especie/', include('especie.urls')),
    path('api/v1/familia/', include('familia.urls')),
    path('api/v1/ciclo/', include('ciclo.urls')),
    path('api/v1/manejo/', include('manejo.urls')),
]
