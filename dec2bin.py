    while len(numero_binario) < numero_bits:      # añade 0's a la izquierda si hace falta
        numero_binario = "0" + numero_binario
    return numero_binario

# ----------------------------------------
# MAIN
# ----------------------------------------
if __name__ == "__main__":
    # Pide al usuario el número a convertir y el número de bits 
    numero_decimal = int(input("Escribe el número en decimal que quieres convertir: "))
    numero_bits = int(input("Cuantos bits tendrá el número binario: "))

    # se llama a la función dec2bin() para hacer la conversión
    numero_binario = dec2bin(numero_decimal, numero_bits)

    # Muestra por pantalla el resultado.
    # Para imprimir un entero es necesario convertirlo a string con str()
    print("El numero " + str(numero_decimal) + " es " + numero_binario + " en binario con " + str(numero_bits) + " bits.")