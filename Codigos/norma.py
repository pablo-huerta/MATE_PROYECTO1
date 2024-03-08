import math

def norma(v, p=None):
    """
    Calcula la norma p o la norma euclidiana de un vector v.

    :param v: Lista de números representando el vector.
    :param p: Valor de p para la norma p. Si no se proporciona, se calcula la norma euclidiana.
    :return: Valor de la norma p o la norma euclidiana.
    """
    if p is None:
        # Calcula la norma euclidiana (p por defecto es 2).
        return math.sqrt(sum(x**2 for x in v))
    else:
        # Calcula la norma p.
        return (sum(abs(x)**p for x in v))**(1/p)

# Ejemplos de uso:
vector = [10, 8]

# Norma Euclidiana (norma 2)
norma_euclidiana = norma(vector)
print(f"Norma Euclidiana: {norma_euclidiana}")

# Norma 1
norma_1 = norma(vector, p=1)
print(f"Norma 1: {norma_1}")

