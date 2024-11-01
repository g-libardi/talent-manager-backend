from rest_framework.views import APIView, Response, Request
from rest_framework import status
from drf_spectacular.utils import extend_schema


class PingView(APIView):
    @extend_schema(
        summary='Ping endpoint',
        description='Use this endpoint to check if the API is running',
        responses={200: {'message': 'pong'}},
    )
    def get(self, _: Request):
        return Response({'message': 'pong'}, status=status.HTTP_200_OK)
