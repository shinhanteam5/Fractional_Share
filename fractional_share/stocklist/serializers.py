from rest_framework import serializers
from .models import StockList

class StockListSerializer(serializers.ModelSerializer):
    # comment_count = serializers.SerializerMethodField();

    # def get_comment_count(self,obj):
    #     return obj.comment_set.all().count();

    class Meta:
        model = StockList
        fields = "__all__"
