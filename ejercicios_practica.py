#!/usr/bin/env python
'''
Condicionales [Python]
Ejercicios de práctica
---------------------------
Autor: Inove Coding School
Version: 1.1
 
Descripcion:
Programa creado para que practiquen los conocimietos adquiridos durante la semana
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.1"

def ej1():
    # Ejercicios de práctica con números

    '''
    Realice un programa que solicite por consola 2 números
    Calcule la diferencia entre ellos e informe por pantalla
    si el resultado es positivo, negativo o cero.
        
    '''
    numero_1 = int(input("Ingrese el primer numero: "))
    numero_2 = int(input("Ingrese el segundo numero: "))
    if numero_1 - numero_2 > 0:
      print("El resultado es positivo") 
    elif numero_1 - numero_2 < 0:
      print("El resultado es negativo")
    else:
      print("El resultado es cero")

def ej2():
  # Ejercicios de práctica con números

  '''
    Realice un programa que solicite el ingreso de tres números
    enteros, y luego en cada caso informe si el número es par
    o impar.
    Para cada caso imprimir el resultado en pantalla.
    
  '''
  lista = []
  lista.append(int(input("Ingrese el primer numero: ")))
  lista.append(int(input("Ingrese el segundo numero: ")))
  lista.append(int(input("Ingrese el tercer numero: ")))
  for numero in lista:
    if numero % 2 == 0:
      print(numero, "es par")
    else:
      print(numero, "es impar")

def ej3():
    # Ejercicios de práctica con números

    '''
    Realice una calculadora, se ingresará por línea de comando dos números
    Luego se ingresará como tercera entrada al programa el símbolo de la operación
    que se desea ejecutar
    - Suma (+)
    - Resta (-)
    - Multiplicación (*)
    - División (/)
    - Exponente/Potencia (**)

    Se debe efectuar el cálculo correcto según la operación ingresada por consola
    Imprimir en pantalla la operación realizada y el resultado
    

    '''
    numero_1 = int(input("Ingrese el primer numero a operar: "))
    numero_2 = int(input("Ingrese el segundo numero a operar: "))
    operacion = str(input("Ingrese la operacion a realizar: "))
    if operacion == "+":
      resultado = numero_1 + numero_2
      print("El resultado de sumar {} y {} es {}".format(numero_1, numero_2, resultado))

    elif operacion == "-":
      resultado = numero_1 - numero_2
      print("El resultado de restar {} y {} es {}".format(numero_1, numero_2, resultado))

    elif operacion == "*":
      resultado = numero_1 * numero_2
      print("El resultado de multiplicar {} y {} es {}".format(numero_1, numero_2, resultado))

    elif operacion == "/":
      resultado = numero_1 / numero_2
      print("El resultado de dividir {} y {} es {}".format(numero_1, numero_2, resultado))

    elif operacion == "**":
      resultado = numero_1 ** numero_2
      print("El resultado de elevar {} y {} es {}".format(numero_1, numero_2, resultado))

    else:
      print("Error, el operador ingresado es desconocido, empieze de vuelta")
      ej3()

def ej4():
    # Ejercicios de práctica con cadenas
    
    '''
    Realice un programa que solicite por consola 3 palabras cualesquiera
    Luego el programa debe consultar al usuario como quiere ordenar las palabras
    1 - Ordenar por orden alfabético (usando el operador ">")
    2 - Ordenar por cantidad de letras (longitud de la palabra)

    Si se ingresa "1" por consola se deben ordenar las 3 palabras por orden alfabético
    e imprimir en pantalla de la mayor a la menor

    Si se ingresa "2" por consola se deben ordenar las 3 palabras por cantidad de letras
    e imprimir en pantalla de la mayor a la menor

  '''
    palabra_1 = str(input("Ingrese la primera palabra que comparar: "))
    palabra_2 = str(input("Ingrese la segunda palabra que comparar: "))
    palabra_3 = str(input("Ingrese la tercera palabra que comparar: "))
    operacion = str(input("Ingrese 1 para comparar alfabeticamente \t|\t Ingrese 2 para comparar por longitud: \n"))

    if operacion == "1":
      if palabra_3 < palabra_1 > palabra_2:
        if palabra_2 > palabra_3:
          print("En orden alfabetico estan:", palabra_1, palabra_2, palabra_3)
        else:
          print("En orden alfabetico estan:", palabra_1, palabra_3, palabra_2)
      elif palabra_1 < palabra_2 > palabra_3:
        if palabra_1 > palabra_3:
          print("En orden alfabetico estan:", palabra_2, palabra_1, palabra_3)
        else:
          print("En orden alfabetico estan:", palabra_2, palabra_3, palabra_1)
      elif palabra_1 > palabra_2:
        print("En orden alfabetico estan:", palabra_3, palabra_1, palabra_2)
      else:
        print("En orden alfabetico estan:", palabra_3, palabra_2, palabra_1)

    elif operacion == "2":
      if len(palabra_3) < len(palabra_1) > len(palabra_2):
        if len(palabra_2) > len(palabra_3):
          print("Por cantidad de letras estan:", palabra_1, palabra_2, palabra_3)
        else:
          print("Por cantidad de letras estan:", palabra_1, palabra_3, palabra_2)
      elif len(palabra_1) < len(palabra_2) > len(palabra_3):
        if len(palabra_1) > len(palabra_3):
          print("Por cantidad de letras estan:", palabra_2, palabra_1, palabra_3)
        else:
          print("Por cantidad de letras estan:", palabra_2, palabra_3, palabra_1)
      elif len(palabra_1) > len(palabra_2):
        print("En orden alfabetico estan:", palabra_3, palabra_1, palabra_2)
      else:
        print("En orden alfabetico estan:", palabra_3, palabra_2, palabra_1)
    
    else: 
      print("La operacion introducida es desconocida, por favor empieze de nuevo")
      ej4()

             
def ej5():
    # Ejercicios de práctica con números
       
    '''
    Realice un programa que solicite ingresar tres valores de temperatura
    De las temperaturas ingresadas por consola determinar:
    1 - ¿Cuáles de ellas es la máxima temperatura ingresada?
    2 - ¿Cuáles de ellas es la mínima temperatura ingresada?
    3 - ¿Cuál es el promedio de las temperaturas ingresadas?

    En cada caso imprimir en pantalla el resultado  

    '''
    lista = []
    lista.append(int(input("Introduzca la primera temperatura (°C): ")))
    lista.append(int(input("Introduzca la segunda temperatura (°C): ")))
    lista.append(int(input("Introduzca la tercera temperatura (°C): ")))
    temperatura_maxima = -999
    temperatura_minima = 999    
    temperatura_promedio = 0
    for temperatura in lista:
      temperatura_promedio = temperatura_promedio + temperatura
      if temperatura > temperatura_maxima:
        temperatura_maxima = temperatura   
      if temperatura < temperatura_minima:
        temperatura_minima = temperatura   
    return print(
          "La temperatura mas alta registra es de: {}\n"
          "La temperatura mas baja registrada es de: {}\n"
          "El promedio de las tres temperaturas es de: {}"
                                                        .format(temperatura_maxima, temperatura_minima, (temperatura_promedio / len(lista))))    

if __name__ == '__main__':
    print("Ejercicios de práctica")
    #ej1()
    #ej2()
    #ej3()
    #ej4()
    ej5()
