import matplotlib.pyplot as plt

#PROGRAMA PARA GENERAR LAS GRAFICAS DE LA METRICA

# Definir valores de los parámetros
K1 = 1
K2 = 0
K3 = 1
K4 = 0
K5 = 0
Delay = 10  # microsegundos
REL = 200

# Calcular la métrica para diferentes valores de ancho de banda
BW_values = list(range(1, 1001))  # Ancho de banda de 1 a 1000 Mbps
metric_values = [256 * ((K1 * BW) / (K4 + REL)) for BW in BW_values]

# Graficar la métrica en función del ancho de banda
plt.plot(BW_values, metric_values)
plt.xlabel('Ancho de Banda (Mbps)')
plt.ylabel('Métrica')
plt.title('Métrica en función del Ancho de Banda')
plt.grid(True)
plt.show()