import os
import sys
import django

# setup
path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(path)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "fractional_share.settings")
django.setup()

# django 사용 가능

from random import randint,choice
from stocklist.models import StockList
from faker import Faker
# from django_seed import Seed


for i in range(10):
            stock = StockList(
                # stock_id=randint(1,10000000),
                stock_name=Faker("ko_KR").name(),
                current_price=randint(1000,1000000),
                high_rate=randint(1,100),
                trading_volume=randint(10000,100000),
                category=choice(['a','b','c'])
                )
        # print(product.id) # 에러!
            stock.save()
