
#   0) Importar datetime

from datetime import datetime

anoAtual = datetime.now().year

#    1) Importar sqlite3

import sqlite3

#    2) Comunição e cursor com os dois bancos de dados

conn = sqlite3.connect('Artemis.db')
cursor = conn.cursor()

# conn2 = sqlite3.connect('banco de cadastro')
# cursor2 = conn2.cursor()

#    3) Validação do login 

# PROVISÓRIO ENQUANTO NÃO HÁ INTEGRAÇÃO

login = input("Digite seu login: ")

#    4) Solicitar o gênero

while True:
    genero = input("Informe o gênero ao qual a espécie pertence: ").lower()
    if not genero.isalpha():
        print("Atenção: utilize apenas letras.")
    else:
        genero = genero.capitalize()
        break

cursor.execute('Select count (*) from generos where genero = ?', (genero, ))
resultado = cursor.fetchone()
if resultado[0] == 0:
    print("O gênero ainda não foi cadastrado. Por favor, cadastre-o.")
    quit() # não repetir o loop e encerrar o programa
else:
    cursor.execute('Select idGenero from generos where genero = ?', (genero, ))
    idgenero = cursor.fetchone()[0]

#   4.5) Buscar o ID da subfamilia baseado no Id do genero

cursor.execute('Select idSubfamilia from generos where idGenero = ?', (idgenero, ))
idSubfamilia = cursor.fetchone()[0]


#   5) Inclusão da espécie

while True:
    especie = input("Espécie: ").lower().capitalize()
    especie_split = especie.split()

    if not especie_split[0].isalpha() or not especie_split[1].isalpha():
            print("Atenção: utilize apenas letras!")
    else:
        if especie_split[0] != genero:
            print(f"O epíteto genérico deve ser igual ao gênero já inserido: {genero}.")
        else:
            # 5.5 busca se a espécie já está cadastrada no banco:
            cursor.execute('Select count (*) from especie where especie = ?', (especie, ))
            resultado = cursor.fetchone()
            if resultado[0] == 0:
                break
            else:
                print('Espécie já cadastrada no banco.')

#    6) Inclusão do autor da espécie:

while True:
    autorEspecie = input("Autor da espécie: ").lower().capitalize()
    if not autorEspecie.isalpha():
        print("Atenção: utilize apenas letras!")
    else:
        break

#    7) Inclusão do ano da espécie:

while True:
    anoEspecie = input("Ano da espécie: ")
    if anoEspecie.isnumeric():
        anoEspecie = int(anoEspecie)
        if anoEspecie < 1700 or anoEspecie > anoAtual:
            print("Ano inválido. Tente novamente.")
        else:
            break
    else:
        print("Atenção: utilize apenas números.")
                       
#    8) Comando de inclusão no banco:

conn.execute('Insert into especie (idSubfamilia, idGenero, especie, autorEspecie, anoEspecie, idlog) values (?,?,?,?,?,?)', (idSubfamilia, idgenero, especie, autorEspecie, anoEspecie, login))

#    9) Commit e fim:

conn.commit()

print("Espécie cadastrada com sucesso!")

cursor.close()
conn.close()

quit()
