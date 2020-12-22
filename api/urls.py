from django.urls import path, include
from rest_framework import routers
from .views import MonkeyViewSet

router = routers.DefaultRouter()
router.register('monkey', MonkeyViewSet)

urlpatterns = [
  path('', include(router.urls))
]

