from zenrows import ZenRowsClient
import bd

lista_produtos = []
for produto in bd.Produtos:
    lista_produtos.append(bd.Produtos[produto]["titulo"])

print(lista_produtos)
# Funções de chamada da API
def terabyte(lista_produtos):
    client = ZenRowsClient("023c5b438407dc890018789c2e5671632af20ae0")
    url = "https://www.terabyteshop.com.br/busca?str="
    params = {"js_render":"true","antibot":"true"}

    response1 = client.get(url+lista_produtos[0], params=params)
    print("1")
    response2 = client.get(url+lista_produtos[1], params=params)
    print("2")
    response3 = client.get(url+lista_produtos[2], params=params)
    print("3 ...")
    response4 = client.get(url+lista_produtos[3], params=params)
    response5 = client.get(url+lista_produtos[4], params=params)
    response6 = client.get(url+lista_produtos[5], params=params)
    response7 = client.get(url+lista_produtos[6], params=params)
    print("... 7")
    response8 = client.get(url+lista_produtos[7], params=params)
    print("8")

    bd = open('bd\produtos.txt', "w")
    bd.write(f"{[response1.text]}, {[response2.text]}, {[response3.text]}, {[response4.text]}, {[response5.text]}, {[response6.text]}, {[response7.text]}, {[response8.text]}")
    bd.close()

    #print(response.text)

terabyte(lista_produtos)


def pichau(lista_produtos):
    client = ZenRowsClient("023c5b438407dc890018789c2e5671632af20ae0")
    url = "https://www.terabyteshop.com.br/busca?str="
    params = {"js_render":"true","antibot":"true"}

    response1 = client.get(url+lista_produtos[0], params=params)
    response2 = client.get(url+lista_produtos[1], params=params)
    response3 = client.get(url+lista_produtos[2], params=params)
    response4 = client.get(url+lista_produtos[3], params=params)
    response5 = client.get(url+lista_produtos[4], params=params)
    response6 = client.get(url+lista_produtos[5], params=params)
    response7 = client.get(url+lista_produtos[6], params=params)
    response8 = client.get(url+lista_produtos[7], params=params)


    #print(response.text)

def kabum(lista_produtos):
    client = ZenRowsClient("023c5b438407dc890018789c2e5671632af20ae0")
    url = "https://www.terabyteshop.com.br/busca?str="
    params = {"js_render":"true","antibot":"true"}

    response1 = client.get(url+lista_produtos[0], params=params)
    response2 = client.get(url+lista_produtos[1], params=params)
    response3 = client.get(url+lista_produtos[2], params=params)
    response4 = client.get(url+lista_produtos[3], params=params)
    response5 = client.get(url+lista_produtos[4], params=params)
    response6 = client.get(url+lista_produtos[5], params=params)
    response7 = client.get(url+lista_produtos[6], params=params)
    response8 = client.get(url+lista_produtos[7], params=params)


    #print(response.text)