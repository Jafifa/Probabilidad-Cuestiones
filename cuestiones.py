CUESTIONES = 23 #Cuestiones que hay en total
SABIDAS = 15 #Cuestiones que te sabes
CUESTIONESOFRECIDAS = 12 #Cuestiones que te ofrecen en el examen
CUESTIONESNECESARIAS = 4 #Cuestiones que piden que respondas en el examen


tope = CUESTIONESOFRECIDAS - CUESTIONESNECESARIAS +1
def main():
	probabilidad = 100 * ramificacion(CUESTIONESOFRECIDAS, 7, CUESTIONES-7, 0, 1.0)
	for i in range(3,16):
		print(f"Probabilidad para {i} cuestiones estudiadas: {round(100 * ramificacion(CUESTIONESOFRECIDAS, i, CUESTIONES-i, 0, 1.0),2)}%" )
	#print(f"Probabilidad final: {probabilidad}" )

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