from rest_framework import serializers
from .models import Portfolio
from holdingstock.models import HoldingStock

class PortfolioSerializer(serializers.ModelSerializer):

    stocks = serializers.SerializerMethodField()

    def get_stocks(self, obj):
        return [
            {
                'stock_name': s.stock_name,
                'stock_share': s.stock_share, 
                'invest_amount': s.invest_amount,
                'earn_rate': s.earn_rate,
            }
            for s in obj.holdingstock_set.all()
        ]
    class Meta:
        model = Portfolio
        fields = "__all__"