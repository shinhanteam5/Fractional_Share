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
from stockdetail.models import StockDetail
from faker import Faker
# from django_seed import Seed
lst=["삼성전자","HLB","비보존제약","카카오","LG디스플레이","에스맥",
     "SK증권","코오롱인더우","인포뱅크","현대차","스킨앤스킨","한국조선해양",
     "디딤이앤에프","에스엠","NAVER","POSCO홀딩스"
     ]

for i in range(len(lst)):
            stock = StockList(
                # stock_id=randint(1,10000000),
                stock_name=lst[i],
                current_price=randint(1000,1000000),
                high_rate=randint(1,100),
                trading_volume=randint(10000,100000),
                category=choice(['a','b','c']),

                earn = randint(1,100),
                earn_rate = randint(1,100),
                info = "안녕하세요"+lst[i] +"입니다.",
                profit1 =randint(10000,100000),
                profit2 =randint(10000,100000),
                profit3 =randint(10000,100000),
                profit4 =randint(10000,100000),
                target_price = randint(10000,100000),

                )
            stock.save()
            # detail = StockDetail(
            #         stock_id=stock
            #         stock_name=lst[i],
            #         current_price=randint(1000,1000000),
            #         high_rate=randint(1,100),
            #     trading_volume=randint(10000,100000),
            #     category=choice(['a','b','c'])
            # )
        # print(product.id) # 에러!