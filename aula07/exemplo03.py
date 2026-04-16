# lst_produtos = [i for i in range(10)]
# clas_produtos = [i for i in range(10)]
# for i in lst_produtos:
#     lst_produtos[i] = int(input(f'Digite o valor da venda {i}: '))
#     if lst_produtos[i] > 700:
#         clas_produtos[i] = 'Próximo da meta.'
#     else:
#         clas_produtos[i] = 'Abaixo do esperado.'
# print('')
# print('CLASSIFICAÇÃO')
# print('')
# for i in range(9):
#     print(f'{lst_produtos[i]}       {clas_produtos[i]}')
n = int(input('Digite a quantidade de vendas: '))
print('')
vendas= []
for i in range(n):
    valor = float(input(f'Digite a venda {i}: '))
    vendas.append(valor)
print('')
print(f'Vendas registradas: {vendas}\n')

META = 1000
META_MINIMA = 700

for v in vendas:
    if v >= META:
        print(f'Venda de {v} - Meta Atingida')
    elif v >= META_MINIMA:
        print(f'Venda de {v} - Próximo da meta')  
    else:
        print(f'Venda de {v} - Bem abaixo da meta')

print('')
print('Encerrando...')