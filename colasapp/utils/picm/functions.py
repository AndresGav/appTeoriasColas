import math


def kMuMenosLambdaPICM(k, mu, lambd):
    kMuLambda = (k * mu) - lambd
    return kMuLambda


def kMuSobreKMuLPICM(lambd, mu, k):
    resul = (k * mu) / kMuMenosLambdaPICM(k, mu, lambd)
    return resul

def factorialPotenciaPICM(p, lambd, mu, x):
    factorial = p / math.factorial(x)
    potencia = math.pow((lambd / mu), x)
    return factorial * potencia

def probSistemaVacioPICM(lambd, mu, k):
    print("LLEGAMOS !!! A LA FUNCION")
    sumatoria = 0
    for n in range(k):
        sumatoria += factorialPotenciaPICM(1, lambd, mu, n)
    kMuLambda = factorialPotenciaPICM(1, lambd, mu, k) * kMuSobreKMuLPICM(lambd, mu, k)
    probSisVacio = 1 / (sumatoria + kMuLambda)
    print("PROBABILIDAD SISTEMA VACIO", probSisVacio)
    return probSisVacio

def probClienteEsperarPICM(lambd, mu, k):
    probEsperar = factorialPotenciaPICM(
        1, lambd, mu, k) * kMuSobreKMuLPICM(lambd, mu, k) * probSistemaVacioPICM(lambd, mu, k)
    return probEsperar

def probNoEsperarPICM(lambd, mu, k):
    return 1 - probClienteEsperarPICM(lambd, mu, k)

def probHallarExactamenteNClientesSistemaPICM(lambd, mu, k, n):
    probNCliente = 0
    if(n <= k):
        probNCliente = factorialPotenciaPICM(probSistemaVacioPICM(lambd, mu, k), lambd, mu, n)
    elif (n >= k):
        factorial = 1 / (math.factorial(k) * math.pow(k, (n-k)))
        potencia = math.pow((lambd/mu), n)
        probNCliente = factorial * potencia * probSistemaVacioPICM(lambd, mu, k)
    return probNCliente

def probHallarMaxClientesSistemaPICM(lambd, mu, k, max):
    sumatoria = 0
    for n in range(max+1):
        sumatoria += probHallarExactamenteNClientesSistemaPICM(lambd, mu, k, n)
    return sumatoria

def probHallarMinClientesSistemaPICM(lambd, mu, k, min):
    sumatoria = 0
    for n in range(min):
        sumatoria += probHallarExactamenteNClientesSistemaPICM(lambd, mu, k, n)
    return 1 - sumatoria

def probHallarExactamenteNClientesColaPICM(lambd, mu, k, n):
    probClienteN = probHallarExactamenteNClientesSistemaPICM(lambd, mu, k, n+k)
    return probClienteN

def probHallarMaxClientesColaPICM(lambd, mu, k, max):
    sumatoria = 0
    for n in range(max+1+k):
        sumatoria += probHallarExactamenteNClientesSistemaPICM(lambd, mu, k, n)
    return sumatoria

def probHallarMinClientesColaPICM(lambd, mu, k, min):
    sumatoria = 0
    for n in range(min+k):
        sumatoria += probHallarExactamenteNClientesSistemaPICM(lambd, mu, k, n)
    return 1 - sumatoria

def lambdaPorMuPICM(x, lambd, mu, k):
    lMuK = x * mu * math.pow((lambd / mu), k)
    return lMuK * probSistemaVacioPICM(lambd, mu, k)

def kMuLambdaPICM(lambd, mu, k):
    kMuMenosL = (k * mu) - lambd
    kMuL = math.factorial((k - 1)) * math.pow(kMuMenosL, 2) 
    return kMuL

def numEsperadoPICM(x, lambd, mu, k):
    return lambdaPorMuPICM(x, lambd, mu, k) / kMuLambdaPICM(lambd, mu, k)

def numEsperadoClientesSistemaPICM(lambd, mu, k):
    nCliSistema = numEsperadoPICM(lambd, lambd, mu, k) + (lambd / mu)
    return nCliSistema

def numEsperadoClientesColaPICM(lambd, mu, k):
    return numEsperadoPICM(lambd, lambd, mu, k)

def numEsperadoClientesColaNoVaciaPICM(lambd, mu, k):
    nCliColaNoVacia = numEsperadoClientesColaPICM(lambd, mu, k) / probClienteEsperarPICM(lambd, mu, k)
    return nCliColaNoVacia

def tiempoEsperadoSistemaPICM(lambd, mu, k):
    tEsperadoSistema = numEsperadoPICM(1, lambd, mu, k) + (1 / mu)
    return tEsperadoSistema

def tiempoEsperadoColaPICM(lambd, mu, k):
    return numEsperadoPICM(1, lambd, mu, k)

def tiempoEsperadoColaNoVaciaPICM(lambd, mu, k):
    return tiempoEsperadoColaPICM(lambd, mu, k) / probClienteEsperarPICM(lambd, mu, k)


def prueba(lambd, mu, k):
    print("")
    print("Sistema Vacio Po        : ", probSistemaVacioPICM(lambd, mu, k))
    print("Prob Esperar Pk         : ", probClienteEsperarPICM(lambd, mu, k))
    print("Prob No Esperar Pne     : ", probNoEsperarPICM(lambd, mu, k))
    print("")
    print("1 Usuario Sistema       : ", probHallarExactamenteNClientesSistemaPICM(lambd, mu, k, 1))
    print("Max 2 usuario Sistema   : ", probHallarMaxClientesSistemaPICM(lambd, mu, k, 2))
    print("Min 2 usuario Sistema   : ", probHallarMinClientesSistemaPICM(lambd, mu, k, 2))
    print("")
    print("2 Usuario Cola          : ", probHallarExactamenteNClientesColaPICM(lambd, mu, k, 2))
    print("Max 2 usuario Cola      : ", probHallarMaxClientesColaPICM(lambd, mu, k, 2))
    print("Min 1 usuario Cola      : ", probHallarMinClientesColaPICM(lambd, mu, k, 1))
    print("")
    print("Clientes Sistema L      : ", numEsperadoClientesSistemaPICM(lambd, mu, k))
    print("Clientes Cola Lq        : ", numEsperadoClientesColaPICM(lambd, mu, k))
    print("Cliente Cola NA Ln      : ", numEsperadoClientesColaNoVaciaPICM(lambd, mu, k))
    print("")
    print("Tiempo en sistema W     : ", tiempoEsperadoSistemaPICM(lambd, mu, k))
    print("Tiempo en cola Wq       : ", tiempoEsperadoColaPICM(lambd, mu, k))
    print("Tiempo en cola NA Wn    : ", tiempoEsperadoColaNoVaciaPICM(lambd, mu, k))  


prueba(10, 7.5, 2)