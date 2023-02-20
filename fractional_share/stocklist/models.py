from django.db import models

# Create your models here.
class StockList(models.Model):
    # stock_id = models.CharField(max_length=16,verbose_name='stock_id')
    stock_name = models.CharField(max_length=16,verbose_name='stock_name')
    current_price = models.IntegerField(verbose_name='current_price')
    high_rate = models.IntegerField(verbose_name='high_rate')
    trading_volume = models.IntegerField(verbose_name='trading_volume')
    category = models.CharField(max_length=16,verbose_name='category')

    class Meta:
        db_table ="stock_list"
        verbose_name="주식리스트"
        verbose_name_plural ="주식리스트"


