bd = open("bd\produtos.txt", "r")


htmls = bd.read().split("], ")
# html = htmls[0].split(">")
word = ""
result = []

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

for k in range(0,len(result)):
    if result[k][1] == "a":
        line = result[k].split()
        if len(line) > 4 and line[1] == 'class="commerce_columns_item_image"':
            print(line[3:])
#print(result)


# print(html)
# for i in html:
# print(i[0:4])
