
from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register("ibiteramo", IbiteramoViewset)
router.register("itike", ItikeViewset)

urlpatterns = [
    path('', include(router.urls)),
]
