#from django.urls import path
#from . import views
from rest_framework import routers
from .api import AgenteViewSet, AseguradoViewSet, ClienteViewSet, PolizaViewSet, Estado_PolizaViewSet, Tipo_PolizaViewSet, AseguradoraViewSet


router = routers.SimpleRouter()

router.register(r'API/Agente', AgenteViewSet, 'app')
router.register(r'API/Cliente', ClienteViewSet, 'app')
router.register(r'API/Asegurado', AseguradoViewSet, 'app')
router.register(r'API/Aseguradora', AseguradoraViewSet, 'app')
router.register(r'API/Poliza', PolizaViewSet, 'app')
router.register(r'API/Estado_Poliza', Estado_PolizaViewSet, 'app')
router.register(r'API/Tipo_Poliza', Tipo_PolizaViewSet, 'app')

urlpatterns = router.urls

