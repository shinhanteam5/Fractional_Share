from rest_framework import mixins, generics,status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import StockDetail
from holdingstock.models import HoldingStock
from portfolio.models import Portfolio
from .serializers import StockDetailSerializer,BuyStockSerializer
from django.http.response import JsonResponse
from bs4 import BeautifulSoup
import requests
class StockDetailView(
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    generics.GenericAPIView,
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
):
    serializer_class=StockDetailSerializer

    def get_queryset(self):
        stock_code = self.kwargs.get('pk')
        return StockDetail.objects.filter(stock_code=stock_code).order_by('id')
#
    def get(self,request,*args,**kwargs):
        return self.list(request,args,kwargs)


def submit(request,stock_code):
    # if not request.user.is_authenticated:
    #     return redirect('/member/login/')
    print(request.POST.get("clpr"))
    if request.method == 'POST':
        url = 'https://finance.naver.com/item/main.naver?code='+str(stock_code)
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')

        stockdetail = StockDetail(
                stock_code =  stock_code,
                current_price =request.POST.get("clpr"),
                name =request.POST.get("itmsNm"),
                earn = request.POST.get("vs"),
                earn_rate =request.POST.get("fltRt"),
                info =soup.select_one('#summary_info').get_text(),
                profit1 = int(soup.select_one('#content > div.section.cop_analysis > div.sub_section > table > tbody > tr:nth-child(3) > td:nth-child(2)').get_text().strip().replace(",","")),
                profit2 = int(soup.select_one('#content > div.section.cop_analysis > div.sub_section > table > tbody > tr:nth-child(3) > td:nth-child(3) > em').get_text().strip().replace(",","")),
                profit3 =int(soup.select_one('#content > div.section.cop_analysis > div.sub_section > table > tbody > tr:nth-child(3) > td:nth-child(4)').get_text().strip().replace(",","")),
                sales1 = int(soup.select_one('#content > div.section.cop_analysis > div.sub_section > table > tbody > tr:nth-child(1) > td:nth-child(2)').get_text().strip().replace(",","")),
                sales2 = int(soup.select_one('#content > div.section.cop_analysis > div.sub_section > table > tbody > tr:nth-child(1) > td:nth-child(3)').get_text().strip().replace(",","")),
                sales3 = int(soup.select_one('#content > div.section.cop_analysis > div.sub_section > table > tbody > tr:nth-child(1) > td:nth-child(4)').get_text().strip().replace(",","")),
                week = 'https://ssl.pstatic.net/imgfinance/chart/item/area/week/'+str(stock_code)+'.png?sidcode=1676905742196',
                month3 = 'https://ssl.pstatic.net/imgfinance/chart/item/area/month3/'+str(stock_code)+'.png?sidcode=1676905742196',
                year = 'https://ssl.pstatic.net/imgfinance/chart/item/area/year/'+str(stock_code)+'.png?sidcode=1676905742196',
                year3 = 'https://ssl.pstatic.net/imgfinance/chart/item/area/year3/'+str(stock_code)+'.png?sidcode=1676905742196',
        )
        # print(product.id) # 에러!
        stockdetail.save()
        return JsonResponse("OK",safe=False)
    return JsonResponse("OK",safe=False)
class BuyStockView(
    mixins.CreateModelMixin,
    generics.GenericAPIView
):
    serializer_class = BuyStockSerializer
    def get_queryset(self):
        return HoldingStock.objects.all().order_by('id')
    def post(self,request,*args,**kwargs):
        print(request.POST.get("invest_amount"))
        a = self.create(request,args,kwargs)
        p = Portfolio.objects.get()
        p.total_invest += int(request.POST.get("invest_amount"))
        p.save()
        return a