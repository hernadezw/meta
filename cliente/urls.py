from rest_framework import routers
from .api import CLienteViewSet

router=routers.DefaultRouter()

router.register('api/cliente', CLienteViewSet, 'cliente-api')

urlpatterns =router.urls
