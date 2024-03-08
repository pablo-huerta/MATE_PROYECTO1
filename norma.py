import math

def norm(v, p=2):
    """
    Calcula la p-norm o Norma Euclidana de un vector v.

    Parametros:
    - v (list): Lista de numeros que representan el vector.
    - p (float): La norma que se desea calcular (default 2, ya que es la norma Euclidiana).

    Returns:
    - float: El valor calculado de la norma 
    """
    if not isinstance(v, list) or not all(isinstance(x, (int, float)) for x in v):
        raise ValueError("Debe ser una lista de numeros")

    if p <= 0:
        raise ValueError("p debe de ser un numero positivo")

    norm_value = sum(abs(x) ** p for x in v) ** (1 / p)

    return norm_value

# Ejemplo de vector, aqui se puede colocar cualquier vector que usted desee calcular su norma.
vector = [4, 3]
euclidean_norm = norm(vector)  # Calcula la norma Euclidiana (p=2)
manhattan_norm = norm(vector, p=1)  # Calcula norma Manhattan (p=1)

print("Norma Euclidiana:", euclidean_norm)
print("Norma Manhattan:", manhattan_norm)
