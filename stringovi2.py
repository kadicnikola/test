def broj_rijeci(ulazni_string):
    """
    ulazni_string -> string koji ima razmake
    Funkcija vraca broj elemenata niza razbijenog stringa po razmacima
    """
    niz_rijeci = ulazni_string.split(' ')
    duzina_niza = len(niz_rijeci) # nova ugradjena funkcija
    return duzina_niza

def da_li_je_rijec_palindrom(rijec):
    """
    Za unijetu rijec ispituje da li je palindrom
    returns: True or False zavisno od toga je li palindrom
    if rijec == rijec[::-1]:
        return True
    else:
        return False
    """

    rijec = rijec.replace(' ','')
    rijec = rijec.lower()
    
    return rijec == rijec[::-1]

print(da_li_je_rijec_palindrom('ana     voli milovanA'))