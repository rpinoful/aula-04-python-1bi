# # 1 - type hint 
# dicionario :dict ={
    
#     'livro1':{
#         'Autor':'Homero',
#         'Titulo': 'Odisea'
#         },
    
    
#     'livro2':{
#         'Autor': 'Dostoievksi',
#         'Titulo': 'Crime e castigo'     
#     }

# }


# autores = []

# print(dicionario.items())
# # pegar todos os autores e armazenar em uma lista
# for livro,cont in dicionario.items():
#     autores.append(cont['Autor'])
    

# print(autores)   
    
    
    




# data = {
#     'dept1': {
#         'emp1': {'name': 'Alice', 'salary': 50000},
#         'emp2': {'name': 'Bob', 'salary': 45000}
#     },
    
#     'dept2': {
#         'emp2': {'name': 'Ana', 'salary': 70000},
#         'emp3': {'name': 'Jhon', 'salary': 85000}
#     }
    
    
    
# }
# #recorre el primer dicionario que es dept 1 y con emp tomo el contenido de emp1
# for dep,emp in data.items():
#     print(f"\n{'='*80}")
#     print(f"DEPARTAMENTO: {dep.upper()}")
#     print(f"{'='*80}\n")
#     for key,datos in emp.items():
#         print(f"  ID Empleado: {key}")
#         print(f"  Nombre:      {datos['name']}")
#         print(f"  Salario:     ${datos['salary']:,}")
#         print(f"  {'-'*76}\n")





""" 
# Enunciados dos Exercícios




## Exercícios Básicos de Listas e Dicionários

1. **Lista de números ao quadrado** - Criar uma lista com números de 1 a 10 e exibir o quadrado de cada número.

2. **Modificar lista de linguagens** - Dada uma lista de linguagens de programação, remover "C++" e adicionar "Ruby".

3. **Informações de um livro** - Criar um dicionário com informações de um livro (título, autor, ano) e exibir cada chave e valor.

4. **Contar ocorrências de caracteres** - Criar uma função que recebe uma string e retorna um dicionário com a contagem de cada caractere.

5. **Preço total da lista de compras** - Dada uma lista de compras e um dicionário de preços, calcular o preço total.





## Exercícios Intermediários

6. **Eliminação de Duplicatas** - Dada uma lista de emails, remover todos os duplicados.

7. **Filtragem de Dados** - Dada uma lista de idades, filtrar apenas aquelas que são maiores ou iguais a 18.

8. **Ordenação Personalizada** - Dada uma lista de dicionários representando pessoas, ordená-las pelo nome.

9. **Agregação de Dados** - Dado um conjunto de números, calcular a média.

10. **Divisão de Dados em Grupos** - Dada uma lista de valores, dividir em duas listas: uma para valores pares e outra para ímpares.






## Exercícios com Dicionários

11. **Atualização de Dados** - Dada uma lista de dicionários representando produtos, atualizar o preço de um produto específico.

12. **Fusão de Dicionários** - Dados dois dicionários, fundi-los em um único dicionário.

13. **Filtragem de Dados em Dicionário** - Dado um dicionário de estoque de produtos, filtrar aqueles com quantidade maior que 0.

14. **Extração de Chaves e Valores** - Dado um dicionário, criar listas separadas para suas chaves e valores.

15. **Contagem de Frequência de Itens** - Dada uma string, contar a frequência de cada caractere usando um dicionário.# Enunciados dos Exercícios




## Exercícios Básicos de Listas e Dicionários

1. **Lista de números ao quadrado** - Criar uma lista com números de 1 a 10 e exibir o quadrado de cada número.

2. **Modificar lista de linguagens** - Dada uma lista de linguagens de programação, remover "C++" e adicionar "Ruby".

3. **Informações de um livro** - Criar um dicionário com informações de um livro (título, autor, ano) e exibir cada chave e valor.

4. **Contar ocorrências de caracteres** - Criar uma função que recebe uma string e retorna um dicionário com a contagem de cada caractere.

5. **Preço total da lista de compras** - Dada uma lista de compras e um dicionário de preços, calcular o preço total.










## Exercícios com Dicionários

11. **Atualização de Dados** - Dada uma lista de dicionários representando produtos, atualizar o preço de um produto específico.

12. **Fusão de Dicionários** - Dados dois dicionários, fundi-los em um único dicionário.

13. **Filtragem de Dados em Dicionário** - Dado um dicionário de estoque de produtos, filtrar aqueles com quantidade maior que 0.

14. **Extração de Chaves e Valores** - Dado um dicionário, criar listas separadas para suas chaves e valores.

15. **Contagem de Frequência de Itens** - Dada uma string, contar a frequência de cada caractere usando um dicionário.
"""




'''
## Exercícios Básicos de Listas e Dicionários







'''



# #1. **Lista de números ao quadrado** - Criar uma lista com números de 1 a 10 e exibir o quadrado de cada número.
# lista:list = [1,2,3,4,5,6,7,8,9,10]
# for num in lista :
#     print(f"o quadrado do num {num} é {num**2}")
    
    
    
    


# # 2. **Modificar lista de linguagens** - Dada uma lista de linguagens de programação, remover "C++" e adicionar "Ruby".
# linguagens :list = ['python','java','C++','C','Cobol']
# linguagens.remove('C++')
# linguagens.append('ruby')
# print(linguagens)


# # 3. **Informações de um livro** - Criar um dicionário com informações de um livro (título, autor, ano) e exibir cada chave e valor.
# dicionario :dict ={
    
#     'livro1':{
#         'Autor':'Homero',
#         'Titulo': 'Odisea',
#         'Ano':725
#         },
    
    
#     'livro2':{
#         'Autor': 'Dostoievksi',
#         'Titulo': 'Crime e castigo',     
#         'Ano' : 1866
#     }

# }

# for nome_livro, info_livro in dicionario.items():
#     print(f" Titulo: {info_livro['Titulo']} -Autor:{info_livro['Autor']} -Ano:{info_livro['Ano']}")




# # 4. **Contar ocorrências de caracteres** - Criar uma função que recebe uma string e retorna um dicionário com a contagem de cada caractere.
# from pprint import pprint

# def func_contar(string):
#     contar_char={}

#     if string == "":
#         return False

#     try:
#         for char in string:
#             if char in contar_char:
#                 contar_char[char] +=1
        
#             else:
#                 contar_char[char]=1




#     except ValueError as e:
#         print("Não foi inserido uma string")



    
    
    
    
    
    
    
#     return contar_char


# resultado = func_contar('dsfjdsiojfsdoijfbbbbvbnnnnffffgggghhhheeeerrrrttttyyyuuuiiioooppp')

# if resultado:
#     pprint(resultado)

# else:
#     print("Não foi ingresado valor nenhum")
    




#5. **Preço total da lista de compras** - Dada uma lista de compras e um dicionário de preços, calcular o preço total.
'''
precos = {
    "arroz": 22.90,
    "feijão": 9.45,
    "macarrão": 4.29,
    "leite": 5.69,
    "óleo de soja": 8.99,
    "açúcar": 5.19,
    "café": 12.80,
    "manteiga": 14.50,
    "pão de forma": 7.89,
    "ovos (dúzia)": 13.90
}


lista_compras = ["arroz","óleo de soja","ovos (dúzia)","feijão"]


# percorrer a lista de compras
preco_total = 0 
for produto in lista_compras:
    valor_produto = precos[produto]
    preco_total += valor_produto

print(f" A compra total foi de {preco_total:.2f}")
'''





## Exercícios Intermediários












# 6. **Eliminação de Duplicatas** - Dada uma lista de emails, remover todos os duplicados.
#1era forma com set
'''
emails = ['hola@gmail.com','pedroperez@gmail.com','marta@gmail.com','jhonmclean@gmail.com','pedroperez@gmail.com']
emails_not_dup = set(emails)
emails_not_dup= list(emails_not_dup)
print(emails_not_dup)
'''

'''
emails = ['hola@gmail.com','pedroperez@gmail.com','marta@gmail.com','jhonmclean@gmail.com','pedroperez@gmail.com']
email_vistos = set() #auxiliar
email_no_duplicados_ = [] #lista com aqueles quye não estão duplicados de fato
for email in emails:
    if email not in email_vistos:
        email_vistos.add(email)
        email_no_duplicados_.append(email)
print(email_no_duplicados_)
'''



# # 7. **Filtragem de Dados** - Dada uma lista de idades, filtrar apenas aquelas que são maiores ou iguais a 18.
# idades = [18,25,30,45,50,55,1,30,29,50,60,70,80,14,10,9,7]
# idades_filtro  = [idade for idade in idades if idade>=18]
# print(f"{idades_filtro}")


# # 8. **Ordenação Personalizada** - Dada uma lista de dicionários representando pessoas, ordená-las pelo nome.
# from numpy import append


# lista_pessoas:list = [
    
#     {
#         "nome":"Bob",
#         "idade":18
#     },
    
#     {
#         "nome":"Chester",
#         "idade":25
#     },
    
#     {
#         "nome":"Ana",
#         "idade":25
#     }    
# ]


# lista_pessoas.sort(key= lambda pessoa: pessoa['nome'])





# # 9. **Agregação de Dados** - Dado um conjunto de números, calcular a média.
# numeros = [15, 22, 8, 31, 19, 45, 12, 28, 37, 9]
# numeros_media = sum(numeros)/len(numeros)
# print(f" Numeros media {numeros_media:.2f}")



# # 10. **Divisão de Dados em Grupos** - Dada uma lista de valores, dividir em duas listas: uma para valores pares e outra para ímpares.
# valores = [23, 48, 15, 92, 7, 34, 61, 88, 12, 55, 76, 3, 41, 68, 29]
# impares =[num for num in valores if num%2!=0 ]
# pares = [num for num in valores if num%2==0 ]

# print(f" Numeros pares{pares}\n  Numeros impares{impares}")







'''❌ Exercícios que FALTAM (5 de 15):
Exercícios com Dicionários:








'''





#11. Atualização de Dados - Dada uma lista de dicionários representando produtos, atualizar o preço de um produto específico.
''' 
from pprint import pprint
produtos = [
    {"id": 1, "nome": "Notebook", "preco": 2500.00, "estoque": 15},
    {"id": 2, "nome": "Mouse", "preco": 45.00, "estoque": 50},
    {"id": 3, "nome": "Teclado", "preco": 120.00, "estoque": 30},
    {"id": 4, "nome": "Monitor", "preco": 800.00, "estoque": 10},
    {"id": 5, "nome": "Webcam", "preco": 250.00, "estoque": 20}
]


#quero atualizar
produtos_atualizar = ["Notebook","Mouse",]
1era versão
for produto in produtos:
    for nome_produto in produtos_atualizar:
        if produto['nome'] == nome_produto:
            produto['preco']= produto['preco']*0.25

print(produtos)
'''
# #versão mais direta
# for produto in produtos:
#     if produto['nome'] in produtos_atualizar:
#         produto['preco']= produto['preco']*0.25
# pprint(produtos)



#12. Fusão de Dicionários - Dados dois dicionários, fundi-los em um único dicionário.
'''
from pprint import pprint
dicionario1 = {
    "nome": "João",
    "idade": 28,
    "cidade": "São Paulo",
    "profissao": "Engenheiro"
}

dicionario2 = {
    "email": "joao@email.com",
    "telefone": "(11) 98765-4321",
    "estado": "SP",
    "pais": "Brasil"
}

#using update
dicionario1.update(dicionario2)
pprint(dicionario1)

# using | operator
fundidos = dicionario1 | dicionario2
pprint(fundidos)
'''



# 13. Filtragem de Dados em Dicionário - Dado um dicionário de estoque de produtos, filtrar aqueles com quantidade maior que 0.
''' 
from pprint import pprint
estoque = {
    "Teclado": 15,
    "Mouse": 0,
    "Monitor": 8,
    "Webcam": 0,
    "Headset": 25,
    "Mousepad": 0,
    "Hub USB": 12,
    "Cabo HDMI": 0,
    "SSD 500GB": 5,
    "Pendrive": 0
}

# traditional loop
produtos_disponiveis = {}


for key,quantidade in estoque.items():
    if quantidade >0:
        produtos_disponiveis[key]= quantidade

pprint(produtos_disponiveis)


#pythonic dict comprenhesion {k: v for k, v in ...
disponiveis_comp = {key:value for key,value in estoque.items() if value >0}
pprint(disponiveis_comp)
'''


# 14. Extração de Chaves e Valores - Dado um dicionário, criar listas separadas para suas chaves e valores.
''' 
funcionario = {
    "nome": "Maria Silva",
    "cargo": "Analista de Dados",
    "salario": 8500.00,
    "departamento": "TI",
    "anos_empresa": 5,
    "cidade": "Rio de Janeiro"
}

#pythonic
funcionario_keys = list(funcionario.keys())
funcionario_values = list(funcionario.values())
print(funcionario_keys)
print(funcionario_values)


# tradicional
tradicional_keys_func = []
tradicional_values_func = []
for key, value in funcionario.items():
    tradicional_keys_func.append(key)
    tradicional_values_func.append(value)
print(tradicional_keys_func)
print(tradicional_values_func)
'''



# 15. Contagem de Frequência de Itens - Dada uma string, contar a frequência de cada caractere usando um dicionário.
from pprint import pprint


texto = "engenharia de dados e analise de dados"
texto = texto.replace(" ","")

dictionary_char ={}

for char in texto:
    if char in dictionary_char:
        dictionary_char[char] +=1
    
    else:
        dictionary_char[char]=1


pprint(dictionary_char)