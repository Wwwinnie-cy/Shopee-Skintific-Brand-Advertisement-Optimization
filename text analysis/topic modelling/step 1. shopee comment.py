## 爬虫shoppe评论
import csv
import json
import random
import time
import uuid

import pandas as pd
import requests
from lxml import etree
from bs4 import BeautifulSoup
from openpyxl import Workbook


class Demo(object):

    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
            'cookie': 'SPC_SI=Z0dTZQAAAABaaG1KUmZaMP4jngAAAAAAOU4waXgyN2o=; SPC_SEC_SI=v1-M2I0QzA0UVBPMHB3SlhybyKyQ7g2rMTZiAN4t2F4xfYKst+GfkiauBrs7MwzIaIeMaTqGHahFc0BZyIZK1Nr+YQLhsDzlf7Z31bsZkoqvbU=; SPC_F=3J3N4IwXlhpobqVRQ26RCmb5ITXvMkFp; REC_T_ID=a7bd93ea-880e-11ee-bbe2-c6cd8e7090f7; csrftoken=DR2fRD5JBNRZAuSjDDh5jmzubjYDZzTP; _gcl_au=1.1.1112706426.1700530652; _fbp=fb.2.1700530652399.401358522; _QPWSDCXHZQA=99239cc4-6258-4a84-939b-2a6483e20e88; REC7iLP4Q=16bf540e-2833-437e-a1f1-b4bb4d1f157f; _gid=GA1.3.2252408.1700530697; SPC_CLIENTID=M0ozTjRJd1hsaHBvzyjekrfvxpezpjaq; SPC_ST=.ZmJFaWpaN1JNOHV5cnR2UUqMyqtMr4QJiYfWIqtT/eJo9YWvmQYw44en4lkrOjLO9qKWxb1xeJZwqSP32caFapCwKPlJMgs7gA7LoGykLg3a0lf4DKPnRAkDTOzgaZLyMR58b9h99gcPj4XC1aZfQ/dA6Dv8WtfBj2FmSo+iQD/tio46yHBYsPdMBp4sMVydDKqP7UwYUA5zklDSP0ikrg==; SPC_U=1122995562; SPC_R_T_ID=HQC6H7GWEnAS46Qu0kea8SawOYQTX7xUVF5wsFkhIvxAzkMlvpajCHZrXTai6emT6q90cC/vwM1H89V/txBKM8Xt+i172oZ4LVKC2P8ym8V7I1FSO199cmmPS6BOnPDZYPdSfaO91fNOsOfeeVxbstIHFw/F+mkGaH5xi7H4u6w=; SPC_R_T_IV=dkd1elBjc2ZIRUtmU3FaNg==; SPC_T_ID=HQC6H7GWEnAS46Qu0kea8SawOYQTX7xUVF5wsFkhIvxAzkMlvpajCHZrXTai6emT6q90cC/vwM1H89V/txBKM8Xt+i172oZ4LVKC2P8ym8V7I1FSO199cmmPS6BOnPDZYPdSfaO91fNOsOfeeVxbstIHFw/F+mkGaH5xi7H4u6w=; SPC_T_IV=dkd1elBjc2ZIRUtmU3FaNg==; shopee_webUnique_ccd=I%2B1XzpHJbZheHGdUCQY8Hg%3D%3D%7CizaUQPekBWJxzrqkHLjhh8BoLmP4taFly4MyZ0GVwiuI4k28l9z91DGHGHhq6Am6IzYw4Yx2IPtcCrw%3D%7CoHY%2B2eh0BuWtH%2Fcg%7C08%7C3; ds=f8618b60c016e93256ab351174c5b1da; _ga=GA1.3.1546192389.1700530653; _ga_SW6D8G0HXK=GS1.1.1700530653.1.1.1700530796.60.0.0; SPC_EC=a05SUjhTRzJjVjRLdE1YemAoaUOPPeo0OAOkLnD+krQ1jeySewIZQCsneKFwmrvcx2d0hP4UaBK9gvL4kyiPNN5MynJd4GcoXZT3mdZ/twZbukdS+QZLApPb3AEhN+ksaEYVCsbmjwWGPC6gwS19JZ6GODrsGDI0IojwHGoDCDA=',
            'Af-Ac-Enc-Sz-Token': 'I+1XzpHJbZheHGdUCQY8Hg==|izaUQPekBWJxzrqkHLjhh8BoLmP4taFly4MyZ0GVwiuI4k28l9z91DGHGHhq6Am6IzYw4Yx2IPtcCrw=|oHY+2eh0BuWtH/cg|08|3',
            # ''
        }
        self.dataslist = []


    def get_data(self):
        """ 获取数据并解析解析 """
        offset = 0  # 下标
        while True:
            # https://shopee.co.id/-Tasya-Farasya-Approved-SKINTIFIC-5X-Ceramide-Skin-Barrier-Moisturize-Gel-30g-Moisturizer-Cream-Pemutih-Wajah-Day-Cream-Night-Cream-Pelembab-Wajah-i.457706720.11242593437?sp_atk=ee4146bb-e0a3-4870-8f94-1c230adbc28e&xptdk=ee4146bb-e0a3-4870-8f94-1c230adbc28e
            # url = 'https://shopee.co.id/api/v2/item/get_ratings?exclude_filter=1&filter=0&filter_size=0&flag=1&fold_filter=0&itemid=11242593437&limit=6&offset=' + \
            #       str(offset) + '&relevant_reviews=false&request_source=2&shopid=457706720&tag_filter=&type=0&variation_filters='

            # https://shopee.co.id/-Tasya-Farasya-Approved-SKINTIFIC-MSH-Niacinamide-Brightening-Moisturizer-Glowing-Moisture-Gel-30g-Cream-Pemutih-Wajah-i.457706720.17486965055?sp_atk=d22e3af7-0756-4c0d-9689-75b9b00bcafb&xptdk=d22e3af7-0756-4c0d-9689-75b9b00bcafb
            # url = 'https://shopee.co.id/api/v2/item/get_ratings?exclude_filter=1&filter=0&filter_size=0&flag=1&fold_filter=0&itemid=17486965055&limit=6&offset=' + \
            #       str(offset) + '&relevant_reviews=false&request_source=2&shopid=457706720&tag_filter=&type=0&variation_filters='

            # https://shopee.co.id/-TASYA-FARASYA-APPROVED-SOMETHINC-Calm-Down!-Skinpair-R-Cover-Cream-Moisturizer-(Madagascar-Centella-Asiatica-Skin-Barrier-Kulit-Sensitif-Kulit-Iritasi)-i.195455930.23824435470?sp_atk=f330a038-f9c3-4dd1-be1b-cb0aa3bdc270&xptdk=f330a038-f9c3-4dd1-be1b-cb0aa3bdc270
            url = 'https://shopee.co.id/api/v2/item/get_ratings?exclude_filter=1&filter=0&filter_size=0&flag=1&fold_filter=0&itemid=23824435470&limit=6&offset=' + \
                  str(offset) + '&relevant_reviews=false&request_source=2&shopid=195455930&tag_filter=&type=0&variation_filters='

            print('offset: ', offset, ' url: ', url)
            response = requests.get(url, headers=self.headers)
            print(response.text)

            r_dict = json.loads(response.text)

            if r_dict.get('data').get('ratings') is None:
                print('没有更多评论，结束程序...')
                break

            for rd in r_dict.get('data').get('ratings'):
                data = {}
                comment = rd.get('comment').split('\n')  # 评论内容分割
                data['内容'] = comment
                print(data)

                # with open('json/comment_11242593437.json', 'a', encoding='utf8') as f:
                #     f.write(json.dumps(data, ensure_ascii=False) + ',\n')

                # with open('json/comment_17486965055.json', 'a', encoding='utf8') as f:
                #     f.write(json.dumps(data, ensure_ascii=False) + ',\n')

                with open('json/comment_23824435470.json', 'a', encoding='utf8') as f:
                    f.write(json.dumps(data, ensure_ascii=False) + ',\n')

            offset += 6  # 每次加载6条评论

            time.sleep(random.randint(2, 3))

    def save(self):
        with open('json/comment_23824435470.json', 'r', encoding='utf-8') as f:
            json_data = f.read()
        datajson = json_data[0:-2]
        datajson = '[' + datajson + ']'
        datalist = json.loads(datajson)

        wb = Workbook()
        sheet = wb.active

        sheet['a1'] = '评论内容'

        if datalist is not None:
            for i in range(len(datalist)):

                comment = ''
                for j in datalist[i].get('内容'):
                    if j != '':
                        comment += j + '\n'

                sheet.cell(row=(i + 2), column=1).value = comment

            wb.save('excel/comment_23824435470.xlsx')
            wb.close()

    def run(self):
        # self.get_data()
        self.save()


if __name__ == '__main__':
    zy = Demo()
    zy.run()