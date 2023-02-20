from django.db import models

# Create your models here.
class Portfolio(models.Model):
    user_id = models.ForeignKey('member.Member',on_delete=models.CASCADE,verbose_name="포트폴리오명")
    total_invest = models.IntegerField(verbose_name='total_invest')
    total_rate = models.FloatField(verbose_name='total_rate')
    total_earn = models.IntegerField(verbose_name='total_earn')


    class Meta:
        db_table ="portfolio"
        verbose_name="포트폴리오"
        verbose_name_plural ="포트폴리오"