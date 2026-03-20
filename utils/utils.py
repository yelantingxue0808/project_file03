import requests
import time
from lxml import etree
from config import settings

# 请求url并获取数据
def send_url(url_):
    request = requests.get(url_, headers=settings.HEADERS)
    # print(request.text)
    data_html = request.text
    time.sleep(0.2)
    return parse_data(data_html)

# 解析请求的数据
def parse_data(data_html):
    # 使用xpath提取数据
    tree = etree.HTML(data_html, parser=None)
    name = tree.xpath('//div[@class="price-list"]/table/thead/tr/td[1]/text()')[0]
    specification = tree.xpath('//div[@class="price-list"]/table/thead/tr/td[2]/span/text()')[0]
    market = tree.xpath('//div[@class="price-list"]/table/thead/tr/td[3]/span/text()')[0]
    price = tree.xpath('//div[@class="price-list"]/table/thead/tr/td[4]/span/text()')[0]
    trend = tree.xpath('//div[@class="price-list"]/table/thead/tr/td[5]/text()')[0]
    week = tree.xpath('//div[@class="price-list"]/table/thead/tr/td[6]/span/text()')[0]
    mon = tree.xpath('//div[@class="price-list"]/table/thead/tr/td[7]/span/text()')[0]
    year = tree.xpath('//div[@class="price-list"]/table/thead/tr/td[8]/span/text()')[0]
    tr_lis = tree.xpath('//div[@class="price-list"]/table/tbody/tr')
    market_list = []
    for tr in tr_lis:
        # 创建一个字典
        market_dict = dict()
        td_text = []
        td_lis = tr.xpath('./td[position()<9]')
        for index, td in enumerate(td_lis):
            if index == 0:
                td_text.append(td.xpath('./a/text()')[0])
            elif index == 1:
                td_text.append(td.xpath('./a/text()')[0])
            else:
                td_text.append(td.xpath('./text()')[0])
        market_dict[name] = td_text[0]
        market_dict[specification] = td_text[1]
        market_dict[market] = td_text[2]
        market_dict[price] = td_text[3]
        market_dict[trend] = td_text[4]
        market_dict[week] = td_text[5]
        market_dict[mon] = td_text[6]
        market_dict[year] = td_text[7]
        market_list.append(market_dict)
        time.sleep(0.1)
    print(f'url抓取完成')
    # print(market_list)
    return market_list
