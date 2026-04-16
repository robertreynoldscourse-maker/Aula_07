#git remote set-url origin https://github.com/robertreynoldscourse-maker/Aula_06.git

lst_vazia_meses = [] #Lista vazia
lst_meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho']

#print(lst_vazia_meses)
print(lst_meses[0]) #Primeiro índice
print(lst_meses[2]) #Terceiro índice
print(lst_meses[-1]) #Último índice
print(lst_meses[-2]) #Penúltimo índice


## Fateamento
print(lst_meses[:3]) #Fatia1, imprime a partir do índice 2 até final.
print(lst_meses[3:]) #Fatia2, do inicio até (3-1)
print(lst_meses[3:5]) #Fatia3, Imprime a partir de 3 até (5-1)
print(lst_meses[3:6]) #Fatia4, Imprime a partir de 3 até (6-1)


#print(lst_vazia_meses)
print(lst_meses)

for i in lst_meses:
    print(i)