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

def op5():
    binario1 = ""
    binario2 = ""

    try:
        binario1 = input("Ingresa el primer número binario: ")
        binario2 = input("Ingresa el segundo número binario: ")

        resultado = ""
        acarreo = 0

        i = len(binario1) - 1
        j = len(binario2) - 1

        while i >= 0 or j >= 0:

            bit1 = int(binario1[i]) if i >= 0 else 0
            bit2 = int(binario2[j]) if j >= 0 else 0

            suma = bit1 + bit2 + acarreo

            if suma == 0:
                resultado = "0" + resultado
                acarreo = 0

            elif suma == 1:
                resultado = "1" + resultado
                acarreo = 0

            elif suma == 2:
                resultado = "0" + resultado
                acarreo = 1

            elif suma == 3:
                resultado = "1" + resultado
                acarreo = 1

            i -= 1
            j -= 1

        if acarreo == 1:
            resultado = "1" + resultado

        print("Resultado:", resultado)

    except ValueError:
        print("Ingrese un valor valido")
        op5()

def menu():
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

        try:
            op = int(input("Opcion: "))

        
            match op:
                case 1:
                    print("En proceso...")
                case 2:
                    op1()
                case 3:
                    op2()
    
                case 4:
                    print("En proceso...")
    
                case 5:
                    op5()
    
                case 6:
                    print("En proceso...")
    
                case 7:
                    print("En proceso...")
    
                case 8:
                    print("En proceso...")
    
                case 9:
                    print("Saliendo del programa...")
                    break               
    
                case _:
                    print("Opcion no valida, Ingrese una opcion valida.") 
                    
        except ValueError: 
            print("Opcion no valida.")
            
menu()
