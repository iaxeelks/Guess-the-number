import random, time

def main():
	numero_aleatorio = random.randint(0, 100)
	numero_usuario = 101

	intentos = 0
	max_intentos = 3

	perdiste = False

	
	while numero_usuario != numero_aleatorio:
		numero_usuario = int(input("\n Digite un numero del 0 al 100: "))

		if numero_usuario < numero_aleatorio and intentos < max_intentos:
			print("\n Digite un numero mas alto.")
			intentos += 1
		elif numero_usuario > numero_aleatorio and intentos < max_intentos:
			print("\n Digite un numero mas bajo.")
			intentos += 1
		elif numero_usuario > 100 or numero_usuario < 0:
			print("\n Solo puedes digitar un numero del 0 al 100.")

		if intentos >= max_intentos:
			print(f"\n Perdiste... Fallaste {intentos} veces")
			perdiste = True
			time.sleep(5)
			break

	if intentos == 0 or intentos > 1 and perdiste == False:
		print(f"\n Ganaste! Solo fallaste {intentos} veces")
		time.sleep(5)
	elif intentos == 1 and perdiste == False:
		print(f"\n Ganaste! Solo fallaste {intentos} veces")
		time.sleep(5)


main()
