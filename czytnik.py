from barcode import EAN13
from generator_kodow_wlasny import *

print("------Czytnik kodów kreskowych------")
print("(proszę wpisać q, aby zakończyć działanie programu)\n")
while True:
	print("Prosze zeskanować kod kreskowy:")
	numerEAN = input()
	if numerEAN == 'q':
		print("Kończenie pracy programu")
		break
	print()
	if len(numerEAN) != 12 or numerEAN.isnumeric() is False:
		print(f"Kod EAN powinien mieć 12 znaków i nie zawierać liter, {numerEAN} nie jest prawidłowym kodem EAN.")
	else:
		print(f"Czy chesz wygenerować zeskanowany kod ({numerEAN})? Proszę wpisać \'t\' jeśli tak")
		generowanie = input()
		if generowanie == 't':
			ean_graficzny = EAN13(numerEAN)
			ean_graficzny.save(f"kod_{numerEAN}")
			ean_graficzny2 = wygeneruj_kod_EAN(numerEAN)
