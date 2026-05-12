def dibujaTablero(ranura):
    """
    Función que imprime el tablero en pantalla.
    Recibe una lista con 10 elementos (índices 0 al 9).
    """
    print("\n-------------")
    for i in range(1, 10, 3):
        # Imprime las filas usando los índices 1-2-3, 4-5-6, 7-8-9
        print(f"| {ranura[i]} | {ranura[i+1]} | {ranura[i+2]} |")
        print("-------------")

# --- Bloque Principal ---

# 1. Creamos la lista.
# Ponemos un espacio ' ' en el índice 0 para ignorarlo,
# así el número 1 corresponde al índice 1.
tablero = [' ', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# 2. Mostramos un título
print("   TABLERO DE JUEGO")

# 3. Llamamos a la función para dibujarlo
dibujaTablero(tablero)
