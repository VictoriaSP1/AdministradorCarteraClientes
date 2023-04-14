#from django.urls import path
#from . import views
from rest_framework import routers
from .api import AgenteViewSet

router = routers.DefaultRouter()

router.register('api/Agente', AgenteViewSet, 'app')

urlpatterns = router.urls

