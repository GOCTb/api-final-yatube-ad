from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.exceptions import InvalidToken
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView


class CustomTokenRefreshView(TokenRefreshView):
    """Переопределяем сообщение об ошибке для refresh."""
    def post(self, request, *args, **kwargs):
        try:
            return super().post(request, *args, **kwargs)
        except InvalidToken:
            return Response(
                {
                    'detail': 'Token is invalid or expired',
                    'code': 'token_not_valid'
                },
                status=status.HTTP_401_UNAUTHORIZED
            )


class CustomTokenVerifyView(TokenVerifyView):
    """Переопределяем сообщение об ошибке для verify."""
    def post(self, request, *args, **kwargs):
        try:
            return super().post(request, *args, **kwargs)
        except InvalidToken:
            return Response(
                {
                    'detail': 'Token is invalid or expired',
                    'code': 'token_not_valid'
                },
                status=status.HTTP_401_UNAUTHORIZED
            )
