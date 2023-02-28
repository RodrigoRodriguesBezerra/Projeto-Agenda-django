from datetime import datetime
import random
import os

# Você pode mudar para .sql ou a extensão que quiser.
arquivo = open("sqlsInserts.sql", "a")
sqls = list()

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

for i in range(3, 210):  # Presume que você só usou os ids 1 e 2 pois começa do 3
    id = i
    nome = ''.join(random.choices(ALPHABET, k=6))  # Gera nomes de tamanho 6
    sobrenome = ''.join(random.choices(ALPHABET, k=6))  # Gera sobrenomes de tamanho 6
    num_registro = str(i).zfill(3)
    tres_ultimos_digitos = num_registro
    telefone = f'31999999{tres_ultimos_digitos}'
    email = f'{nome}@gmail.com'
    data_criacao = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    categoria_id = random.randint(1, 3)  # Estou presumindo a existência de 3 categorias

    valores = f"INSERT INTO contatos_contato (id, nome, sobrenome, telefone, email, data_criacao, descricao, categoria_id) VALUES ('{id}', '{nome}', '{sobrenome}', '{telefone}', '{email}', '{data_criacao}', 'descricao{num_registro}', '{categoria_id}'); \n"

    sqls.append(str(valores))

arquivo.writelines(sqls)
arquivo.close()
print(f"Feito, foram inseridos {len(sqls)} no arquivo txt!")
