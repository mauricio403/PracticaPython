#print(5 + 10)
# comentario

#mauricio = 'Mauricio.py'

# print(mauricio)


#print(r"este texto tiene \nsalto de linea")

#nombre = 'Teoria sobre este tema donde salto de linea es con \nson dos lineas'
# print(nombre)

#nombreSuma = nombre+nombre
#print(nombreSuma)

#nombre = 'Hyoga '
#constelacion = ' cisne'

#print(nombre + 'de' + constelacion)

#caballero = 'Viviana'
# print(caballero[5])

#numero = len(caballero)

#print(numero)


#listas = [10, 20, "Mauricio", -9, "Josselyn"]

#print(listas[3])

#listas[2] = 'Fabiricio'
#print(listas[2])


#listas.append("Vivana")

#print(listas)

#input("Introduce un valor")

#mau = not True
#print(mau)

#mau = False and False
#print(mau)

#numero = 10

#val = numero > 5 and numero > 15 
#print(val)

#print(numero>5 or numero>15)

#print(1!=1)

#print(4>=4)


#Estrcuturas de Control

#if True:
 # print("Imprimo esto porque la evaluacion es verdadera")

#Maur = 10
#if Maur == 67:
  #  print("La variable vale 67")
#if Maur == 10:
 #   print("Maur vale 10")

#if Maur == 11 or  Maur == 10:
#    print("Entro!")


#vivi = 13

#if vivi % 2 == 0:
   # print('El resto es 0')
#else:
 #   print("El resto no es cero")

#frase = "mmvrg"

#if frase == "NO":
 #   print("Bienvenidos")
#elif frase == "Hola":
 #   print("Nos estan saludando")
#else:
 #   print("Esto es algo cuando no da ningun resultado")

#final = float(input("Colocca la nota: "))

#if final >= 9:
 #   print("Eres un crack!")
#elif final >=7:
  #  print("Aprobaste")
#elif final == 6:
 #   print("Te falto poco xD")
#elif final <= 5:
 #   print("Tuviste que estudiar un curso mas chevere")
#else:
 #   print("Valiste gaver")


#Bucle While

#inicio = 0

#while inicio <= 3:
 #   inicio += 1
  #  print("Estoy iterando, van  = ", inicio)
#else:
 #   print("Imprimo esto porque se termino y esto es el else")


#iteracion = 0

#while iteracion <=0:
 #   iteracion +=1
  #  print("Estoy iterando van = ", iteracion)
   # break
#else:
 #   print("Imprimo esto porque se termino y es el else")

        #Practica


#print("elije tu propio camino'")

#inicio = input("Escribe empezar para iniciar el programa: ")


#while inicio == "empezar":
 #   print("""Que camino deseas elejinr?
  #  1. Quiero que me saludes
   # 2. Deseo multiplicar porque no se como hacerlo
    #3. Quiero salir de este programa , ya que aprendi a multiplicar""")
     
    #opcion = input("elije")
    #if opcion == '1':
     #   print("Hola que tal??")
    #elif opcion == '2':
     #   numero1 = float(input("Escribe un numero"))
      #  numero2 = float(input('Escribe el segundo numero'))

       # print("El resultado es: ", numero1*numero2)
    #elif opcion == '3':
     #   print("Ya has salido")
      #  break
    #else:
     #   print("No se que elejiste, elije del rango del 1 al 3")

#Bucle For

#lista=[1,2,3,4,5,6,7,8,9]

#indice = 0

#while indice <= len(lista):
 #   print(lista[indice])
  #  indice +=1

#for recorrer in lista:
 #   print(recorrer)

#for recorrer in lista:
 #  lista[indice] *= 10
  # indice +=1
#print(lista)

#for indice, recorrer in enumerate(lista):
 #   lista[indice] *=10
#print(lista)

#letra = 'Mauricio'
#for caracteres in letra:
 #   print(caracteres)

#for i in range(10):
 #    print(i)

#for i in [0,1,2,3,4,5]:
 #    print(i)


#Tuplas

#son listas que no se pueden mdificar.... al hacerlo nos da error
#t = ("Mauricio", "Viviana", "ALexandra", 20, [1,2,3], 10, -50)
#print(t)

#t[0]='Luis'
#print(t)

#print(t.index("Viviana"))

#con index... buscamos por teclado el termino y nos devuelve la posicion que tiene en la tupla

#print(t.count(20))
#el count sirve para contar cuantos caracteres hay dentor de una tupla


#continara....