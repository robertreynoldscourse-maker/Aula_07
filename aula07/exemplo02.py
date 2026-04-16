list_produtos = ['Notebook', 'Mouse', 'Teclado', 'Monitor']
list_produtos[0] = 'PC'
print(f'Alterar o primeiro elemento {list_produtos}')

list_produtos.append('WebCam')
print(f'Produto adicionado {list_produtos}')

list_produtos.remove('Monitor')
list_produtos.pop() #Remove o ultimo elemento
print(f'Remove o ultimo {list_produtos}')

del list_produtos[0]
print(f'Produto removido {list_produtos}')
#print(list_produtos)