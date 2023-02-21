from django.contrib import admin
from .models import StockList

# Register your models here.

@admin.register(StockList)
class StockListAdmin(admin.ModelAdmin):
    pass


