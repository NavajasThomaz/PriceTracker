from fastapi import FastAPI, Path
from bd import Produtos
from typing import Optional
import requests
from bs4 import BeautifulSoup

app = FastAPI()


# URL Base
@app.get("/busca/{user_busca}")
def busca(user_busca: str):
    urls = {
        1: {"Nome": "TERABYTE", "url": f'https://www.terabyteshop.com.br/busca?str={user_busca}'},
        2: {"Nome": "PICHAU", "url": f'https://www.pichau.com.br/search?q={user_busca}'},
        3: {"Nome": "KABUM","url": f'https://www.kabum.com.br/busca/{user_busca}'},
        }
    for url in urls:
        if urls[url]["Nome"] == "TERABYTE":
            return
            

@app.get("/")
def homepage():
    return "Hello Word!"

@app.get("/produtos/{id_produto}")
def produtos(id_produto: int = Path(description="Id do produto")):
    return Produtos[id_produto]

@app.get("/produtos_por_nome/{nome_produto}")
def produtos_por_nome(nome_produto: Optional[str] = Path(description="Nome do produto")):
    for produto in Produtos:
        if Produtos[produto]["titulo"] == nome_produto:
            return Produtos[produto]