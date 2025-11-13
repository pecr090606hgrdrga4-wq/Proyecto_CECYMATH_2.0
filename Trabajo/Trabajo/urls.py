from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('suma/', include('suma.urls')),
    path('resta/', include('resta.urls')),
    path('multiplicacion/', include('multiplicacion.urls')),
    path('division/', include('division.urls')),
    path('jerarquia/', include('jerarquia.urls')),
    path('recta/', include('recta.urls')),
    path('polinomios/', include('polinomios.urls')),
    path('ecuaciones1/', include('ecuaciones1.urls')),
    path('ecuaciones2/', include('ecuaciones2.urls')),
    path('factorizacion/', include('factorizacion.urls')),
    path('areas_perimetros/', include('areas_perimetros.urls')),
]
