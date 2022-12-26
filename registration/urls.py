from django.urls import path

from .views import RegisterCreateView, SignInView


urlpatterns = [
    path('signup/', RegisterCreateView.as_view(), name='signup'),
    path('signin/', SignInView.as_view(), name='signin'),
]
