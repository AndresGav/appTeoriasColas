import math

def lambdaSobreMuPFCM(lambd, mu):
    return lambd / mu

def factorialesPorNPFCM(lambd, mu, m, n):
    factorial = math.factorial(m) / (math.factorial(m - n) * math.factorial(n))
    potencia = math.pow(lambdaSobreMuPFCM(lambd, mu), n)
    return factorial * potencia

def factorialesPorKPFCM(lambd, mu, m, n, k):
    factorial = math.factorial(m) / (math.factorial(m - n) * math.factorial(k) * math.pow(k, (n-k)))
    potencia = math.pow(lambdaSobreMuPFCM(lambd, mu), n)
    return factorial * potencia

def probSistemaVacioPFCM(lambd, mu, m, k):
    sumatoriaN = 0
    sumatoriaK = 0
    for n in range(k):
        sumatoriaN += factorialesPorNPFCM(lambd, mu, m, n)
    
    for n in range (k, m+1):
        sumatoriaK += factorialesPorKPFCM(lambd, mu, m, n, k)
    
    probSisOcupado = 1 / (sumatoriaN + sumatoriaK)
    return probSisOcupado

def probHallarExactamenteNClientesSistemaPFCM(lambd, mu, m, k, n):
    probNCliente = 0
    if(n >= 0 and n <= k):
        probNCliente = probSistemaVacioPFCM(lambd, mu, m, k) * factorialesPorNPFCM(lambd, mu, m, n)
    elif (n >= k and n <= m):
        probNCliente = probSistemaVacioPFCM(lambd, mu, m, k) * factorialesPorKPFCM(lambd, mu, m, n, k)
    return probNCliente

def probHallarMaxClientesSistemaPFCM(lambd, mu, m, k, max):
    sumatoria = 0
    for n in range(max+1):
        sumatoria += probHallarExactamenteNClientesSistemaPFCM(lambd, mu, m, k, n)
    return sumatoria

def probHallarMinClientesSistemaPFCM(lambd, mu, m, k, min):
    sumatoria = 0
    for n in range(min):
        sumatoria += probHallarExactamenteNClientesSistemaPFCM(lambd, mu, m, k, n)
    return 1 - sumatoria

def probHallarExactamenteNClientesColaPFCM(lambd, mu, m, k, n):
    probClienteN = probHallarExactamenteNClientesSistemaPFCM(lambd, mu, m, k, n+k)
    return probClienteN

def probHallarMaxClientesColaPFCM(lambd, mu, m, k, max):
    sumatoria = 0
    for n in range(max+1+k):
        sumatoria += probHallarExactamenteNClientesSistemaPFCM(lambd, mu, m, k, n)
    return sumatoria

def probHallarMinClientesColaPFCM(lambd, mu, m, k, min):
    sumatoria = 0
    for n in range(min+k):
        sumatoria += probHallarExactamenteNClientesSistemaPFCM(lambd, mu, m, k, n)
    return 1 - sumatoria

def probSistemaOcupadoPFCM(lambd, mu, m, k):
    sumatoria = 0
    for n in range(k, m+1):
        sumatoria += probHallarExactamenteNClientesSistemaPFCM(lambd, mu, m, k, n)
    return sumatoria

def probNoEsperarPFCM(lambd, mu, m, k):
    return 1 - probSistemaOcupadoPFCM(lambd, mu, m, k)

def numEsperadoClientesSistemaPFCM(lambd, mu, m, k):
    nPorP = 0
    nMenosK = 0
    for n in range(k):
        nPorP += n * probHallarExactamenteNClientesSistemaPFCM(lambd, mu, m, k, n)
    for n in range(k, m+1):
        nMenosK += (n - k) * probHallarExactamenteNClientesSistemaPFCM(lambd, mu, m, k, n)
    kPorProbOcu = k  * probSistemaOcupadoPFCM(lambd, mu, m, k)
    return nPorP + nMenosK + kPorProbOcu

def numEsperadoClientesColaPFCM(lambd, mu, m, k):
    cliEsperadoCola = 0
    for n in range(k, m+1):
        cliEsperadoCola += (n-k) * probHallarExactamenteNClientesSistemaPFCM(lambd, mu, m, k, n)
    return cliEsperadoCola

def numEsperadoClientesColaNoVaciaPFCM(lambd, mu, m, k):
    cliColaNoVacia = numEsperadoClientesColaPFCM(lambd, mu, m, k) / probSistemaOcupadoPFCM(lambd, mu, m, k)
    return cliColaNoVacia

def tiempoEsperadoSistemaPFCM(lambd, mu, m, k):
    tEsperadoSistema = tiempoEsperadoColaPFCM(lambd, mu, m, k) + (1 / mu)
    return tEsperadoSistema

def tiempoEsperadoColaPFCM(lambd, mu, m, k):
    mMenosL = m - numEsperadoClientesSistemaPFCM(lambd, mu, m, k)
    tEsperadoCola = numEsperadoClientesColaPFCM(lambd, mu, m, k) / (mMenosL * lambd)
    return tEsperadoCola

def tiempoEsperadoColaNoVaciaPFCM(lambd, mu, m, k):
    tEsperadoColaNoVacia = tiempoEsperadoColaPFCM(lambd, mu, m, k) / probSistemaOcupadoPFCM(lambd, mu, m, k)
    return tEsperadoColaNoVacia

def prueba(lambd, mu, m, k):
    print("")
    print("Sistema Vacio Po        : ", probSistemaVacioPFCM(lambd, mu, m, k))
    print("Sistema Ocupado Pe      : ", probSistemaOcupadoPFCM(lambd, mu, m, k))
    print("Prob No Esperar Pne     : ", probNoEsperarPFCM(lambd, mu, m, k))
    print("")
    print("1 Usuario Sistema       : ", probHallarExactamenteNClientesSistemaPFCM(lambd, mu, m, k, 1))
    print("Max 2 usuario Sistema   : ", probHallarMaxClientesSistemaPFCM(lambd, mu, m, k, 2))
    print("Min 2 usuario Sistema   : ", probHallarMinClientesSistemaPFCM(lambd, mu, m, k, 2))
    print("")
    print("2 Usuario Cola          : ", probHallarExactamenteNClientesColaPFCM(lambd, mu, m, k, 2))
    print("Max 2 usuario Cola      : ", probHallarMaxClientesColaPFCM(lambd, mu, m, k, 2))
    print("Min 1 usuario Cola      : ", probHallarMinClientesColaPFCM(lambd, mu, m, k, 1))
    print("")
    print("Clientes Sistema L      : ", numEsperadoClientesSistemaPFCM(lambd, mu, m, k))
    print("Clientes Cola Lq        : ", numEsperadoClientesColaPFCM(lambd, mu, m, k))
    print("Cliente Cola NA Ln      : ", numEsperadoClientesColaNoVaciaPFCM(lambd, mu, m, k))
    print("")
    print("Tiempo en sistema W     : ", tiempoEsperadoSistemaPFCM(lambd, mu, m, k))
    print("Tiempo en cola Wq       : ", tiempoEsperadoColaPFCM(lambd, mu, m, k))
    print("Tiempo en cola NA Wn    : ", tiempoEsperadoColaNoVaciaPFCM(lambd, mu, m, k))

prueba(0.1, 0.5, 4, 2)
