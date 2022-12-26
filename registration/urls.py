from django.urls import path

from .views import RegisterCreateView


urlpatterns = [
    path('signup/', RegisterCreateView.as_view(), name='signup'),
]
