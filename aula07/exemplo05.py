# titulo, autor, ano de publicação, gênero e número de páginas
livros = []
for i in range(2):
    print(f'\n----- Livro {i+1} -----')
    livro = {}
    livro['titulo'] = input('Nome do livro: ')
    livro['autor'] = input('Nome do autor: ')
    livro['ano'] = int(input('Ano de publicação: '))
    livro['genero'] = input('Gênero do livro: ')
    livro['paginas'] = int(input('Número de páginas: '))
    livros.append(livro)
print('Livro cadastrado!!!!')
print(livros)

# #Mostrando
print('\n--- LIVROS A PARTIR DE 2020 ---')
for l in livros:
    if l['ano'] >= 2020:
        #print(l)
        print('----------------------------')
        print(f'Nome do livro: {l['autor']}')
        print(f'Ano: {l['ano']}')
        print('----------------------------')