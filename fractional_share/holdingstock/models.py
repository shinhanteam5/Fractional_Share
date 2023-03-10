from django.db import models
# Create your models here.
class HoldingStock(models.Model):
    member = models.ForeignKey('member.Member',on_delete=models.CASCADE,verbose_name="회원")
    portfolio_id = models.ForeignKey('portfolio.Portfolio',on_delete=models.CASCADE,verbose_name="포트폴리오명")
    stock_code=models.CharField(max_length=128, verbose_name='stock_code')
    stock_name=models.CharField(max_length=128, verbose_name='stock_name')
    stock_share = models.FloatField(verbose_name='stock_share')
    invest_amount = models.IntegerField(verbose_name='invest_amount')
    earn_rate = models.FloatField(verbose_name='earn_rate')


    class Meta:
        db_table ="holdingstock"
        verbose_name="보유주식"
        verbose_name_plural ="보유주식"