imiona = ['Agata', 'Raymond', 'Stasiu','Stefan', 'Mafik', 'Kuba']

for i in range(len(imiona)):
    if imiona[i][-1] == 'a' and imiona[i] != 'Kuba':
        print(f'Szanowna Pani {imiona[i]}')
    else:
        print(f'Szanowny Pan {imiona[i]}')

for imie in imiona:
    if imie[-1] == 'a' and imie != 'Kuba':
        print(f'Szanowna Pani {imie}')
    else:
        print(f'Szanowny Pan {imie}')
