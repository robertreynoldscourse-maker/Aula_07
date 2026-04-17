####DICIONÁRIO-- requer chave mais valor
#pessoa_vazio = {}
#print(pessoa_vazio)

pessoa = {}
pessoa['Nome'] = 'João'
pessoa['Idade'] = 25
pessoa['Cidade'] = 'Niterói'

print(pessoa)

#Acessando uma chave
print(pessoa['Cidade'])
print(pessoa.keys())
print(pessoa.values())

###ALTERANDO VALOR
pessoa['Idade'] = 26
print(pessoa)

##ADICIONANDO UMA CHAVE
pessoa['Profissao'] = 'Programador'
print(pessoa)

##DELETANDO UMA CHAVE
del pessoa['Cidade']
print(pessoa)

