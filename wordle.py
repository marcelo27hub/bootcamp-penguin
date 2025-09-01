palabra_del_dia = "panteon"
cantidad_de_letras = 7
intentos = 5

# Función para verificar letras
def palabra_a_verificar(palabra_ingresada_usuario, palabra_del_dia):
    letras_verificadas = []
    for posicion in range(cantidad_de_letras):
        letra_en_posicion_correcta = palabra_ingresada_usuario[posicion] == palabra_del_dia[posicion]
        letra_en_posicion_incorrecta = palabra_ingresada_usuario[posicion] in palabra_del_dia

        if letra_en_posicion_correcta:
            letras_verificadas.append(f"[{palabra_ingresada_usuario[posicion]}]")
        elif letra_en_posicion_incorrecta:
            letras_verificadas.append(f"({palabra_ingresada_usuario[posicion]})")
        else:
            letras_verificadas.append(palabra_ingresada_usuario[posicion])
    return letras_verificadas

# Grilla para guardar todos los intentos
grilla = []

# Juego
while intentos > 0:
    palabra_ingresada_usuario = input("Ingrese una palabra: ").lower()

    while len(palabra_ingresada_usuario) != cantidad_de_letras:
        print("Ingrese una palabra de 7 letras, por favor.")
        palabra_ingresada_usuario = input("Intenta de nuevo: ").lower()

    if palabra_ingresada_usuario == palabra_del_dia:
        resultado = palabra_a_verificar(palabra_ingresada_usuario, palabra_del_dia)
        grilla.append(resultado)
        print("Ganastee!")
        break
    else:
        resultado = palabra_a_verificar(palabra_ingresada_usuario, palabra_del_dia)
        grilla.append(resultado)
        print(resultado)
        intentos -= 1
        print(f"Lo siento te quedan {intentos} ")

# Mostrar resultado final
print("Resultado de tus intentos:")
for fila in grilla:
    print(fila)

if intentos == 0:
    print("Perdiste la palabra era: ", palabra_del_dia)