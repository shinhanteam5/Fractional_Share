from django.db import models
# Create your models here.
class StockDetail(models.Model):

    name=models.CharField(max_length=128, verbose_name='stock_name')
    stock_code =  models.IntegerField(verbose_name='stock_code')
    current_price = models.DecimalField(max_digits=7, decimal_places=2,verbose_name='current_price')
    earn = models.DecimalField(max_digits=7, decimal_places=2,verbose_name='earn')
    earn_rate = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='earn_rate')
    info = models.CharField(max_length=256,verbose_name='info')
    profit1 = models.DecimalField(max_digits=7, decimal_places=2,verbose_name='profit1')
    profit2 = models.DecimalField(max_digits=7, decimal_places=2,verbose_name='profit2')
    profit3 = models.DecimalField(max_digits=7, decimal_places=2,verbose_name='profit3')
    
    sales1 = models.DecimalField(max_digits=7, decimal_places=2,verbose_name='sales1')
    sales2 = models.DecimalField(max_digits=7, decimal_places=2,verbose_name='sales2')
    sales3 = models.DecimalField(max_digits=7, decimal_places=2,verbose_name='sales3')

    week = models.CharField(max_length=256,verbose_name='week')
    month3 = models.CharField(max_length=256,verbose_name='month3')
    year = models.CharField(max_length=256,verbose_name='year')
    year3 = models.CharField(max_length=256,verbose_name='year3')

    class Meta:
        db_table ="stock_detail"
        verbose_name="주식상세리스트"
        verbose_name_plural ="주식상세리스트"

class Comment(models.Model):
    stock = models.ForeignKey(StockDetail,on_delete=models.CASCADE,verbose_name="상품")
    content = models.TextField(verbose_name='뉴스 제목')
    tstamp = models.DateTimeField(auto_now_add=True,verbose_name="등록일시")
    
    class Meta:
        db_table = "news"
        verbose_name="뉴스"
        verbose_name_plural = "뉴스"