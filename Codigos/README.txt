# MATE_PROYECTO1
Martinez Huerta Pablo 
Sanchez Flores Camila 

PARADOJA DEL CUMPLEAÑOS:
Este programa de python hace una simulación de la paradoja del cumpleaños. El programa consta de distintas funciones que cumplen con tareas determinadas, a continuación se enlistan:
    1.Generación Aleatoria de Cumpleaños: La función generar_cumpleaños(n) genera una lista de n cumpleaños aleatorios, representados como números enteros entre 1 y 365 (ignorando los años bisiestos para simplificar).

    2.Verificación de Duplicados: La función hay_duplicados(cumpleaños) verifica si hay al menos dos cumpleaños iguales en la lista proporcionada.

    3.Simulación de la Paradoja: La función principal simulacion_paradoja_cumpleaños(n_experimentos, tamaños_grupos) realiza simulaciones para diferentes tamaños de grupos. Por cada tamaño de grupo especificado, se generan aleatoriamente cumpleaños en n_experimentos ocasiones y se calcula la probabilidad de que al menos dos personas compartan el mismo cumpleaños.

    4.Resultados e Impresión: Los resultados se imprimen en la consola, mostrando la probabilidad estimada para cada tamaño de grupo.

Los parametros que se pueden ajustar son:
    -n_experimentos:Número de experimentos realizados para cada tamaño de grupo. Es decir Cada        experimento implica la generación aleatoria de cumpleaños para un grupo de personas y la verificación de si al menos dos de ellas comparten el mismo cumpleaños.

    Por ejemplo, si tienes un tamaño de grupo de 20 personas y decides realizar 1000 experimentos, significa que el programa generará aleatoriamente 20 cumpleaños para un grupo de 20 personas 1000 veces. En cada uno de esos experimentos, se verificará si al menos dos personas comparten el mismo cumpleaños. El número de veces que se encuentra esta coincidencia se utilizará para calcular la probabilidad para ese tamaño de grupo específico.
    Ajusta este valor para obtener resultados más precisos a costa de un mayor tiempo de ejecución.

    -tamaños_grupos: la lista de tamaños de grupos en los que se probó el experimento

El código se ejecuta desde la terminal con estando dentro del directorio ~/MATE II/MATE_PROYECTO1 con el comando python3 cumpleanos.py

CALCULADORA DE NORMA:
Este programa en Python proporciona una función llamada norma para calcular la norma p o la norma euclidiana de un vector representado como una lista de números.
Funcionalidades

    1.Norma Euclidiana (Norma 2): La función calcula la norma euclidiana de un vector si no se proporciona el parámetro p.

    2.Norma p Personalizada: Si se proporciona el parámetro p, la función calcula la norma p del vector.

Parámetros Ajustables

    -v: Lista de números que representa el vector.

    -p: Parámetro opcional que indica el valor de p para la norma p. Si no se proporciona, se calcula la norma euclidiana.(p=2)

El programa se ejecuta con el comando pyhton3 norma.py

GENERADOR GRAFICAS:
Este programa genera gráficas de la métrica en función del ancho de banda utilizando los parámetros proporcionados. 
La métrica se calcula según la siguiente fórmula:

Métrica = 256 * ((K1 * Ancho_de_Banda) / (K4 + REL))

Donde:

    K1, K2, K3, K4, K5: son parámetros definidos en el programa.
    Delay: es el retardo en microsegundos.
    REL: es la relación.
    Ancho_de_Banda: varía de 1 a 1000 Mbps.

-Uso:

Para ejecutar el programa y generar la gráfica de la métrica en función del ancho de banda:
python3 generadorGraficas.py

- Requisitos

El programa utiliza la biblioteca matplotlib para generar la gráfica. 