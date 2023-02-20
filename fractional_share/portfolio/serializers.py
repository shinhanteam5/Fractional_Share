from rest_framework import serializers
from .models import Portfolio
from holdingstock.models import HoldingStock

class PortfolioSerializer(serializers.ModelSerializer):

    # stock_name = serializers.SerializerMethodField()
    # # stock_share = serializers.SerializerMethodField()
    # def get_stock_name(self,obj):
    #     return obj.holdingstock.stock_name
    class Meta:
        model = Portfolio
        fields = "__all__"