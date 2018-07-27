from django.urls import path
from django.conf.urls import include

from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/area/', include('area.urls')),
    path('api/especie/', include('especie.urls')),
    path('api/familia/', include('familia.urls')),
]
