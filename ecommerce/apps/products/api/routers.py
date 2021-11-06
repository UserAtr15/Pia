from rest_framework import urlpatterns
from rest_framework.routers import DefaultRouter
from apps.products.api.views.product_view import ProductViewSet
from apps.products.api.views.category_views import CategoryViewSet

router = DefaultRouter()

router.register(r'products', ProductViewSet, basename = 'products')
router.register(r'category',CategoryViewSet, basename = 'category')

urlpatterns = router.urls