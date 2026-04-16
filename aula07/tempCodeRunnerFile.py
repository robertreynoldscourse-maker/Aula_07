lst_produtos = [i for i in range(10)]
clas_produtos = [i for i in range(10)]
for i in lst_produtos:
    lst_produtos[i] = int(input(f'Digite o valor da venda {i}: '))
    if lst_produtos[i] > 700:
        clas_produtos[i] = 'Próximo da meta.'
    else:
        clas_produtos[i] = 'Abaixo do esperado.'
print('')
print('CLASSIFICAÇÃO')
print('')
for i in range(9):
    print(f'{lst_produtos[i]}       {clas_produtos[i]}')