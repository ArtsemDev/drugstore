from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import ProductViewSet

api_router = SimpleRouter()
api_router.register(r'products', ProductViewSet)


urlpatterns = [
    path('', include(api_router.urls))
]
