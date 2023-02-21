from django.contrib import admin
from .models import StockDetail,News

# Register your models here.

@admin.register(StockDetail)
class StockDetailAdmin(admin.ModelAdmin):
    pass
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    pass
