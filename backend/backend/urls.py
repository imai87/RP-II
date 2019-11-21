"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework_mongoengine import routers

from carteira.views import AtualViewSet, AtivosViewSet

router = routers.DefaultRouter()
router.register(
    'atual', AtualViewSet, base_name='atual',
)
router.register(
    'ativos', AtivosViewSet, basename='ativos'
)
#router.register(
 #   'historico/(?P<stock>[a-z0-9]+)/$', HistoricoViewSet, basename='historico'
#)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
