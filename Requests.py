from zenrows import ZenRowsClient


# Funções de chamada da API
def terabyte(lista_produtos):
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