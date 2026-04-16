# lista_de_livros_usando_dict: dict = {
#     "livro_01": {
#         "Titulo": "Game of Thrones",
#         "Autor": "Estagiario",
#         "Ano": 2005
#     },
    
#     "livro_02": {
#         "Titulo": "Game of Thrones 2",
#         "Autor": "Estagiario",
#         "Ano": 2007
#     }
# }

# titulos_livros = []

# for chave,conteudo in  lista_de_livros_usando_dict.items() :
#     titulos_livros.append(conteudo['Titulo'])



from pprint import pprint
respuesta_api = {
    "usuarios": [           #← LISTA
        {                   #← DICCIONARIO
            "id": 1,
            "nombre": "Juan",
            "perfil": {"edad": 30, "ciudad": "Madrid"} # DICCIONARIO
        },
        
        {                   #← DICCIONARIO
            "id": 2,
            "nombre": "Pedro",
            "perfil": {"edad": 25, "ciudad": "Valencia"} # DICCIONARIO
        }
    ]
}

usuarios = []

for chave,lista in respuesta_api.items():
    for elemento_lista in lista:
        usuarios.append(elemento_lista)
    


for usuario in usuarios:
    for clave,valor in usuario['perfil'].items():
        usuario[clave]= valor
    del usuario['perfil']    
    
pprint(usuarios)