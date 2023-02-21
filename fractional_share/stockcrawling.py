import requests
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/item/main.nhn?code=112040'

response = requests.get(url)

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    info = soup.select_one('#summary_info')

    current_price = soup.select_one('#middle > dl > dd:nth-child(6)')
    #당기순이익(억원)
    profit1 = soup.select_one('#content > div.section.cop_analysis > div.sub_section > table > tbody > tr:nth-child(3) > td:nth-child(2)')
    profit2 = soup.select_one('#content > div.section.cop_analysis > div.sub_section > table > tbody > tr:nth-child(3) > td:nth-child(3) > em')
    profit3 = soup.select_one('#content > div.section.cop_analysis > div.sub_section > table > tbody > tr:nth-child(3) > td:nth-child(4)')
    #매출액(억원)
    sales1  = soup.select_one('#content > div.section.cop_analysis > div.sub_section > table > tbody > tr:nth-child(1) > td:nth-child(2)')
    sales2  = soup.select_one('#content > div.section.cop_analysis > div.sub_section > table > tbody > tr:nth-child(1) > td:nth-child(3)')
    sales3  = soup.select_one('#content > div.section.cop_analysis > div.sub_section > table > tbody > tr:nth-child(1) > td:nth-child(4)')
    #뉴스
    news  = soup.select('#content > div.section.new_bbs > div.sub_section.news_section > ul > li')
    for news in news:
        print(news.get_text().replace("\n",":"))

    #차트
    week  = 'https://ssl.pstatic.net/imgfinance/chart/item/area/week/900110.png?sidcode=1676905742196'
    month3  = 'https://ssl.pstatic.net/imgfinance/chart/item/area/month3/900110.png?sidcode=1676905742196'
    year  = 'https://ssl.pstatic.net/imgfinance/chart/item/area/year/900110.png?sidcode=1676905742196'
    year3  = 'https://ssl.pstatic.net/imgfinance/chart/item/area/year3/900110.png?sidcode=1676905742196'

    # print(current_price.get_text())
    # print(info.get_text())
    # print(int(profit1.get_text()))
    # print(int(profit2.get_text()))
    print(profit3.get_text().strip())

    # print(int(sales1.get_text()))
    # print(int(sales2.get_text()))
    # print(int(sales3.get_text()))

else : 
    print(response.status_code)