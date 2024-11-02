from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_spectacular.utils import extend_schema
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer
from .serializers import ErrorNotAuthorizedSerializer


class CreateTokenPairView(TokenObtainPairView):
    @extend_schema(
        summary='Create a new token pair from credentials',
        description='Takes a set of user credentials and returns an access and refresh JSON web token pair to prove the authentication of those credentials.',
        responses={
            200: TokenObtainPairSerializer,
            401: ErrorNotAuthorizedSerializer,
        }
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class CreateAccessTokenView(TokenRefreshView):
    @extend_schema(
        summary='Create a new access token from a refresh token',
        description='Takes a refresh type JSON web token and returns a new access JSON web token if the refresh token is valid.',
        responses={
            200: TokenRefreshSerializer,
            401: ErrorNotAuthorizedSerializer,
        }
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
