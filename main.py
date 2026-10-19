"""
Actividad de programación  
Desarrolla un programa con un menú que permita convertir números entre bases, sumar y restar en binario, obtener complementos a 1 y a 2 y consultar códigos ASCII de letras mayúsculas.  

Menú principal  
1. Convertir de binario a octal.  
2. Convertir de binario a hexadecimal.  
3. Convertir de octal a hexadecimal.  
4. Convertir de hexadecimal a octal.  
5. Sumar dos números binarios.  
6. Restar dos números binarios.  
7. Obtener complemento a 1 y a 2.  
8. Convertir letras mayúsculas a ASCII decimal y binario.  
9. Salir.  

Opciones 1 a 4 Conversiones entre bases  
Solicita un número en la base correspondiente a la opción elegida y muestra su equivalente en la base de destino. Identifica claramente la base de entrada y la del resultado.  

Opción 5 Suma de números binarios  
Solicita dos números binarios, realiza la suma y muestra el resultado en binario.  

Opción 6 Resta de números binarios  
Solicita dos números binarios, realiza la resta y muestra el resultado en binario. Para simplificar, valida que el primer número sea mayor o igual que el segundo; de lo contrario, solicita nuevamente los datos.  

Opción 7 Complemento a 1 y a 2  
Solicita un número decimal positivo entre 1 y 127. Convierte el número a binario de 8 bits, agregando ceros a la izquierda cuando sea necesario. Después:  
Obtén el complemento a 1 invirtiendo cada bit: cambia los ceros por unos y los unos por ceros.  
Obtén el complemento a 2 sumando 1 al complemento a 1.  
Muestra el número decimal, su binario de 8 bits y ambos complementos.  

Opción 8 Código ASCII de letras mayúsculas  
Solicita una o varias letras mayúsculas de la A a la Z, sin acentos ni Ñ. Recorre la entrada y muestra, por cada letra, su código ASCII decimal y su representación binaria de 8 bits.  

Opción 9 Salir  
Finaliza la ejecución del programa y muestra un mensaje de despedida.  

Requisitos generales  
El menú debe repetirse hasta que el usuario seleccione la opción 9.  
Valida las opciones del menú y los datos ingresados. Si hay un error, muestra un mensaje y solicita nuevamente el dato.  
Acepta únicamente 0 y 1 en binario; de 0 a 7 en octal; y de 0 a 9 y de A a F en hexadecimal.  
Utiliza números enteros no negativos para las conversiones, la suma y la resta. En la opción de complementos, respeta el rango de 1 a 127.  
Después de cada operación, permite regresar al menú principal.  
Implementa cada opción en una función o método.  

"""
"""
def LOGICA1():
    binario = ""
    try: 
        numero = int(input("Ingrese su numero entero positivo: "))

        if 0 <= numero <= 999:
            if numero == 0:
                binario = "0"
            else:
                while numero > 0:
                    if numero % 2 == 0:
                        binario = "0" + binario
                    else:
                        binario = "1" + binario
                    numero = numero // 2
                    
            print("Este es el numero en binario:", binario)
        elif numero > 999:
            print("Ingrese un valor positivo, hasta 3 cifras como maximo.")
            LOGICA1()
        elif numero < 0:
            print("Ingrese un numero positivo")
            LOGICA1()
    except ValueError:
        print ("Ingrese una opcion valida")
        LOGICA1()

def menu():
    while True:
        print("\n//////////////////////////////")
        print("\tDECIMAL a BINARIO")
        print("//////////////////////////////")
        print("\n1) Decimal a Binario>>>")
        print("2) Salir del programa>>>")

        try:
            op = int(input("Opcion: "))

        
            match op:
                case 1:
                    LOGICA1()
                case 2:
                    print("Saliendo del programa...")
                    break
        except ValueError: 
            print("Opcion no valida.")
menu()

"""

