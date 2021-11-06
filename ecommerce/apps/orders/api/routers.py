from rest_framework.routers import DefaultRouter
from apps.orders.api.views import OrderViewSet

router = DefaultRouter()

router.register('',OrderViewSet, basename='orders')

urlpatterns= router.urls