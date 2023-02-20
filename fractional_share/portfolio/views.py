from rest_framework import mixins, generics,status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from holdingstock.models import HoldingStock
from .serializers import (
    PortfolioSerializer)
# from .paginations import ProductLargePagination

class PortfolioDetailView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView
):

    serializer_class = PortfolioSerializer
    # pagination_class = ProductLargePagination
    # permission_classes =[IsAuthenticated]

    def get_queryset(self):
        # portfolios = Portfolio.objects.all()
        # return portfolios.order_by('id')
        product_id = self.kwargs.get('pk')
				# 쿼리개선
        if product_id:
            return HoldingStock.objects.filter(portfolio_id=product_id).order_by('-id') 
        return HoldingStock.objects.none()

    def get(self,request,*args,**kwargs):
        return self.list(request,args,kwargs)
    def post(self,request,*args,**kwargs):
        return self.create(request,args,kwargs)
