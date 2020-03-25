######################################################################################################################
###################################### by Arturo ####################################################################
#####################################################################################################################
'''
Importante: la pregunta y cada respuesta debe estar cada una en una linea, no puede haber mas de 4 opciones, solo 1 respuesta puede ser correcta,
    tras la ultima respuesta ha de ponerse la letra de la respuesta correcta Ej: Respuesta: C;
    despues de poner la respuesta hay q poner un salto de linea.
    Si cambias el directorio del programa, cambia el directorio donde debe estar el archivo .txt
'''

import random
import os


def ajustar(lista):         #ajusta la lista para que funcione bien con menos respeustas
    
    if len(lista)>4:
        while not (lista[1][:2].upper() == 'A)' or lista[1][:2].upper() == 'A.'):
            del lista[0]
    
    if lista[0] == '\n':
        lista[0].remove()
    i = 0
    
    while (i < len(lista)-2):
        if lista[i] == lista[i+1]:
            del lista[i]
        else:
            i += 1
    
    i = 0

    while (i < (len(lista)+1)//7):
        j = i*7
        
        if not (lista[j+1][:2].upper() == 'A)' or lista[j+1][:2].upper() == 'A.'):
            a=1

        elif not (lista[j+2][:2].upper() == 'B)' or lista[j+2][:2].upper() == 'B.'):
            a=2

        elif not (lista[j+3][:2].upper() == 'C)' or lista[j+3][:2].upper() == 'C.'):
            a=3
            
        elif not (lista[j+4][:2].upper() == 'D)' or lista[j+4][:2].upper() == 'D.'):
            a=4

        else:
            a=5
        
        try:
            for k in range(5-a):
                lista.insert(j+a,'\n')
        except: pass

        i = i+1

    if not lista[-1] == '\n':
        lista.append('\n')
    
    return(lista)


salir = True                #Variable que cambia cuando quieres salir del programa
aceptar = True
conjunto = set({})               #conjunto de respuestas respondidas correctamente
conjunto2 = set({})
txt_files = []
texto = []
su_respuesta = 'su respuesta'
error = set({})

print("Este programa realizara preguntas al azar de un archivo que elijas, responda con A, B, C o D, y con close para salir")
print("Las preguntas respondidas correctamente no volveran a mostrarse, mientras que las incorrectas volveran a salir en algun momento")
print (f"Este es el directorio donde debe estar el archivo: {os.getcwd()}\n")

while (aceptar):
    try:
        #'''
        nombre = input("\nIntroduzca el nombre del archivo terminado en txt o la carpeta de la cual se abriran todos los txt que haya:  ")     #introduces el nombre del archivo
        if nombre[-4:len(nombre)] == '.txt':
            with open(nombre,"r") as archivo:
                texto = archivo.readlines()   #guarda todas las lineas en un vector de lineas
            ajustar(texto)
            
        else:
            nombre1 = nombre+'/'
            all_files = os.listdir(nombre)
            for guardar in all_files:
                if guardar[-4:] == '.txt':
                    txt_files.append(guardar)
                    
            for filename in txt_files:
                try:
                    with open(f'{os.getcwd()}\\{nombre}\\{filename}', 'r') as prueba:
                        aux = prueba.readlines()
                        aux = ajustar(aux)
                
                        for i in range(len(aux)-1):
                            texto.append(aux[i])
                    
                        if not texto[-1] == '\n':
                            texto.append('\n')
                except:
                    error.add(filename)

        aceptar = False


    except:
        print("Este archivo o carpeta no puede abrirse, asegurate de que el nombre esta bien escrito")

if not len(error) == 0:
    print("\nNo se han podido abrir los siguientes archivos:")
    for i in error:
        print(f"    {i}")
    print(" ")

preguntas = (len(texto)+1)//7   #calcula cuantas preguntas hay
print(' ')

while (salir):
    try:
        if len(conjunto2) == preguntas-1:
            conjunto2.clear()
        rng = (random.randint(1,preguntas)-1)*7 #genera una pregunta al azar

        k = 0
        while (rng in conjunto2 or rng in conjunto):
            rng = (random.randint(1,preguntas)-1)*7 #genera una pregunta al azar hasta q genere uno q no este en conjunto
            k += 1
            if (k > 50):
                conjunto2.clear()   #la guarda como respondida para no repetir
            
        conjunto2.add(rng)   #la guarda como respondida para no repetir
        
        for i in range(5):      #escribe la pregunta y las 5 respuestas
            print(texto[rng+i])
            
        correcta = texto[rng+i+1]
        for i in range(len(correcta)):  #coge cual es la respuesta correcta
            if correcta[-i-1].upper() == 'A' or correcta[-i-1].upper() == 'B' or correcta[-i-1].upper() == 'C' or correcta[-i-1].upper() == 'D':
                correcta = correcta[-i-1].upper()
                break


    except:
        rng = 1
        print ("El archivo seleccionado no es adecuado para este programa")
        su_respuesta = 'close'
        correcta = 'no hay ninguna'
    
    respuesta = input(f"\nEscriba {su_respuesta}: ")
    respondida = True

    while respondida:   #se repite mientras se escriban cosas distintas de A,B,C,D o close
        if correcta == respuesta.upper():
            print("Correcto!!\n\n")
            respondida = False
            conjunto.add(rng)

        elif respuesta == "close":
            print("Suerte con el examen :)")
            salir = False
            respondida = False

        elif not(respuesta.upper() == "A" or respuesta.upper() == "B" or respuesta.upper() == "C" or respuesta.upper() == "D"):
            respuesta = input("Respuesta no valida, escriba A, B, C o D: ")

        else:
            print(f"Respuesta incorrecta, la respuesta correcta era la {correcta}\n\n")
            respondida = False

    if len(conjunto) == preguntas and not correcta == 'no hay ninguna':
        terminado = input("Has respondido correctamente todas las preguntas, para volver a empezar pulsa Enter, para salir escriba close\n")
        if terminado == "close":
            print("Suerte con el examen :)")
            salir = False

        else:
            conjunto.clear()

input()
