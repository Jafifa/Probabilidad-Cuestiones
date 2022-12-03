CUESTIONES = int(input("Escriba nº de cuestiones que hay en total (normalmente 23): "))
SABIDAS = int(input("Escriba nº de cuestiones sabidas (las que has estudiado): "))
CUESTIONESOFRECIDAS = int(input("Escriba nº de cuestiones que le ofrecen en el examen (normalmente 12): "))
CUESTIONESNECESARIAS = int(input("Escriba nº de cuestiones que le piden responder en el examen (normalmente 4): "))


tope = CUESTIONESOFRECIDAS - CUESTIONESNECESARIAS +1
def main():
	probabilidad = 100 * ramificacion(CUESTIONESOFRECIDAS, SABIDAS, CUESTIONES-SABIDAS, 0, 1.0)
	print(f"Probabilidad final: {round(probabilidad,2)}%" )


def ramificacion(preguntasRestantes, sabidasRestantes, sinSaberRestantes, errores, probabilidadActual):
	#Si esta rama ha cateado ya, ni nos molestamos en calcular sus subdivisiones
	if errores >= tope:
		return 0
	#Si ha sobrevivido la condicion anterior y no quedan preguntas restantes, significa que se sabe todas
	if preguntasRestantes <= 0:
		return probabilidadActual
	#Calculamos probabilidad de cada rama
	probabilidadMala = probabilidadActual * (sinSaberRestantes / (sabidasRestantes + sinSaberRestantes))
	probabilidadBuena = probabilidadActual * (sabidasRestantes / (sabidasRestantes + sinSaberRestantes))

	#Recursión
	#Rama donde la siguiente pregunta la sabemos
	probabilidadBien = ramificacion(preguntasRestantes-1, sabidasRestantes-1, sinSaberRestantes, errores, probabilidadBuena)
	#Rama donde NO la sabemos
	probabilidadBien += ramificacion(preguntasRestantes-1, sabidasRestantes, sinSaberRestantes-1, errores+1, probabilidadMala)
	return probabilidadBien


if __name__ == "__main__":
	main()
