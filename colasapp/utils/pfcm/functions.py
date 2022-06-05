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

def numEsperadoClientesColaNoVacia(lambd, mu, m, k):
    cliColaNoVacia = numEsperadoClientesCola(lambd, mu, m, k) / probSistemaOcupado(lambd, mu, m, k)
    return cliColaNoVacia

def tiempoEsperadoSistema(lambd, mu, m, k):
    tEsperadoSistema = tiempoEsperadoCola(lambd, mu, m, k) + (1 / mu)
    return tEsperadoSistema

def tiempoEsperadoCola(lambd, mu, m, k):
    mMenosL = m - numEsperadoClientesSistema(lambd, mu, m, k)
    tEsperadoCola = numEsperadoClientesCola(lambd, mu, m, k) / (mMenosL * lambd)
    return tEsperadoCola

def tiempoEsperadoColaNoVacia(lambd, mu, m, k):
    tEsperadoColaNoVacia = tiempoEsperadoCola(lambd, mu, m, k) / probSistemaOcupado(lambd, mu, m, k)
    return tEsperadoColaNoVacia

def prueba(lambd, mu, m, k):
    print("")
    print("Sistema Vacio Po        : ", probSistemaVacio(lambd, mu, m, k))
    print("Sistema Ocupado Pe      : ", probSistemaOcupado(lambd, mu, m, k))
    print("Prob No Esperar Pne     : ", probNoEsperar(lambd, mu, m, k))
    print("")
    print("1 Usuario Sistema       : ", probHallarExactamenteNClientesSistema(lambd, mu, m, k, 1))
    print("Max 2 usuario Sistema   : ", probHallarMaxClientesSistema(lambd, mu, m, k, 2))
    print("Min 2 usuario Sistema   : ", probHallarMinClientesSistema(lambd, mu, m, k, 2))
    print("")
    print("2 Usuario Cola          : ", probHallarExactamenteNClientesCola(lambd, mu, m, k, 2))
    print("Max 2 usuario Cola      : ", probHallarMaxClientesCola(lambd, mu, m, k, 2))
    print("Min 1 usuario Cola      : ", probHallarMinClientesCola(lambd, mu, m, k, 1))
    print("")
    print("Clientes Sistema L      : ", numEsperadoClientesSistema(lambd, mu, m, k))
    print("Clientes Cola Lq        : ", numEsperadoClientesCola(lambd, mu, m, k))
    print("Cliente Cola NA Ln      : ", numEsperadoClientesColaNoVacia(lambd, mu, m, k))
    print("")
    print("Tiempo en sistema W     : ", tiempoEsperadoSistema(lambd, mu, m, k))
    print("Tiempo en cola Wq       : ", tiempoEsperadoCola(lambd, mu, m, k))
    print("Tiempo en cola NA Wn    : ", tiempoEsperadoColaNoVacia(lambd, mu, m, k))

prueba(0.1, 0.5, 4, 2)
