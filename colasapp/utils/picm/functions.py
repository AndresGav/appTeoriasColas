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
    sumatoria = 0
    for n in range(k):
        sumatoria += factorialPotenciaPICM(1, lambd, mu, n)
    kMuLambda = factorialPotenciaPICM(1, lambd, mu, k) * kMuSobreKMuLPICM(lambd, mu, k)
    probSisVacio = 1 / (sumatoria + kMuLambda)
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
    nCliSistema = numEsperadoPICM(1, lambd, mu, k) + (lambd / mu)
    return nCliSistema

def numEsperadoClientesColaPICM(lambd, mu, k):
    return numEsperadoPICM(1, lambd, mu, k)

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

# FORMULAS DE COSTOS
# Costo Diario por el Tiempo de Espera en Cola
def costoTiempoEsperaEnCola(lambd, mu, h, k, cte):
    costoTiempoEspera = lambd * h * tiempoEsperadoColaPICM(lambd, mu, k) * cte
    return costoTiempoEspera

# Costo Diario por el Tiempo en el Sistema 
def costoTiempoEnSistema(lambd, mu, h, k, cts):
    costoTiempoEnSistema = lambd * h * tiempoEsperadoSistemaPICM(lambd, mu, k) * cts
    return costoTiempoEnSistema

# Costo Diario por el Tiempo de Servicio
def costoTiempoServicio(lambd, mu, h, ctse):
    costoTiempoDeServicio = lambd * h * (1/mu) * ctse
    return costoTiempoDeServicio

# Costo Diario del Servidor
def costoDiarioServidor(k, cs):
    return k * cs

# Costo Total Diario del Sistema
def costoTotalSistema(lambd, mu, h, k, cte, cts, ctse, cs):
    costoTotal = costoTiempoEsperaEnCola(lambd, mu, h, k, cte) + costoTiempoEnSistema(
        lambd, mu, h, k, cts) + costoTiempoServicio(lambd, mu, h, ctse) + costoDiarioServidor(k, cs)
    return costoTotal

def prueba(lambd, mu, k):
    print("")
    print("Lambda                  : ", lambd)
    print("Mu                      : ", mu)
    print("k                       : ", k)
    print("")
    print("Sistema Vacio Po        : ", probSistemaVacioPICM(lambd, mu, k))
    print("Prob Esperar Pk         : ", probClienteEsperarPICM(lambd, mu, k))
    print("Prob No Esperar Pne     : ", probNoEsperarPICM(lambd, mu, k))
    print("")
    print("Sistema ocupado         : ", probHallarExactamenteNClientesSistemaPICM(lambd, mu, k, k))
    print("Max 3 usuario Sistema   : ", probHallarMaxClientesSistemaPICM(lambd, mu, k, k))
    # print("Min 2 usuario Sistema   : ", probHallarMinClientesSistemaPICM(lambd, mu, k, 2))
    # print("")
    # print("2 Usuario Cola          : ", probHallarExactamenteNClientesColaPICM(lambd, mu, k, 2))
    # print("Max 2 usuario Cola      : ", probHallarMaxClientesColaPICM(lambd, mu, k, 2))
    # print("Min 1 usuario Cola      : ", probHallarMinClientesColaPICM(lambd, mu, k, 1))
    print("")
    print("Clientes Sistema L      : ", numEsperadoClientesSistemaPICM(lambd, mu, k))
    print("Clientes Cola Lq        : ", numEsperadoClientesColaPICM(lambd, mu, k))
    print("Cliente Cola NA Ln      : ", numEsperadoClientesColaNoVaciaPICM(lambd, mu, k))
    print("")
    print("Tiempo en sistema W     : ", tiempoEsperadoSistemaPICM(lambd, mu, k))
    print("Tiempo en cola Wq       : ", tiempoEsperadoColaPICM(lambd, mu, k))
    print("Tiempo en cola NA Wn    : ", tiempoEsperadoColaNoVaciaPICM(lambd, mu, k))  
    print("")


prueba(lambd=120, mu=60, k=3)

print("Costo Servidor k = 3    : ", costoTotalSistema(lambd=120, mu=60, h=8, k=3, cte=0, cts=10, ctse=0, cs=32))
print("Costo Servidor k = 4    : ", costoTotalSistema(lambd=120, mu=60, h=8, k=4, cte=0, cts=10, ctse=0, cs=32))
print("Costo Servidor k = 5    : ", costoTotalSistema(lambd=120, mu=60, h=8, k=5, cte=0, cts=10, ctse=0, cs=32))
print("")
# print("")