import math


def kMuMenosLambda(k, mu, lambd):
    kMuLambda = (k * mu) - lambd
    return kMuLambda


def kMuSobreKMuL(lambd, mu, k):
    resul = (k * mu) / kMuMenosLambda(k, mu, lambd)
    return resul

def factorialPotencia(p, lambd, mu, x):
    factorial = p / math.factorial(x)
    potencia = math.pow((lambd / mu), x)
    return factorial * potencia

def probSistemaVacio(lambd, mu, k):
    sumatoria = 0
    for n in range(k):
        sumatoria += factorialPotencia(1, lambd, mu, n)
    kMuLambda = factorialPotencia(1, lambd, mu, k) * kMuSobreKMuL(lambd, mu, k)
    probSisVacio = 1 / (sumatoria + kMuLambda)
    return probSisVacio

def probClienteEsperar(lambd, mu, k):
    probEsperar = factorialPotencia(
        1, lambd, mu, k) * kMuSobreKMuL(lambd, mu, k) * probSistemaVacio(lambd, mu, k)
    return probEsperar

def probNoEsperar(lambd, mu, k):
    return 1 - probClienteEsperar(lambd, mu, k)

def probHallarExactamenteNClientesSistema(lambd, mu, k, n):
    probNCliente = 0
    if(n <= k):
        probNCliente = factorialPotencia(probSistemaVacio(lambd, mu, k), lambd, mu, n)
    elif (n >= k):
        factorial = 1 / (math.factorial(k) * math.pow(k, (n-k)))
        potencia = math.pow((lambd/mu), n)
        probNCliente = factorial * potencia * probSistemaVacio(lambd, mu, k)
    return probNCliente

def probHallarMaxClientesSistema(lambd, mu, k, max):
    sumatoria = 0
    for n in range(max+1):
        sumatoria += probHallarExactamenteNClientesSistema(lambd, mu, k, n)
    return sumatoria

def probHallarMinClientesSistema(lambd, mu, k, min):
    sumatoria = 0
    for n in range(min):
        sumatoria += probHallarExactamenteNClientesSistema(lambd, mu, k, n)
    return 1 - sumatoria

def probHallarExactamenteNClientesCola(lambd, mu, k, n):
    probClienteN = probHallarExactamenteNClientesSistema(lambd, mu, k, n+k)
    return probClienteN

def probHallarMaxClientesCola(lambd, mu, k, max):
    sumatoria = 0
    for n in range(max+1+k):
        sumatoria += probHallarExactamenteNClientesSistema(lambd, mu, k, n)
    return sumatoria

def probHallarMinClientesCola(lambd, mu, k, min):
    sumatoria = 0
    for n in range(min+k):
        sumatoria += probHallarExactamenteNClientesSistema(lambd, mu, k, n)
    return 1 - sumatoria

def lambdaPorMu(x, lambd, mu, k):
    lMuK = x * mu * math.pow((lambd / mu), k)
    return lMuK * probSistemaVacio(lambd, mu, k)

def kMuLambda(lambd, mu, k):
    kMuMenosL = (k * mu) - lambd
    kMuL = math.factorial((k - 1)) * math.pow(kMuMenosL, 2) 
    return kMuL

def numEsperado(x, lambd, mu, k):
    return lambdaPorMu(x, lambd, mu, k) / kMuLambda(lambd, mu, k)

def numEsperadoClientesSistema(lambd, mu, k):
    nCliSistema = numEsperado(lambd, lambd, mu, k) + (lambd / mu)
    return nCliSistema

def numEsperadoClientesCola(lambd, mu, k):
    return numEsperado(lambd, lambd, mu, k)

def numEsperadoClientesColaNoVacia(lambd, mu, k):
    nCliColaNoVacia = numEsperadoClientesCola(lambd, mu, k) / probClienteEsperar(lambd, mu, k)
    return nCliColaNoVacia

def tiempoEsperadoSistema(lambd, mu, k):
    tEsperadoSistema = numEsperado(1, lambd, mu, k) + (1 / mu)
    return tEsperadoSistema

def tiempoEsperadoCola(lambd, mu, k):
    return numEsperado(1, lambd, mu, k)

def tiempoEsperadoColaNoVacia(lambd, mu, k):
    return tiempoEsperadoCola(lambd, mu, k) / probClienteEsperar(lambd, mu, k)


def prueba(lambd, mu, k):
    print("")
    print("Sistema Vacio Po        : ", probSistemaVacio(lambd, mu, k))
    print("Prob Esperar Pk         : ", probClienteEsperar(lambd, mu, k))
    print("Prob No Esperar Pne     : ", probNoEsperar(lambd, mu, k))
    print("")
    print("1 Usuario Sistema       : ", probHallarExactamenteNClientesSistema(lambd, mu, k, 1))
    print("Max 2 usuario Sistema   : ", probHallarMaxClientesSistema(lambd, mu, k, 2))
    print("Min 2 usuario Sistema   : ", probHallarMinClientesSistema(lambd, mu, k, 2))
    print("")
    print("2 Usuario Cola          : ", probHallarExactamenteNClientesCola(lambd, mu, k, 2))
    print("Max 2 usuario Cola      : ", probHallarMaxClientesCola(lambd, mu, k, 2))
    print("Min 1 usuario Cola      : ", probHallarMinClientesCola(lambd, mu, k, 1))
    print("")
    print("Clientes Sistema L      : ", numEsperadoClientesSistema(lambd, mu, k))
    print("Clientes Cola Lq        : ", numEsperadoClientesCola(lambd, mu, k))
    print("Cliente Cola NA Ln      : ", numEsperadoClientesColaNoVacia(lambd, mu, k))
    print("")
    print("Tiempo en sistema W     : ", tiempoEsperadoSistema(lambd, mu, k))
    print("Tiempo en cola Wq       : ", tiempoEsperadoCola(lambd, mu, k))
    print("Tiempo en cola NA Wn    : ", tiempoEsperadoColaNoVacia(lambd, mu, k))  


prueba(10, 7.5, 2)