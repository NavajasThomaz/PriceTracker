from zenrows import ZenRowsClient
import HtmlFinder
import bd
import requests
import json

lista_produtos = []
for produto in bd.Produtos:
    lista_produtos.append(bd.Produtos[produto]["titulo"])

print(lista_produtos)


# Funções de chamada da API
def terabyte(lista_produtos):
    url = "https://www.terabyteshop.com.br/busca?str="
    prod_dict = []

    params = {'api_key': 'BUILBW095PICODZ2EOBMN4NB4EPERMZLVFZ1CLADUITMZRKZL3RG0R988483OMDX8K2NJ8YI9W65VG69'}

    responses = []
    for i in range(0, len(lista_produtos)):
        params['url'] = url + lista_produtos[i].replace(" ", "%20")
        responses.append(requests.get('https://app.scrapingbee.com/api/v1/', params=params))
        print(responses[i].status_code)

    for response in responses:
        if response.status_code == 200:
            prod_dict.append([response.text])

    with open('bd\TerabyteHtml.txt', "w", encoding="utf-8") as bd:
        #prod_dict = f"{[prod_dict]}, {[prod_dict]}, {[response3.text]}, {[response4.text]}, {[response5.text]}, {[response6.text]}, {[response7.text]}, {[response8.text]}"
        prod_dict = str(prod_dict)[2:-2]
        bd.write(str(prod_dict))
        bd.close()
    HtmlFinder.terabyteJson()




def pichau(lista_produtos):
    url = "https://www.pichau.com.br/search?q="
    prod_dict = []

    params = {'api_key': 'BUILBW095PICODZ2EOBMN4NB4EPERMZLVFZ1CLADUITMZRKZL3RG0R988483OMDX8K2NJ8YI9W65VG69'}

    responses = []
    for i in range(0, len(lista_produtos)):
        params['url'] = url + lista_produtos[i].replace(" ", "%20")
        responses.append(requests.get('https://app.scrapingbee.com/api/v1/', params=params))
        print(responses[i].status_code)

    for response in responses:
        if response.status_code == 200:
            prod_dict.append([response.text])

    with open('bd\PichauHtml.txt', "w", encoding="utf-8") as bd:
        #prod_dict = f"{[prod_dict]}, {[prod_dict]}, {[response3.text]}, {[response4.text]}, {[response5.text]}, {[response6.text]}, {[response7.text]}, {[response8.text]}"
        prod_dict = str(prod_dict)[2:-2]
        bd.write(str(prod_dict))
        bd.close()

    #HtmlFinder.pichauJson()

def kabum(lista_produtos):
    url = "https://www.kabum.com.br/busca/"
    prod_dict = []

    params = {'api_key': 'BUILBW095PICODZ2EOBMN4NB4EPERMZLVFZ1CLADUITMZRKZL3RG0R988483OMDX8K2NJ8YI9W65VG69'}

    responses = []
    for i in range(0, len(lista_produtos)):
        params['url'] = url + lista_produtos[i].replace(" ", "-")
        responses.append(requests.get('https://app.scrapingbee.com/api/v1/', params=params))
        print(responses[i].status_code)

    for response in responses:
        if response.status_code == 200:
            prod_dict.append([response.text])

    with open('bd\KabumHtml.txt', "w", encoding="utf-8") as bd:
        # prod_dict = f"{[prod_dict]}, {[prod_dict]}, {[response3.text]}, {[response4.text]}, {[response5.text]}, {[response6.text]}, {[response7.text]}, {[response8.text]}"
        prod_dict = str(prod_dict)[2:-2]
        bd.write(str(prod_dict))
        bd.close()
    #HtmlFinder.terabyteJson()





kabum(lista_produtos)