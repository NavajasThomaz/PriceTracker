import datetime
bd = open("bd\produtos.txt", "r")

htmls = bd.read().split("], ")
# html = htmls[0].split(">")
word = ""
result = []



class prod:
    def __init__(self, nome, preco, imagem, link, hist):
        self.nome = nome
        self.preco = preco
        self.imagem = imagem
        self.link = link
        self.hist = hist

    def __repr__(self):
        return f"Titulo: {self.nome}\nPreço: {self.preco}\nLink da Imagem: {self.imagem}\nLink do Produto: {self.link}\nHistórico de preço: {self.hist}\n\n"




for l in htmls[0][2:-2]:
    if l == "<":
        word += l
    elif l == ">":
        word += l
        if word[1] == "n" or word[2] == "n":
            result.append(word[2:])
        else:
            result.append(word)
        word = ""
    else:
        word += l

prod_list = []
for k in range(0, len(result)):
    if result[k][0:4] == "<img":
        img = result[k].split()[1]
    elif result[k][1] == "a":
        line = result[k].split()
        if len(line) > 4 and line[1] == 'class="prod-name"':
            #prod_list.append(prod(f"{line[3:][0][7:]} {line[3:][0][7:]}"))
            nome = f"{line[3:][0][7:]} " + " ".join(line[4:-1]) + f" {line[-1][:-2]}"
            link = line[2]
            #print(f"{line[3:][0][7:]} {line[3:][0][7:]}")
            if result[k + 12][:-7][0] == "R":
                preco = result[k + 12][:-7]
            else:
                preco = result[k + 11][:-7]
            hist = [str(datetime.datetime.now())[0:10], preco]
            prod_list.append(prod(nome, preco, img, link, hist))

print(prod_list)


# print(html)
# for i in html:
# print(i[0:4])
