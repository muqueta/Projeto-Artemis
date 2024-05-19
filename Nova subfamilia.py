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

#    4) Inclusão da subfamília

while True:
    subfamilia = input("Subfamília: ").lower().capitalize()
    if not subfamilia.isalpha():
        print("Atenção: utilize apenas letras")
    else:
        if subfamilia[-4:] != "inae":
            print('É necessária a utilização do sufixo "inae" para subfamílias.')
        else:
            cursor.execute('Select count (*) from subfamilias where subfamilia = ?', (subfamilia, ))
            result = cursor.fetchone()
            if result[0] == 0:
                break
            else:
                print('Subfamília já cadastrada.')
                resposta = input('Deseja sair? S/N: ').upper()
                if resposta == 'S':
                    quit()
                else:
                    continue

#    5) Inclusão do autor da subfamília

while True:
    autorSubfamilia = input("Autor da espécie: ").lower().capitalize()
    if not autorSubfamilia.isalpha():
        print("Atenção: utilize apenas letras!")
    else:
        break

#    6) Inclusão do ano da subfamília

while True:
    anoSubfamilia = input("Ano da subfamília: ")
    if anoSubfamilia.isnumeric():
        anoSubfamilia = int(anoSubfamilia)
        if anoSubfamilia < 1700 or anoSubfamilia > anoAtual:
            print("Ano inválido. Tente novamente.")
        else:
            break
    else:
        print("Atenção: utilize apenas números")
  
#    7) Comando de inclusão no banco 

conn.execute('Insert into subfamilias (subfamilia, autorSubfamilia, anoSubfamilia, idlog) values (?,?,?,?)', (subfamilia, autorSubfamilia, anoSubfamilia, login))

#    8) Commit e fim:

conn.commit()

print("Subfamília cadastrada com sucesso!")

cursor.close()
conn.close()

quit()
