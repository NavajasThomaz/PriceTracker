from zenrows import ZenRowsClient




def terabyte():
    client = ZenRowsClient("023c5b438407dc890018789c2e5671632af20ae0")
    url = "https://www.terabyteshop.com.br/busca?str="
    params = {"js_render":"true","antibot":"true"}

    response = client.get(url, params=params)

    print(response.text)