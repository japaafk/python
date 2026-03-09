produtos = {
    'Mouse' : {
        'preço' : 150,
        'quantidade' : 20
    },
    'Teclado' : {
        'preço' : 200,
        'quantidade' : 30
    },
    'Headset' : {
        'preço' : 10,
        'quantidade' : 50
    },
}

for chaves, valores in produtos.items():
    print(f"Item: {chaves}, Preço: {valores['preço']}, Quantidade: {valores['quantidade']}")