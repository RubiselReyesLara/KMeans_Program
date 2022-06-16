import Metricas

ARCHIVO = open('datos\\100datos.txt', 'r')
VECTOR = list()

# Leo la data
while linea := ARCHIVO.readline():
    VECTOR.append(eval(linea.rstrip()))
ARCHIVO.close()

contador = 0
clusters = list()
clases = list()

# Clusters iniciales
clusters.append(VECTOR[3][1:])
clusters.append(VECTOR[10][1:])
clusters.append(VECTOR[12][1:])

print(f'Clusters iniciales: {clusters}')

while True: 
    minimos_maximos = list()
    distancias = [list() for i in range(len(VECTOR))]
    indices = list()

    print(f'Iteracion: {contador + 1}')

    for j in range(len(VECTOR)): # Cada elemento del vector
        for cluster in clusters: # Tomando a cada cluster...
            distancias[j].append(Metricas.Euclidiana(VECTOR[j][1:], cluster))
        minimos_maximos.append(distancias[j].index(min(distancias[j]))) # Se obtiene el indice de la distancia minima segun el caso
    
    clases.append(minimos_maximos)
    print(f'K = {contador + 1}: {minimos_maximos}')

    for i in range(len(clusters)): # Para cada iteracion de cluster
        sumatoria_variables = [0 for i in range(len(VECTOR[0][1:]))]
        indices = [x for x, y in enumerate(minimos_maximos) if y == i] # x tal que x sea el indice de y, donde y sea igual a i
        for k in indices: # Para cada indice perteneciente a un cluster => 0 [2,4,5...], 1, 2
            temporal = VECTOR[k][1:] # Se toma el vector en ese indice
            for l in range(len(temporal)): # Se obtienen las variables
                sumatoria_variables[l] = sumatoria_variables[l] + temporal[l] # Sumatoria de cada variable en n posicion
        
        clusters[i] = [x/len(indices) for x in sumatoria_variables] # Obtener promedio en base al número de indice recopilado

    if contador > 0:
        if clases[-1] == clases[-2]: # Comparo si las dos ultimas clases son iguales, si no, se rompe y termina el while
            print(f'KMeans se ha detenido en K = {contador + 1}')
            print(f'Clases = {clases}')
            print(f'Centroides finales = {clusters}')
            break
    
    contador = contador + 1