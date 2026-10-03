notas = []
n1 = float(input("digite a nota 1 :"))
n2 = float(input("digite a nota 2 :"))
n3 = float(input("digite a nota 3 :"))
n4 = float(input("digite a nota 4 :"))

notas = [n1, n2, n3, n4]

media = sum(notas) / len(notas)
maior = max(notas)
menor = min(notas)
total = sum(notas)

print (f"media é igual a : {media}")
print (f"nota maior é igual : {maior}")
print (f"nota menor é igual a : {menor}")
print (f"o valor das nota total é igual a :{total}")

if media >=6:
    print("aprovado")
else:
    print("reprovado")
    






# print(max(lista_notas))
# #append max ele traz o maior valor
# print(min(lista_notas))
# #append min ele traz o minimo valor
# print(sum(lista_notas))
# #append sum ele soma todos valores
# print(len(lista_notas))
# 9
# 8
# 7



                 

# notas_1 = [4,6,8,10]
# notas_2 = [8,7,6,9]
# notas_3 = [10,8,5,7]
# notas_4 = [8,5,7,9]