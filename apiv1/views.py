from datetime import datetime, timedelta

import pytz
from django.conf import settings
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly, SAFE_METHODS
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authentication import TokenAuthentication

from main.models import Product, Category
from .serializers import ProductSerializer, CategorySerializer


class ExpiredTokenAuthentication(TokenAuthentication):

    def authenticate_credentials(self, key):
        user, token = super().authenticate_credentials(key=key)
        utc_now = datetime.utcnow()
        utc_now = utc_now.replace(tzinfo=pytz.utc)
        if token.created < utc_now - timedelta(minutes=settings.TOKEN_EXPIRE):
            raise AuthenticationFailed('token has expired')
        return user, token


class IsAdminOrReadOnly(IsAuthenticatedOrReadOnly):

    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS or
            request.user and
            request.user.is_authenticated and
            request.user.is_staff
        )


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.filter(is_published=True)
    serializer_class = ProductSerializer
    permission_classes = [IsAdminOrReadOnly]
    authentication_classes = [ExpiredTokenAuthentication]


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.filter(is_published=True)
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]
    authentication_classes = [ExpiredTokenAuthentication]


class AuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        Token.objects.filter(user=user).delete()
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})
