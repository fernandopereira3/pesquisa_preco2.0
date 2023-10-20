import datetime
import requests
import parsel
import smtplib
import email.message

def produto_1():  # IMAC M1
    req = requests.get("https://www.zoom.com.br/search?q=imac%20m1")
    sel = parsel.Selector(text=req.text)
    title = sel.xpath('//*[@id="product-card-12484406::name"]//text()').get()
    price = sel.xpath('//*[@id="__next"]/div/div[7]/div[1]/a/div[2]/div[2]/div[2]/p[1]//text()').get()
    link = sel.xpath('//*[@id="__next"]/div/div[7]/div[1]/a/div[2]/div[2]/div[2]/h3//text()').get()
    return title, price, link

def produto_2():  # TV 65"
    req = requests.get("https://www.zoom.com.br/search?q=tv%2065%20polegadas%204k&hitsPerPage=24&page=1&sortBy=price_asc&isDealsPage=false&enableRefinementsSuggestions=true", headers={'USER_AGENT': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'})
    sel = parsel.Selector(text=req.text)
    title = sel.xpath('//*[@id="product-card-12484406::name"]//text()').get()
    price = sel.xpath('//*[@id="__next"]/div/div[7]/div[1]/a/div[2]/div[2]/div[2]/p[1]//text()').get()
    link = sel.xpath('//*[@id="__next"]/div/div[7]/div[1]/a/div[2]/div[2]/div[2]/h3//text()').get()
    return title, price, link

def organizador():
    pro1 = produto_1()
    pro2 = produto_2()
    now = datetime.datetime.now()
    time = now.strftime("%d/%m/%Y as %H:%M ")
    with open('tv.txt', 'a') as tv:
        tv.write(' ' + '\n')
        tv.write("Produto: " + str(pro2[0]) + " PRECO: " + str(pro2[1]) + '\n')
        tv.write("Em "+ time +" - "+ str(pro2[2]) + '\n')
    tv.close()

def enviar():
    pro = produto_2()
    corpo = str("PRODUTO: " + pro[0] + " PRECO: " + pro[1] + " LOJA: " + pro[2])
    msg = email.message.Message()
    msg['Subject'] = "ROBO"
    msg['From'] = 'sap.fernando.pereira@gmail.com'
    msg['to'] = 'fernandopereira-3@hotmail.com', ''
    password = "ilwvhquhfxbjthex"
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo)
    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    s.login(msg['From'], password)
    s.sendmail(msg['From'], msg['to'], msg.as_string().encode('utf-8'))


main = organizador()
mail = enviar()
