import math

def lambdaSobreMu(lambd, mu):
    return lambd / mu

def factorialesPorN(lambd, mu, m, n):
    factorial = math.factorial(m) / (math.factorial(m - n) * math.factorial(n))
    potencia = math.pow(lambdaSobreMu(lambd, mu), n)
    return factorial * potencia

def factorialesPorK(lambd, mu, m, n, k):
    factorial = math.factorial(m) / (math.factorial(m - n) * math.factorial(k) * math.pow(k, (n-k)))
    potencia = math.pow(lambdaSobreMu(lambd, mu), n)
    return factorial * potencia

def probSistemaVacio(lambd, mu, m, k):
    sumatoriaN = 0
    sumatoriaK = 0
    for n in range(k):
        sumatoriaN += factorialesPorN(lambd, mu, m, n)
    
    for n in range (k, m+1):
        sumatoriaK += factorialesPorK(lambd, mu, m, n, k)
    
    probSisOcupado = 1 / (sumatoriaN + sumatoriaK)
    return probSisOcupado

def probHallarExactamenteNClientesSistema(lambd, mu, m, k, n):
    probNCliente = 0
    if(n >= 0 and n <= k):
        probNCliente = probSistemaVacio(lambd, mu, m, k) * factorialesPorN(lambd, mu, m, n)
    elif (n >= k and n <= m):
        probNCliente = probSistemaVacio(lambd, mu, m, k) * factorialesPorK(lambd, mu, m, n, k)
    return probNCliente

def probHallarMaxClientesSistema(lambd, mu, m, k, max):
    sumatoria = 0
    for n in range(max+1):
        sumatoria += probHallarExactamenteNClientesSistema(lambd, mu, m, k, n)
    return sumatoria

def probHallarMinClientesSistema(lambd, mu, m, k, min):
    sumatoria = 0
    for n in range(min):
        sumatoria += probHallarExactamenteNClientesSistema(lambd, mu, m, k, n)
    return 1 - sumatoria

def probHallarExactamenteNClientesCola(lambd, mu, m, k, n):
    probClienteN = probHallarExactamenteNClientesSistema(lambd, mu, m, k, n+k)
    return probClienteN

def probHallarMaxClientesCola(lambd, mu, m, k, max):
    sumatoria = 0
    for n in range(max+1+k):
        sumatoria += probHallarExactamenteNClientesSistema(lambd, mu, m, k, n)
    return sumatoria

def probHallarMinClientesCola(lambd, mu, m, k, min):
    sumatoria = 0
    for n in range(min+k):
        sumatoria += probHallarExactamenteNClientesSistema(lambd, mu, m, k, n)
    return 1 - sumatoria

def probSistemaOcupado(lambd, mu, m, k):
    sumatoria = 0
    for n in range(k, m+1):
        sumatoria += probHallarExactamenteNClientesSistema(lambd, mu, m, k, n)
    return sumatoria

def probNoEsperar(lambd, mu, m, k):
    return 1 - probSistemaOcupado(lambd, mu, m, k)

def numEsperadoClientesSistema(lambd, mu, m, k):
    nPorP = 0
    nMenosK = 0
    for n in range(k):
        nPorP += n * probHallarExactamenteNClientesSistema(lambd, mu, m, k, n)
    for n in range(k, m+1):
        nMenosK += (n - k) * probHallarExactamenteNClientesSistema(lambd, mu, m, k, n)
    kPorProbOcu = k  * probSistemaOcupado(lambd, mu, m, k)
    return nPorP + nMenosK + kPorProbOcu

def numEsperadoClientesCola(lambd, mu, m, k):
    cliEsperadoCola = 0
    for n in range(k, m+1):
        cliEsperadoCola += (n-k) * probHallarExactamenteNClientesSistema(lambd, mu, m, k, n)
    return cliEsperadoCola

def numEsperadoClienteColaNoVacia(lambd, mu, m, k):
    cliColaNoVacia = numEsperadoClientesCola(lambd, mu, m, k) / probSistemaOcupado(lambd, mu, m, k)
    return cliColaNoVacia

def tiempoEsperadoSistema(lambd, mu, m, k):
    tEsperadoSistema = tiempoEsperadoCola(lambd, mu, m, k) + (1 / mu)
    return tEsperadoSistema

def tiempoEsperadoCola(lambd, mu, m, k):
    tEsperadoCola = numEsperadoClientesCola(lambd, mu, m, k) / ((m - numEsperadoClientesSistema(lambd, mu, m, k)) * lambd)
    return tEsperadoCola

def tiempoEsperadoColaNoVacia(lambd, mu, m, k):
    tEsperadoColaNoVacia = tiempoEsperadoCola(lambd, mu, m, k) / probSistemaOcupado(lambd, mu, m, k)
    return tEsperadoColaNoVacia

print("")
print("Sistema Vacio Po        : ", probSistemaVacio(0.1, 0.5, 4, 2))
print("Sistema Ocupado Pe      : ", probSistemaOcupado(0.1, 0.5, 4, 2))
print("Prob No Esperar Pne     : ", probNoEsperar(0.1, 0.5, 4, 2))
print("")
print("1 Usuario Sistema       : ", probHallarExactamenteNClientesSistema(0.1, 0.5, 4, 2, 1))
print("Max 2 usuario Sistema   : ", probHallarMaxClientesSistema(0.1, 0.5, 4, 2, 2))
print("Min 2 usuario Sistema   : ", probHallarMinClientesSistema(0.1, 0.5, 4, 2, 2))
print("")
print("2 Usuario Cola          : ", probHallarExactamenteNClientesCola(0.1, 0.5, 4, 2, 2))
print("Max 2 usuario Cola      : ", probHallarMaxClientesCola(0.1, 0.5, 4, 2, 2))
print("Min 1 usuario Cola      : ", probHallarMinClientesCola(0.1, 0.5, 4, 2, 1))
print("")
print("Clientes Sistema L      : ", numEsperadoClientesSistema(0.1, 0.5, 4, 2))
print("Clientes Cola Lq        : ", numEsperadoClientesCola(0.1, 0.5, 4, 2))
print("Cliente Cola NA Ln      : ", numEsperadoClienteColaNoVacia(0.1, 0.5, 4, 2))
print("")
print("Tiempo en sistema W     : ", tiempoEsperadoSistema(0.1, 0.5, 4, 1))
print("Tiempo en cola Wq       : ", tiempoEsperadoCola(0.1, 0.5, 4, 1))
print("Tiempo en cola NA Wn    : ", tiempoEsperadoColaNoVacia(0.1, 0.5, 4, 1))