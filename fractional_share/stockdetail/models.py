from django.db import models
# Create your models here.
class StockDetail(models.Model):
    # stock_id = models.CharField(max_length=16,verbose_name='stock_id')
    stock_id = models.ForeignKey('stocklist.StockList',on_delete=models.CASCADE,verbose_name="주식아이디")
    current_price = models.IntegerField(verbose_name='current_price')
    earn = models.IntegerField(verbose_name='earn')
    earn_rate = models.IntegerField(verbose_name='earn_rate')
    info = models.CharField(max_length=256,verbose_name='info')
    profit1 = models.IntegerField(verbose_name='profit1')
    profit2 = models.IntegerField(verbose_name='profit2')
    profit3 = models.IntegerField(verbose_name='profit3')
    profit4 = models.IntegerField(verbose_name='profit4')
    target_price = models.IntegerField(verbose_name='target_price')

    class Meta:
        db_table ="stock_detail"
        verbose_name="주식상세리스트"
        verbose_name_plural ="주식상세리스트"