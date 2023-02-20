from django.contrib import admin
from .models import StockDetail

# Register your models here.

@admin.register(StockDetail)
class StockDetailAdmin(admin.ModelAdmin):
    pass