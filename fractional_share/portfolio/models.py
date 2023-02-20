from django.db import models

# Create your models here.
class Portfolio(models.Model):
    # stock_id = models.CharField(max_length=16,verbose_name='stock_id')
    total_invest = models.IntegerField(verbose_name='total_invest')
    total_rate = models.IntegerField(verbose_name='total_rate')
    total_earn = models.IntegerField(verbose_name='total_earn')


    class Meta:
        db_table ="portfolio"
        verbose_name="포트폴리오"
        verbose_name_plural ="포트폴리오"