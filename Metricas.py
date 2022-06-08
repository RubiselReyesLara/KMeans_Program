def Manhattan(observacion, cluster):
    d = 0
    for i in range(len(observacion)):
        d = d + abs(observacion[i] - cluster[i])
    return d

def Euclidiana(observacion, cluster):
    d = 0
    for i in range(len(observacion)):
        d = d + (observacion[i] - cluster[i]) ** 2
    return d ** 0.5


def Eucli_Normal(observacion, cluster):
    d = 0
    for i in range(len(observacion)):
        d = d + observacion[i]**2 - 2 * (observacion[i] * cluster[i]) + cluster[i]**2
    return d

def Sorense(observacion, clusters):
    d = 0
    x2 = 0
    y2 = 0
    for i in range(len(observacion)):
        arriba = arriba + observacion[i] * clusters[i]
        x2 = x2 + observacion[i] ** 2
        y2 = y2 + clusters[i] ** 2
    d = 2 * arriba / (x2 + y2)
    return d

def Sim_Coseno(observacion, cluster):
    d = 0
    arriba = 0.0
    abajo = 0.0
    x = 0.0
    y = 0.0
    for i in range(len(observacion)):
        arriba = arriba + observacion[i] * cluster[i]
        x = x + observacion[i]**2
        y = y + cluster[i]**2
        d = arriba / ((x * y)**0.5)
    return d

def Jaccard(observacion, cluster):
    d = 0
    arriba = 0.0
    x = 0.0
    y = 0.0
    for i in range(len(observacion)):
        arriba = arriba + observacion[i] * cluster[i]
        x = x + observacion[i]**2
        y = y + cluster[i]**2
        d = arriba / ((x + y) - arriba)
    return d