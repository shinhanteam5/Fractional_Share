from rest_framework.views import APIView
from rest_framework.response import Response

class MyAPIView(APIView):
    def get(self, request):
        data = {'message': 'Hello, world!'}
        return Response(data)