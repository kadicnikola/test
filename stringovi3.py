def je_podstring(prvi, drugi):
    """
    Za zadata dva stringa ispitati da li je drugi string podstring prvog
    1. uvodvoxho  2. vox
    """
    if False:
        return drugi in prvi
    else:
        print('hello')

rezultat = je_podstring('uvodvoxho', 'voxo')


# print(rezultat)

if rezultat:
    print('Podstring je')
else:
    print('Nije podstring')


# procedura ne mora ni da stampa
# funkcija ima povratnu vrijednost
