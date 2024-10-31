from rest_framework.views import APIView, Response, Request
from rest_framework import status

# Create your views here.
class PingView(APIView):
    '''
    Health check endpoint
    '''
    def get(self, _: Request):
        return Response({'message': 'pong'}, status=status.HTTP_200_OK)
