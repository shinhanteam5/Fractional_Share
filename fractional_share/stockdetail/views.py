from rest_framework import mixins, generics,status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import StockDetail,News
from holdingstock.models import HoldingStock
from portfolio.models import Portfolio
from .serializers import StockDetailSerializer,BuyStockSerializer,NewsSerializer
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

    stockdetail = StockDetail.objects.filter(stock_code=stock_code).order_by('id')
    if stockdetail.exists():
        return JsonResponse("이미있어서 POST안함",safe=False)

    if request.method == 'POST':
        if len(str(stock_code)) != 6:
            for _ in range(6 - len(str(stock_code))):
                stock_code = '0' + str(stock_code)

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
                profit2 = int(soup.select_one('#content > div.section.cop_analysis > div.sub_section > table > tbody > tr:nth-child(3) > td:nth-child(3)').get_text().strip().replace(",","")),
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
        news  = soup.select('#content > div.section.new_bbs > div.sub_section.news_section > ul > li')
        for news in news:
            a,b=news.get_text().replace("\n","").split("/")
            newsModel = News(
                    stock_code = stock_code,
                    content = a[:-2],
                    tstamp = a[-2:]+b
            )
            newsModel.save()



        return JsonResponse("OK",safe=False)
    return JsonResponse("OK",safe=False)
class BuyStockView(
    mixins.CreateModelMixin,
    generics.GenericAPIView
):
    serializer_class = BuyStockSerializer
    def get_queryset(self,request):
        return HoldingStock.objects.all().order_by('id')
        # stockdetail = StockDetail.objects.filter(stock_code=stock_code).order_by('id')
    def post(self,request,*args,**kwargs):

        check_stock = HoldingStock.objects.filter(stock_code=request.POST.get("stock_code"))
 
        if check_stock:

            check_stock[0].invest_amount+=int(request.POST.get("invest_amount"))-int(request.POST.get("invest_amount"))*0.01
            check_stock[0].save()
        else:

            self.create(request,args,kwargs)

        p = Portfolio.objects.get()
        p.total_invest += int(request.POST.get("invest_amount"))-int(request.POST.get("invest_amount"))*0.01
        p.save()
        return JsonResponse("성공",safe=False)
    

class NewsListView(
    mixins.ListModelMixin,
    generics.GenericAPIView

):
    serializer_class = NewsSerializer

    def get_queryset(self):
        stock_code = self.kwargs.get('pk')
				# 쿼리개선
        if stock_code:
            return News.objects.filter(stock_code=stock_code).order_by('-id') 
        return News.objects.none()

    def get(self, request, *args, **kwargs):
        return self.list(request, args, kwargs)
    
