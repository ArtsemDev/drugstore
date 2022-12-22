from django.urls import path

from .views import IndexTemplateView, ProductListView


urlpatterns = [
    path('', IndexTemplateView.as_view(), name='index'),
    path('products/', ProductListView.as_view(), name='products')
]
