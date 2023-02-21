from django.db import models

# Create your models here.
class StockList(models.Model):
    # stock_id = models.CharField(max_length=16,verbose_name='stock_id')
    stock_name = models.CharField(max_length=16,verbose_name='stock_name')
    current_price = models.IntegerField(verbose_name='current_price')
    high_rate = models.IntegerField(verbose_name='high_rate')
    trading_volume = models.IntegerField(verbose_name='trading_volume')
    category = models.CharField(max_length=16,verbose_name='category')

    earn = models.IntegerField(verbose_name='earn')
    earn_rate = models.FloatField(verbose_name='earn_rate')
    info = models.CharField(max_length=256,verbose_name='info')
    profit1 = models.FloatField(verbose_name='profit1')
    profit2 = models.FloatField(verbose_name='profit2')
    profit3 = models.FloatField(verbose_name='profit3')
    profit4 = models.FloatField(verbose_name='profit4')
    target_price = models.FloatField(verbose_name='target_price')

    class Meta:
        db_table ="stock_list"
        verbose_name="주식리스트"
        verbose_name_plural ="주식리스트"


