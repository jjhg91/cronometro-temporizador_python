# LIBRERIAS NECESARIAS PARA 
# 	DETENER LA APLICACION -TIME-
# 	CREAR UN TIEMPO DETERMINADO -DATETIME-
# 	LIMPIAR LA PANTALLA -OS-
import time, datetime, os





# FUNCION PARA EL CRONOMETRO
# 	ESTE LIMPIA LA PANTALLA
# 	ASIGNA UN TIEMPO DE H:0 M:0 S:0
# 	Y COMIENZA EL CICLO WHILE 
# 		LIMPIA LA PAMTALLA NUEVAMENTE
# 		IMPRIME EN PANTALLA EL TIEMPO QUE LLEVA
# 		IMPRIME LA OPCION DE SALIR 
# 		SE PAUSA 1 SEGUNDO 
# 		SUMA 1 SEGUNDO AL TIEMPO PARA REPETIR EL CICLO WHILE NUEVAMENTE 
def CRONOMETRO():
	os.system('cls')
		
	tiempo = datetime.timedelta(hours= 0, minutes= 0,seconds= 0)
	while True:
		os.system('cls')
		print("\n")
		print ("     ###########################")
		print ("     #                         #")
		print ("     #        CRONOMETRO       #")
		print ("     ###########################")
		print ("     #                         #")
		print ("     #  Tiempo =  ",tiempo,"    #")
		print ("     #                         #")
		print ("     ###########################")
		print ("\n")
		print ("     Control + C  para salir..")
		time.sleep(1)
		tiempo+= datetime.timedelta(seconds= 1)
		




# FUNCION PARA EL TEMPORIZADOR 
# 	LIMPIA LA PANTALLA 
# 	IMPRIME LAS INSTRUCCIONES
# 	TE SOLICITA LAS HORAS 
# 		VALIDA LAS HORAS CORRECTA
# 	TE SOLICITA LOS MINUTOS
# 		VALIDA LOS MINUTOS CORRECTA
# 	TE SOLICITA LOS SEGUNDOS 
# 		VALIDA LOS SEGUNDOS CORRECTA
# 	CREA UN TIEMPO CON LOS VALORES PASADOS H:M:S
# 	COMIENZA EL CICLO WHILE 
# 		LIMPIA LA PANTALLA NUEVAMENTE  
# 		IMPRIME EN PANTALLA EL TIEMPO TRANSCURRIDO
# 		SE PAUSE 1 SEGUNDO
# 		RESTA 1 SEGUNDO AL TIEMPO TRANSCURRIDO
# 		VALIDA SI A LLEGADO A 0 PARA MOSTRAR EL MENSAJE 
# 			SI LLEGA SE DETIENE 
# 		SI NO LLEGA VUELVE A REALIZAR EL CICLO WHILE HASTA LLEGAR A 0 
def TEMPORIZADOR():
	os.system('cls')
	print ("\n")
	
	print("      Escribe el tiempo para comenzar")
	
	hora = input("      Horas: ")
	while (int(hora) > 23 ):
		print("      Hora invalido, vuelva a escribirlo")
		hora = input("      Horas: ")

	minuto = input("      Minustos: ")
	while (int(minuto) > 59):
		print("      Minutos invalido, vuelva a escribirlo")
		minuto = input("      Minutos: ")

	segundo = input("      Segundos: ")
	while (int(segundo) > 59):
		print("      Segundos invalido, vuelva a escribirlo")
		segundo = input("      Minutos: ")
	tiempo = datetime.timedelta(hours= int(hora), minutes= int(minuto), seconds= int(segundo))

	while True:
		os.system('cls')
		print("\n")
		print ("     ###########################")
		print ("     #                         #")
		print ("     #      TEMPORIZADOR       #")
		print ("     ###########################")
		print ("     #                         #")
		print ("     #  Tiempo =  ",tiempo,"    #")
		print ("     #                         #")
		print ("     ###########################")

		time.sleep(1)
		tiempo -= datetime.timedelta(seconds=1)
		if ( tiempo <  datetime.timedelta(hours= 0, minutes=0,seconds= 0)):
			print("\n")
			print("      Tiempo finalizado ")
			input("      presione enter para salir..")
			break
		







# FUNCION MENU 
# 	LIMPIA LA PANTALLA
# 	IMPRIME EL MENU ESCRITO EN PANTALLA
# 	SOLICITA UN NUMERO DEL MENU EN PANTALLA
# 	VALIDA LA OPCION SELECCIONADA PARA LLAMAR A LA FUNCION DE ESA OPCION 
def MENU():
	os.system("cls")
	print ("\n")
	print ("     ###########################")
	print ("     #                         #")
	print ("     #           MENU          #")
	print ("     ###########################")
	print ("     #                         #")
	print ("     #   1) CRONOMETRO         #")
	print ("     #   2) TEMPORISADOR       #")
	print ("     #   3) SALIR              #")
	print ("     #                         #")
	print ("     ###########################")
	print ("\n")

	opcion = input("OPCION: ")

	if(opcion == "1"):
		CRONOMETRO()
	elif( opcion == "2"):
		TEMPORIZADOR()
	elif(opcion == "3"):
		exit()



# LLAMA A LA FUNCION MENU
MENU()