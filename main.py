def op1():
    # Explicacion de la funcion op1 para mi equipo:
    print("BINARIO A HEXADECIMAL>>>")
    # Se utiliza un input de manera str para digitalizar el binario y ocupar 0 y 1 en posiciones diferentes.
    num_binario = input("Ingresa el numero binario: ")
    
    try: # se ocupa el try para evitar los errores comunes de que no seleccionen el 0 o el 1
        # Variable donde se guardara el numero que se transformo de binario a decimal
        # Esta funcion nos ayuda a cambiar de base en el ,2) esto ya viene incluido en el lenguaje de python y avisa a que base esta dicho num_binario y como pasarlo a un entero a base 10
        decimal = int(num_binario, 2)

        # se ocupa la variable hexadecimal para guardar el resultado de la funcion de hex(), que convierte el numero decimal que ya se habia guardado y convertirlo en hexadecimal
        # Python ya tiene agregado esta funcion, pero ocupa un prefijo 0x, se ocupa el [2:] para quitar ese prefijo, ya que inicia ocupando esos dos "espacios" (slicing)
        # Y pues el upper es pa que sea mayusculas los simbolos del sistema hexadecimal
        hexadecimal = hex(decimal)[2:].upper()
        
        print(f"El resultado en hexadecimal es: {hexadecimal}")
    except ValueError:
        print("Hay un error por favor ingresa un numero binario valido (solo ceros y unos).")

def op2():
    print("OCTAL A HEXADECIMAL>>>")
    num_octal = input("Ingresa el numero octal: ")
    
    try:
        # Aqui pues es lo mismo que en la funcion op2, ya que maneja la base 8 la cual toma como la variable num_octal en base 8, si hay un error pa eso esta el try
        decimal = int(num_octal, 8)
        # Aqui esta igual la misma parte de lo anterior 
        hexadecimal = hex(decimal)[2:].upper()

        print(f"El resultado en hexadecimal es: {hexadecimal}")
    except ValueError:
        print("Hay un error poor favor ingresa un numero octal valido (dígitos del 0 al 7).")

def op5():
    # Estos son para guardar los binarios
    binario1 = ""
    binario2 = ""

    try:
        # Esto pide los binarios
        binario1 = input("Ingresa el primer número binario: ")
        binario2 = input("Ingresa el segundo número binario: ")
        
        # Esto guarda los resultados y el acarreo
        resultado = ""
        acarreo = 0

        # Esto consigue la posicion de cada digito, se va a usar para ir recorriendo los numeros a sumar
        i = len(binario1) - 1
        j = len(binario2) - 1

        # Recorre de derecha a izquierda mientras tenga numeros, es para ir sumand dos digitos en la misma "columna"
        while i >= 0 or j >= 0:

            # Consigue el digito actual, si no hya, utiliza 0
            bit1 = int(binario1[i]) if i >= 0 else 0
            bit2 = int(binario2[j]) if j >= 0 else 0

            # Esto es la suma de los digitos mas el acarreo en caso de tener
            suma = bit1 + bit2 + acarreo

            # Si la suma dio 0, el resultado es 0 y sin acarreo, se le agrega a la derecha el resultado anterior y se convierte en el nuevo resultado
            if suma == 0:
                resultado = "0" + resultado
                acarreo = 0

            # Si la suma dio 1, el resultado es 1 y sin acarreo, se le agrega a la derecha el resultado anterior y se convierte en el nuevo resultado
            elif suma == 1:
                resultado = "1" + resultado
                acarreo = 0
            # Si la suma dio 2, el resultado es 0 y con acarreo de 1, se le agrega a la derecha el resultado anterior y se convierte en el nuevo resultado
            elif suma == 2:
                resultado = "0" + resultado
                acarreo = 1

            # Si la suma dio 3, el resultado es 1 y con acarreo de 1, se le agrega a la derecha el resultado anterior y se convierte en el nuevo resultado
            elif suma == 3:
                resultado = "1" + resultado
                acarreo = 1

            # Avanza a las posiciones anteriores, ya que la suma es de derecha a izquierda, se mueven a la izquierda
            i -= 1
            j -= 1

        # Si todavia hay un acarreo al final, se coloca y a la derecha se le agrega todo el resultado y se convierte en el nuevo resultado
        if acarreo == 1:
            resultado = "1" + resultado

        # Imprime el resultado
        print("Resultado:", resultado)

    # Por si algun dato esta ma puesto, te avisa y reinicia
    except ValueError:
        print("Ingrese un valor valido")
        op5()

def op6():
    # Esta función realiza la resta de dos números binarios (binario1 - binario2)
    # utilizando el algoritmo de resta bit a bit.
    print("RESTAR DOS NÚMEROS BINARIOS>>>")
    
    binario1 = input("Ingresa el primer número binario (Minuendo): ")
    binario2 = input("Ingresa el segundo número binario (Sustraendo): ")

    # Validación de entrada para asegurar que solo contenga 0s y 1s
    if not set(binario1).issubset({'0', '1'}) or not set(binario2).issubset({'0', '1'}):
        print("Error: Por favor ingresa números binarios válidos (solo ceros y unos).")
        return

    # Verificamos si el resultado será negativo en base al valor decimal
    es_negativo = False
    if int(binario1, 2) < int(binario2, 2):
        es_negativo = True
        # Si el resultado es negativo, invertimos el orden para hacer la resta (mayor - menor)
        # y al final le agregamos el signo menos "-"
        binario1, binario2 = binario2, binario1

    resultado = ""
    prestamo = 0

    # Índices para recorrer las cadenas de derecha a izquierda
    i = len(binario1) - 1
    j = len(binario2) - 1

    # Procesamiento bit por bit
    while i >= 0 or j >= 0:
        # Obtenemos el bit actual; si la cadena ya se terminó, asumimos 0
        bit1 = int(binario1[i]) if i >= 0 else 0
        bit2 = int(binario2[j]) if j >= 0 else 0

        # Aplicamos el préstamo actual al bit del minuendo
        diferencia = bit1 - prestamo - bit2

        # Análisis de casos de la resta:
        if diferencia == 0:
            resultado = "0" + resultado
            prestamo = 0
        elif diferencia == 1:
            resultado = "1" + resultado
            prestamo = 0
        elif diferencia == -1:
            # Necesitamos pedir prestado a la siguiente posición de la izquierda (base 2 -> suma 2)
            resultado = "1" + resultado
            prestamo = 1
        elif diferencia == -2:
            # Ocurre cuando bit1=0, prestamo=1 y bit2=1 (-1 - 1 = -2)
            resultado = "0" + resultado
            prestamo = 1

        # Mover los punteros hacia la izquierda
        i -= 1
        j -= 1

    # Eliminamos los ceros a la izquierda sobrantes (ej. "0010" -> "10")
    resultado = resultado.lstrip('0')
    if resultado == "":
        resultado = "0"

    # Si la resta era negativa, agregamos el signo "-"
    if es_negativo:
        resultado = "-" + resultado

    print(f"El resultado de la resta es: {resultado}")

def menu():
    while True:
        print("\n//////////////////////////////////////////////////////////////////////////////////")
        print("\tBienvenido al menu de PRACTICA DE\nLENGUAJE DE BAJO NIVEL")
        print("//////////////////////////////////////////////////////////////////////////////////")
        print("\n1. Convertir de binario a octal.")
        print("2. Convertir de binario a hexadecimal.")
        print("3. Convertir de octal a hexadecimal.")
        print("4. Convertir de hexadecimal a octal.")
        print("5. Sumar dos números binarios.")
        print("6. Restar dos números binarios.")
        print("7. Obtener complemento a 1 y a 2.")
        print("8. Convertir letras mayúsculas a ASCII decimal y binario.")
        print("9. Salir.")

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
                    op6()
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
