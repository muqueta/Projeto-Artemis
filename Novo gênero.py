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

#    4) Solicitar a subfamília

while True:
    subfamilia = input("Informe a subfamilia à qual a espécie pertence: ").lower().capitalize()
    if not subfamilia.isalpha():
        print("Atenção: utilize apenas letras.")
    else:
        break

cursor.execute('Select count (*) from subfamilias where subfamilia = ?', (subfamilia, ))
resultado = cursor.fetchone()
if resultado[0] == 0:
    print("A subfamília ainda não foi cadastrada. Por favor, cadastre-a.")
    quit() # não repetir o loop e encerrar o programa
else:
    cursor.execute('Select idSubfamilia from subfamilias where subfamilia = ?', (subfamilia, ))
    idSubfamilia = cursor.fetchone()[0]

#    5) Inclusão do gênero

while True:
    genero = input('Gênero: ').lower().capitalize()
    if not genero.isalpha():
        print('Atenção: utilize apenas letras.')
    else:
        cursor.execute('Select count (*) from generos where genero = ?', (genero, ))
        resultado = cursor.fetchone()
        if resultado[0] == 0:
            break
        else:
            print('Gênero já cadastrado no banco.')
            resposta = input('Deseja sair? S/N: ').upper()
            if resposta == 'S':
                quit()
            else:
                continue

#    6) Inclusão do autor do gênero

while True:
    autorGenero = input('Autor: ').lower().capitalize()
    if not autorGenero.isalpha():
        print('Atenção: utilize apenas letras.')
    else:
        break

#    7) Inclusão do ano do gênero

while True:
    anoGenero = input('Ano: ')
    if not anoGenero.isnumeric():
        print('Atenção: utilize apenas números.')
    else:
        anoGenero = int(anoGenero)
        if anoGenero < 1700 or anoGenero > anoAtual:
            print('Ano inválido. Tente novamente.')
        else:
            break

#    8) Comando de inclusão no banco 

conn.execute('Insert into generos (idSubfamilia, genero, autorGenero, anoGenero, idlog) values (?,?,?,?,?)', (idSubfamilia, genero, autorGenero, anoGenero, login))

#    9) Commit e fim

conn.commit()

print("Gênero cadastrado com sucesso!")

cursor.close()
conn.close()

quit()