from rest_framework import mixins, generics,status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import StockList
from .serializers import (
    StockListSerializer)

class StockListView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView
):

    serializer_class = StockListSerializer


    def get_queryset(self):
        return  StockList.objects.all().order_by('id')

    def get(self,request,*args,**kwargs):
        print(request.user)
        return self.list(request,args,kwargs)
    def post(self,request,*args,**kwargs):
        return self.create(request,args,kwargs)
