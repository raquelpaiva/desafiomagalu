from django.contrib import admin
from django.urls import path, include 
from django.conf import settings
from django.conf.urls.static import static
from produtos import urls as produtos_urls
from clientes import urls as clientes_urls


urlpatterns = [
    path('clientes/', include(clientes_urls)),
    path('produtos/', include(produtos_urls)),
    path('admin/', admin.site.urls),
  ]
