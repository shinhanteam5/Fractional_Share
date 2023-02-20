from django.contrib import admin
from .models import HoldingStock

# Register your models here.

@admin.register(HoldingStock)
class HoldingStockAdmin(admin.ModelAdmin):
    pass