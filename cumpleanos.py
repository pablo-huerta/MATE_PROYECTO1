import random

def generate_birthdays(group_size):
    """
    Genera cumpleaños aleatorios para un grupo.

    Parameters:
    - group_size (int): Numero de personas en el grupo.

    Returns:
    - list: Lista de cumpleaños aleatorios.
    """
    return [random.randint(1, 365) for _ in range(group_size)]

def has_shared_birthday(birthdays):
    """
    Revisa si hay cumpleaños en común en el grupo.

    Parameters:
    - birthdays (list): Lista de cumpleaños.

    Returns:
    - bool: True si hay un cumpleaños en comun, False en otro caso.
    """
    return len(birthdays) != len(set(birthdays))

def birthday_paradox_experiment(num_experiments, group_sizes):
    """
    Prueba la paradoja del cumpelaños para grupos de diferente tamaño

    Parameters:
    - num_experiments (int): Numero de experimentos a probar para cada grupo.
    - group_sizes (list): Lista de tamaños de grupo a porbar

    Returns:
    - dict: Resultados de cada grupo.
    """
    results = {}

    for size in group_sizes:
        success_count = 0

        for _ in range(num_experiments):
            birthdays = generate_birthdays(size)
            if has_shared_birthday(birthdays):
                success_count += 1

        probability = success_count / num_experiments * 100
        results[size] = probability

    return results

def main():
    num_experiments = 10000
    group_sizes = list(range(5, 110, 5))

    results = birthday_paradox_experiment(num_experiments, group_sizes)

    print("Resultados:")
    for size, probability in results.items():
        print(f"Tamaño del grupo {size}: Probabilidad de que comparatan cumpleaños = {probability:.4f}%")

if __name__ == "__main__":
    main()
