from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Member(AbstractUser):
    name = models.CharField(max_length=32,null=True,blank=True,verbose_name="name")
    tendency = models.CharField(max_length=32,null=True,blank=True,verbose_name="tendency")

    class Meta:
        db_table = "alpha_member"
        verbose_name ="회원"
        verbose_name_plural ="회원"