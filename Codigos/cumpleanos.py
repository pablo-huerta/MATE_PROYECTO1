import random

def generar_cumpleaños(n):
    """Genera n cumpleaños aleatorios."""
    cumpleaños = [random.randint(1, 365) for _ in range(n)]
    return cumpleaños

def hay_duplicados(cumpleaños):
    """Verifica si hay al menos dos cumpleaños iguales en la lista."""
    return len(cumpleaños) != len(set(cumpleaños))

def simulacion_paradoja_cumpleaños(n_experimentos, tamaños_grupos):
    """Realiza simulaciones de la paradoja del cumpleaños para diferentes tamaños de grupos."""
    for n in tamaños_grupos:
        coincidencias = 0
        for _ in range(n_experimentos):
            cumpleaños_grupo = generar_cumpleaños(n)
            if hay_duplicados(cumpleaños_grupo):
                coincidencias += 1

        probabilidad = coincidencias / n_experimentos * 100
        print(f"Para un grupo de {n} personas, la probabilidad de tener al menos dos con el mismo cumpleaños es aproximadamente: {probabilidad:.4f}%")

if __name__ == "__main__":
    n_experimentos = 10000  # Número de experimentos por cada tamaño de grupo
    tamaños_grupos = list(range(5, 110, 5))  # Tamaños de grupos a probar (5, 10, 15, ..., 100)

    simulacion_paradoja_cumpleaños(n_experimentos, tamaños_grupos)
