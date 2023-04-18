#from django.urls import path
#from . import views
from rest_framework import routers
from .api import AgenteViewSet, AseguradoViewSet, ClienteViewSet, PolizaViewSet, Estado_PolizaViewSet, Tipo_PolizaViewSet, AseguradoraViewSet


router = routers.SimpleRouter()

router.register(r'api/agente', AgenteViewSet, 'app')
router.register(r'api/agente/<char:Password>', AgenteViewSet, 'app')
router.register(r'api/cliente', ClienteViewSet, 'app')
router.register(r'api/asegurado', AseguradoViewSet, 'app')
router.register(r'api/aseguradora', AseguradoraViewSet, 'app')
router.register(r'api/poliza', PolizaViewSet, 'app')
router.register(r'api/estado_poliza', Estado_PolizaViewSet, 'app')
router.register(r'api/tipo_poliza', Tipo_PolizaViewSet, 'app')

urlpatterns = router.urls

