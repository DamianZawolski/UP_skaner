from barcode import EAN13
from generator_kodow_wlasny import *

print("Podaj numer EAN, dla którego chcesz wygenerować kod kreskowy: ")
bledny_ean = True
while bledny_ean:
    numerEAN = input()
    if len(numerEAN) != 12 or numerEAN.isnumeric() is False:
        print("Kod EAN powinien mieć 12 znaków i nie zawierać liter, proszę podać prawidłowy kod.")
    else:
        bledny_ean = False

# numerEAN = '123456789012'
ean_graficzny = EAN13(numerEAN)
ean_graficzny.save(f"barcode_kod_{numerEAN}")
ean_graficzny2 = wygeneruj_kod_EAN(numerEAN)

