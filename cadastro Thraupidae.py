import sqlite3

conn = sqlite3.connect('Artemis.db')

login = input("Digite seu login: ")

while True:
    subfamilia = input("Subfamília: ") 
    if not subfamilia.isalpha():
        print("Atenção: utilize apenas letras")
    else:
        if subfamilia[-4:] != "inae":
            print('É necessária a utilização do sufixo "idae" para subfamílias.')
        else:
            subfamilia = subfamilia.lower()
            subfamilia = subfamilia.capitalize()
            break
# se a subfamília estiver em um banco de outra família, invalidar

while True:
    genero = input("Gênero: ") 
    if not genero.isalpha():
        print("Atenção: utilize apenas letras!")
    else:
        genero = genero.lower()
        genero = genero.capitalize()
        break
 # se o gênero estiver em um banco de outra família de animais, invalidar. Plantas e outros pode permitir

while True:
    especie = input("Espécie: ")
    especie = especie.lower()
    especie = especie.capitalize()
    especie_split = especie.split()

    if not especie_split[0].isalpha() or not especie_split[1].isalpha():
            print("Atenção: utilize apenas letras!")
    else:
        if especie_split[0] != genero:
            print(f"O epíteto genérico deve ser igual ao gênero já inserido: {genero}.")
        else:
            break

while True:
    autorsp = input("Autor da espécie: ")
    if not autorsp.isalpha():
        print("Atenção: utilize apenas letras!")
    else:
        autorsp = autorsp.lower()
        autorsp = autorsp.capitalize()
        break

while True:
    anosp = int(input("Ano: "))
    if type(anosp) != int:
        print("Atenção: utilize apenas números.")
    else: 
        break

while True:
    subespecie = input("Subespécie: ")
    if subespecie == "":
        break
    else:
        if not subespecie.isalpha():
            print("Atenção: utilize apenas letras!")
        else:
            subespecie = subespecie.lower()
            break

autorsub = input("Autor da subespécie: ")
while True:
    anosub = int(input("Ano: ")) # se o ano for mais antigo do que o da espécie, invalidar --> verificar se possível
    if anosub == "":
        break
    else:
        if type(anosub) != int:
            print("Atenção: utilize apenas números.")
        else: 
            break

while True:
    confirma = input("Deseja cadastrar a espécie? (S/N)").upper()
    if confirma == "S" or confirma == "N":
        break
    else:
        print("Resposta inválida. Responda apenas com 'S' ou 'N'.")

if confirma == "S":
    conn.execute("insert into Thraupidae(subfamilia, genero, especie, autorsp, anosp, subespécie, autorsub, anosub, )")

quit()
