from rest_framework import routers
from .api import CLienteViewSet, TipoClienteViewSet, MunicipioViewSet, DepartamentoViewSet, DireccionViewSet

router=routers.DefaultRouter()

router.register('api/cliente', CLienteViewSet, 'cliente-api') 
router.register('api/tipocliente', TipoClienteViewSet, 'tipocliente-api')
router.register('api/municipio', MunicipioViewSet, 'municipio-api')
router.register('api/departamento', DepartamentoViewSet, 'depatamento-api')
router.register('api/direccion', DireccionViewSet, 'direccion-api')

urlpatterns =router.urls
