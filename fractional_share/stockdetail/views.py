from rest_framework import mixins, generics,status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import StockDetail
from holdingstock.models import HoldingStock
from .serializers import StockDetailSerializer,BuyStockSerializer
from django.http.response import JsonResponse
class StockDetailView(
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    generics.GenericAPIView,
):
    serializer_class=StockDetailSerializer

    def get_queryset(self):
        return StockDetail.objects.all().order_by('id')

    def get(self,request,*args,**kwargs):
        return self.retrieve(request,args,kwargs)

    def delete(self,request,*args,**kwargs):
        return self.destroy(request,args,kwargs)

    def put(self,request,*args,**kwargs):
        return self.partial_update(request,args,kwargs)


def buy(request):
    # if not request.user.is_authenticated:
    #     return redirect('/member/login/')

    if request.method == 'POST':
        holdingstock = HoldingStock(
            # member=request.POST.get("member"),
            # portfolio_id=request.POST.get("portfolio_id"),
            # stock_name=request.POST.get("stock_name"),
            # stock_share=request.POST.get("stock_share"),
            # invest_amount=request.POST.get("location"),
            # earn_rate=request.POST.get("location"),

            member=1,
            portfolio_id=1,
            stock_name="helo",
            stock_share=0.1,
            invest_amount=1000,
            earn_rate=0.1,

        )
        # print(product.id) # 에러!
        holdingstock.save()
        return JsonResponse("ok")

class BuyStockView(
    mixins.CreateModelMixin,
    generics.GenericAPIView
):
    serializer_class = BuyStockSerializer
    def get_queryset(self):
        return HoldingStock.objects.all().order_by('id')
    def post(self,request,*args,**kwargs):
        return self.create(request,args,kwargs)
