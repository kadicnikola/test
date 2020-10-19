niz_ocjena = [3,5,3,5,3,5,3,1,3,5,3,5]

"""
print(niz_ocjena[2:10])
print(niz_ocjena[2:10:5])
"""

text = """
Prva recenica,
Druga recenica
Treca.
"""

print(text)

txt = "prva recenica druga recenica"

niz_ocjena_drustveni_predmeti = niz_ocjena[::2]

print(niz_ocjena_drustveni_predmeti)


ime_prezime = 'Nikola Kadic'

#ime = ime_prezime[0:6]

ime_prezime2 = 'Ana Markovic'

#ime2 = ime_prezime2[0:3]
ime_prezime_niz = ime_prezime.split(' ')
print(ime_prezime_niz)
ime = ime_prezime_niz[0]
prezime = ime_prezime_niz[1]

ime_prezime2_niz = ime_prezime2.split(' ')
ime2 = ime_prezime2_niz[0]
prezime2 = ime_prezime2_niz[1]


print(ime, prezime, ime2, prezime2)


niz1 = [2,52,312,312,5,123,123,12,3]

def odstampaj_prvih_5_clanova_niza(niz):
    print(niz[:5])

odstampaj_prvih_5_clanova_niza(niz1)
