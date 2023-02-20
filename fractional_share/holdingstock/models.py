from django.db import models
from django.contrib.auth.models import Portfolio
# Create your models here.
class HoldingStock(models.Model):
    portfolio_id = models.ForeignKey(Portfolio,on_delete=models.CASCADE,verbose_name="포트폴리오명")
    stock_name=models.CharField(max_length=128, verbose_name='stock_name')
    stock_share = models.IntegerField(verbose_name='stock_share')
    invest_amount = models.IntegerField(verbose_name='invest_amount')
    earn_rate = models.IntegerField(verbose_name='earn_rate')


    class Meta:
        db_table ="holdingstock"
        verbose_name="보유주식"
        verbose_name_plural ="보유주식"