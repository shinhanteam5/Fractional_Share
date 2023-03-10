from rest_framework import serializers
from .models import StockDetail,News
from holdingstock.models import HoldingStock
from portfolio.models import Portfolio
class StockDetailSerializer(serializers.ModelSerializer):
    # comment_count = serializers.SerializerMethodField();

    # def get_comment_count(self,obj):
    #     return obj.comment_set.all().count();

    class Meta:
        model = StockDetail
        fields = "__all__"

class BuyStockSerializer(serializers.ModelSerializer):
    def validate(self, attrs):
        attrs['member_id']=1
        attrs['invest_amount']=attrs['invest_amount']-attrs['invest_amount']*0.01
        # check_stock = HoldingStock.objects.filter(stock_code=attrs['stock_code']).order_by('id')
        # if check_stock.exists():
        #     raise serializers.ValidationError("member is required")
        return attrs
    class Meta:
        model = HoldingStock
        fields = "__all__"
        extra_kwargs={'member':{'required':False}}
class NewsSerializer(serializers.ModelSerializer):
    # product_name = serializers.SerializerMethodField()
    # member_username = serializers.SerializerMethodField()
    # tstamp = serializers.DateTimeField(
    #     read_only=True,format='%Y-%m-%d %H:%M:%S'
    # )
    class Meta:
        model = News
        fields = "__all__"