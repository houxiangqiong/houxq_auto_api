import random

import allure
import requests
from config.conf import API_URL


@allure.feature("商品模块")
@allure.story("商品价格")
@allure.title("根据产品编码修改商品价格")
def test_rechange(db):
    with allure.step("获取数据库"):
        prodCodes = db.select_execute("select product_code from `t_prod_product` where status = '0' and product_code is not null")
        prodCode = random.choice(prodCodes)[0]
    with allure.step("准备数据"):
        data = {
            'price': '1999',
            'prodCode': prodCode
         }
    with allure.step("发送请求"):
        r = requests.post(API_URL+"/product/changePriceByProdCode",json=data)



    with allure.step("获取请求内容"):
        allure.attach(str(r.request.url),"请求url",allure.attachment_type.TEXT)
        allure.attach(str(r.request.headers), "请求headers", allure.attachment_type.TEXT)
        allure.attach(str(r.request.body), "请求body", allure.attachment_type.TEXT)

    with allure.step("获取响应内容"):
        allure.attach(str(r.headers), "响应headers", allure.attachment_type.TEXT)
        allure.attach(str(r.text), "响应文本", allure.attachment_type.TEXT)
