"""
Actividad de programación  
Desarrolla un programa con un menú que permita convertir números entre bases, sumar y restar en binario, obtener complementos a 1 y a 2 y consultar códigos ASCII de letras mayúsculas.

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
        print("//////////////////////////////")
        print("DECIMAL a BINARIO")
        print("//////////////////////////////")
        print("1) Decimal a Binario>>>")
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

def op1():
    #Explicacion de la funcion op1 para mi equipo:
    print("BINARIO A HEXADECIMAL>>>")
    #Se utiliza un input de manera str para digitalizar el binario y ocupar 0 y 1 en posiciones diferentes.
    num_binario = input("Ingresa el numero binario: ")
    
    try: #se ocupa el try para evitar los errores comunes de que no seleccionen el 0 o el 1

        #Variable donde se guardara el numero que se transformo de binario a decimal
        #Esta funcion nos ayuda a cambiar de base en el ,2) esto ya viene incluido en el lenguaje de python y avisa a que base esta dicho num_binario y como pasarlo a un entero a base 10
        decimal = int(num_binario, 2)

        #se ocupa la variable hexadecimal para guardar el resultado de la funcion de hex(), que convierte el numero decimal que ya se habia guardado y convertirlo en hexadecimal
        #Python ya tiene agregado esta funcion, pero ocupa un prefijo 0x, se ocupa el [2:] para quitar ese prefijo, ya que inicia ocupando esos dos "espacios" (slicing)
        #Y pues el upper es pa que sea mayusculas los simbolos del sistema hexadecimal
        hexadecimal = hex(decimal)[2:].upper()
        
        print(f"El resultado en hexadecimal es: {hexadecimal}")
    except ValueError:
        print("Hay un error por favor ingresa un numero binario valido (solo ceros y unos).")

def op2():
    print("OCTAL A HEXADECIMAL>>>")
    num_octal = input("Ingresa el numero octal: ")
    
    try:
        #Aqui pues es lo mismo que en la funcion op2, ya que maneja la base 8 la cual toma como la variable num_octal en base 8, si hay un error pa eso esta el try
        decimal = int(num_octal, 8)
        #Aqui esta igual la misma parte de lo anterior 
        hexadecimal = hex(decimal)[2:].upper()

        print(f"El resultado en hexadecimal es: {hexadecimal}")
    except ValueError:
        print("Hay un error poor favor ingresa un numero octal valido (dígitos del 0 al 7).")


def op3():
    pass

def op4():
    pass

def op5():
    pass

def op6():
    pass

def op7():
    pass

def op8():
    pass

def main():

    while True:
        print("\n//////////////////////////////////////////////////////////////////////////////////")
        print("\tBienvenido al menu de PRACTICA DE\nLENGUAJE DE BAJO NIVEL")
        print("////////////////////////////////////////////////////////////////////////////////")
        print("\n1. Convertir de binario a octal.")
        print("2. Convertir de binario a hexadecimal. ")
        print("3. Convertir de octal a hexadecimal.  ")
        print("4. Convertir de hexadecimal a octal. ")
        print("5. Sumar dos números binarios. ")
        print("6. Restar dos números binarios. ")
        print("7. Obtener complemento a 1 y a 2. ")
        print("8. Convertir letras mayúsculas a ASCII decimal y binario.")
        print("9. Salir.  ")
        opcion_menu = int(input("Elige una opcion del 1-9: "))

        match opcion_menu:
            case 1: 
                op1()

            case 2:
                op2()

            case 3:
                op3()

            case 4:
                op4()

            case 5:
                op5()

            case 6:
                op6()

            case 7:
                op7()

            case 8:
                op8() 

            case 9:
                print("Saliendo del programa...")
                break               

            case _:
                print("Opcion no valida, Ingrese una opcion valida.") 

main()