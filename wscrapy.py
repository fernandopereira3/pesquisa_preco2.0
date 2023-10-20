import csv
import datetime
import requests
import parsel
# from rocketry import Rocketry
# from rocketry.conds import (minutely, secondly)

# app = Rocketry(config={'task_execution': 'async'})

# @app.task(secondly)
def produto_1():  # IMAC M1
    req = requests.get("https://www.zoom.com.br/search?q=imac%20m1")
    sel = parsel.Selector(text=req.text)
    title = sel.xpath(
        '//h2[@class="Text_Text__h_AF6 Text_MobileLabelXs__ER_cD Text_DesktopLabelSAtLarge__baj_g ProductCard_ProductCard_Name__LT7hv"][1]//text()').get()
    price = sel.xpath('//p[@class="Text_Text__h_AF6 Text_MobileHeadingS__Zxam2"]//text()').get()
    return [title, price]

# @app.task(secondly)
def produto_2():  # TV 65"
    req = requests.get(
        "https://www.zoom.com.br/search?q=tv%2065%20polegadas%204k&hitsPerPage=24&page=1&sortBy=price_asc&isDealsPage=false&enableRefinementsSuggestions=true")
    sel = parsel.Selector(text=req.text)
    title = sel.xpath(
        '//h2[@class="Text_Text__h_AF6 Text_MobileLabelXs__ER_cD Text_DesktopLabelSAtLarge__baj_g ProductCard_ProductCard_Name__LT7hv"][1]//text()').get()
    price = sel.xpath('//p[@class="Text_Text__h_AF6 Text_MobileHeadingS__Zxam2"]//text()').get()
    link = sel.xpath(
        '//h3[@class="Text_Text__h_AF6 Text_MobileLabelXs__ER_cD Text_MobileLabelSAtLarge__YdYbv ProductCard_ProductCard_BestMerchant__AuGU6"]//text()').get()
    return [title, price, link]

# @app.task(minutely)
def organizador():
    pro1 = produto_1()
    pro2 = produto_2()
    now = datetime.datetime.now()
    time = now.strftime("%d/%m/%Y as %H:%M ")
    with open('dados.txt', 'a') as arquivo:
        arquivo.write("Produto: " + str(pro2[0]) + " PRECO: " + str(pro2[1]) + '\n')
        arquivo.write("Melhor site: "+ str(pro2[2]) + '\n')
    arquivo.close()


main = organizador()

