import datetime
import json
import unicodedata
from unidecode import unidecode
import bd as banco


def terabyteJson():
    prod_list = {
        f"{unicodedata.normalize('NFD', banco.Produtos[1]['titulo'].replace(' ', '')).encode('ascii', 'ignore').decode('utf-8')}": {},
        f"{unicodedata.normalize('NFD', banco.Produtos[2]['titulo'].replace(' ', '')).encode('ascii', 'ignore').decode('utf-8')}": {},
        f"{unicodedata.normalize('NFD', banco.Produtos[3]['titulo'].replace(' ', '')).encode('ascii', 'ignore').decode('utf-8')}": {},
        f"{unicodedata.normalize('NFD', banco.Produtos[4]['titulo'].replace(' ', '')).encode('ascii', 'ignore').decode('utf-8')}": {},
        f"{unicodedata.normalize('NFD', banco.Produtos[5]['titulo'].replace(' ', '')).encode('ascii', 'ignore').decode('utf-8')}": {},
        f"{unicodedata.normalize('NFD', banco.Produtos[6]['titulo'].replace(' ', '')).encode('ascii', 'ignore').decode('utf-8')}": {},
        f"{unicodedata.normalize('NFD', banco.Produtos[7]['titulo'].replace(' ', '')).encode('ascii', 'ignore').decode('utf-8')}": {},
        f"{unicodedata.normalize('NFD', banco.Produtos[8]['titulo'].replace(' ', '')).encode('ascii', 'ignore').decode('utf-8')}": {},

    }

    bd = open("bd/terabyteHtml.txt", "r", encoding="utf-8")
    htmls = bd.read().split("], [")

    for html in htmls:
        word = ""
        result = []

        # separador de HTML
        for l in html[2:-2]:
            word += l
            if l == ">":
                if word[1] == "n" or word[2] == "n":
                    result.append(word[2:])
                else:
                    result.append(word)
                word = ""

        count = 1
        for k in range(0, len(result)):
            if result[k][0:4] == "<img":
                img = result[k].split()[1][5:-1]
            elif result[k][1] == "a":
                line = result[k].split()
                if len(line) > 4 and line[1] == 'class="prod-name"':
                    nome = f"{line[3:][0][7:]} " + " ".join(line[4:-1]) + f" {line[-1][:-2]}"
                    link = line[2][6:-1]
                    if result[k + 5][:-7][5:19] == 'class="freteG"':
                        preco = result[k + 16][:-7]
                    elif result[k + 14][:-7][0] == "R":
                        preco = result[k + 14][:-7]
                    else:
                        preco = result[k + 11][:-7]
                    hist = [str(datetime.datetime.now())[0:10], preco]
                    prod_list[unicodedata.normalize('NFD', result[4][8:-19].replace(' ', '')).encode('ascii',
                                                                                                     'ignore').decode(
                        'utf-8')][count] = {
                        "Nome": unicodedata.normalize("NFD", nome).encode("ascii", "ignore").decode("utf-8"),
                        "Preco": preco, "Imagem": img, "Link": link, "Historico": hist}
                    count += 1
                    if count == 6:
                        break

    produtos_json = json.dumps(prod_list)
    with open(f"bd\produtosTERABYTE.json", "w") as arquivo_json:
        arquivo_json.write(produtos_json)


def pichauJson():
    prod_list = {
        f"{unidecode(banco.Produtos[1]['titulo'].replace(' ', ''))}": {},
        f"{unidecode(banco.Produtos[2]['titulo'].replace(' ', ''))}": {},
        f"{unidecode(banco.Produtos[3]['titulo'].replace(' ', ''))}": {},
        f"{unidecode(banco.Produtos[4]['titulo'].replace(' ', ''))}": {},
        f"{unidecode(banco.Produtos[5]['titulo'].replace(' ', ''))}": {},
        f"{unidecode(banco.Produtos[6]['titulo'].replace(' ', ''))}": {},
        f"{unidecode(banco.Produtos[7]['titulo'].replace(' ', ''))}": {},
        f"{unidecode(banco.Produtos[8]['titulo'].replace(' ', ''))}": {},


    }

    bd = open("bd/PichauHtml.txt", "r", encoding="utf-8")
    htmls = bd.read().split("], [")

    for html in htmls:
        word = ""
        result = []

        # separador de HTML
        for l in html[2:-2]:
            word += l
            if l == ">":
                if word[1] == "n" or word[2] == "n":
                    result.append(word[2:])
                else:
                    result.append(word)
                word = ""

        count = 1
        for k in range(0, len(result)):
            result[k][0:7]
            if result[k][0:7] == "<title>" and result[k+1][0:7]:
                item = result[k+1][11:-17].replace(" ", "")
            if result[k][0:4] == "<img":
                img = result[k].split()[2][5:-1]
            elif result[k][0:4] == "<h2 ":
                nome = result[k+1][:-5]
                if nome == "Checking if the site connection is secure":
                    break
                preco = "R$" + result[k+8][8:-4]
                link = "https://www.pichau.com.br/" + result[k-20].split()[-1][6:-2]
                hist = [str(datetime.datetime.now())[0:11], preco]
                prod_list[unidecode(item)][count] = {
                    "Nome": unidecode(nome.replace(" ", "")),
                    "Preco": preco, "Imagem": img, "Link": link, "Historico": hist}
                count += 1
                if count == 6:
                    break
            elif result[k][0:7] == "<title>":
                item = result[k+1][11:-17].replace(" ", "")
                #print("ITEM: " + item)

                """
                print(nome)
                print(preco)
                print(img)
                print(link)
                print(hist)
                print()
                """



    produtos_json = json.dumps(prod_list)
    with open(f"bd\produtosPICHAU.json", "r+") as arquivo_json:
        arquivo_json.write(produtos_json)


def kabumJson():
    prod_list = {
        f"{unicodedata.normalize('NFD', banco.Produtos[1]['titulo'].replace(' ', '')).encode('ascii', 'ignore').decode('utf-8')}": {},
        f"{unicodedata.normalize('NFD', banco.Produtos[2]['titulo'].replace(' ', '')).encode('ascii', 'ignore').decode('utf-8')}": {},
        f"{unicodedata.normalize('NFD', banco.Produtos[3]['titulo'].replace(' ', '')).encode('ascii', 'ignore').decode('utf-8')}": {},
        f"{unicodedata.normalize('NFD', banco.Produtos[4]['titulo'].replace(' ', '')).encode('ascii', 'ignore').decode('utf-8')}": {},
        f"{unicodedata.normalize('NFD', banco.Produtos[5]['titulo'].replace(' ', '')).encode('ascii', 'ignore').decode('utf-8')}": {},
        f"{unicodedata.normalize('NFD', banco.Produtos[6]['titulo'].replace(' ', '')).encode('ascii', 'ignore').decode('utf-8')}": {},
        f"{unicodedata.normalize('NFD', banco.Produtos[7]['titulo'].replace(' ', '')).encode('ascii', 'ignore').decode('utf-8')}": {},
        f"{unicodedata.normalize('NFD', banco.Produtos[8]['titulo'].replace(' ', '')).encode('ascii', 'ignore').decode('utf-8')}": {},

    }

    bd = open("bd/kabumHtml.txt", "r", encoding="utf-8")
    htmls = bd.read().split("], [")

    for html in htmls:
        word = ""
        result = []

        # separador de HTML
        for l in html[2:-2]:
            word += l
            if l == ">":
                if word[1] == "n" or word[2] == "n":
                    result.append(word[2:])
                else:
                    result.append(word)
                word = ""

        count = 1
        for k in range(0, len(result)):
            if result[k] == '<div id="listingBreadcrumbs" class="sc-1f1372c4-0 bmoswX">':
                if result[k+3] == '<div>':
                    print(result[k+9])
                    if str(result[k+9][-9:]) == "(VGA)</a>":
                        item = unicodedata.normalize('NFD', result[k + 9][:-10].replace(' ', '')).encode('ascii','ignore').decode('utf-8')
                    else:
                        item = unicodedata.normalize('NFD', result[k + 9].replace(' ', '').replace("</a>", "")).encode('ascii','ignore').decode('utf-8')
                        if item == "Processadores":
                            item = "Processador"
                        if item == "Coolers":
                            item = "Watercooler"
                        if item == "ntes":
                            item = "Fonte"
                    print(item)
                else:
                    print("AQUI"+result[k+3])
            if result[k][0:4] == "<img":
                img = result[k].split()[2][5:-7]
            elif result[k][0:4] == "<spa":
                line = result[k].split()
                if len(line) > 4 and line[2] == 'class="sc-d79c9c3f-0':
                    nome = result[k+1][:-7]
                    link = "https://www.kabum.com.br" + result[k - 6].split()[1][6:-1]
                    preco = "R$" + result[k+9][8:-7]
                    hist = [str(datetime.datetime.now())[0:10], preco]
                    print(nome)
                    print(img)
                    print(link)
                    print(preco)
                    print(hist)
                    print()



                    prod_list[item][count] = {
                        "Nome": unicodedata.normalize("NFD", nome).encode("ascii", "ignore").decode("utf-8"),
                        "Preco": preco, "Imagem": img, "Link": link, "Historico": hist}
                    count += 1
                    if count == 6:
                        break

    produtos_json = json.dumps(prod_list)
    with open(f"bd\produtosKabum.json", "w") as arquivo_json:
        arquivo_json.write(produtos_json)
kabumJson()
