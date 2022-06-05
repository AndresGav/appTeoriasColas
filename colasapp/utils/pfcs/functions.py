from cmath import exp
import math
from pydoc import cli


def mMenosNPFCS(m, n):
    return m-n

def lambdaSobreMuPFCS(lambd, mu):
    return lambd / mu

# La probabilidad de hallar el sistema vacío Po
def probSistemaVacioPFCS(lambd, mu, m):
    sumatoria = 0
    for n in range(m):
        factorial = math.factorial(m) / math.factorial(mMenosNPFCS(m, n))
        potencia = math.pow(lambdaSobreMuPFCS(lambd, mu), n)
        sumatoria += (factorial * potencia)
    probSisVacio = 1 / sumatoria
    return probSisVacio

# Probabilidad de hallar el sistema ocupado Pe
def probSistemaOcupadoPFCS(lambd, mu, m):
    probSisOcupado = 1 - probSistemaVacioPFCS(lambd, mu, m)
    return probSisOcupado

# La probabilidad de hallar exactamente n clientes dentro del sistema Pn
def probHallarExactementeNClientesSistemaPFCS(lambd, mu, m, n):
    factorial = math.factorial(m) / math.factorial(mMenosNPFCS(m, n))
    potencia = math.pow(lambdaSobreMuPFCS(lambd, mu), n)
    probClienteN = factorial * potencia * probSistemaVacioPFCS(lambd, mu, m)
    return probClienteN

# La probabilidad de hallar maximo n clientes dentro del sistema
def probHallarMaxClientesSistemaPFCS(lambd, mu, m, max):
    sumatoria = 0
    for n in range(max+1):
        sumatoria += probHallarExactementeNClientesSistemaPFCS(lambd, mu, m, n)
    return sumatoria

# La probabilidad de hallar al menos n clientes dentro del sistema
def probHallarMinClienteSistemaPFCS(lambd, mu, m, min):
    sumatoria = 0
    for n in range(min):
        sumatoria += probHallarExactementeNClientesSistemaPFCS(lambd, mu, m, n)
    return 1 - sumatoria

# La probabilidad de hallar exactamente n clientes dentro del sistema
def probHallarExactamenteNClientesColaPFCS(lambd, mu, m, n):
    probClienteN = probHallarExactementeNClientesSistemaPFCS(lambd, mu, m, n+1)
    return probClienteN

# La probabilidad de hallar maximo n clientes en cola
def probHallarMaxClientesColaPFCS(lambd, mu, m, max):
    sumatoria = 0
    for n in range(max+2):
        sumatoria += probHallarExactementeNClientesSistemaPFCS(lambd, mu, m, n)
    return sumatoria

# La probabilidad de hallar al menos n clientes en cola
def probHallarMinClientesColaPFCS(lambd, mu, m, min):
    sumatoria = 0
    for n in range(min+1):
        sumatoria += probHallarExactementeNClientesSistemaPFCS(lambd, mu, m, n)
    return 1 - sumatoria

# Número esperado de clientes en el sistema
def numEsperadoClientesSistemaPFCS(lambd, mu, m):
    cliEsperadosSistema = 0
    # for n in range(m+1):
    #     cliEsperadosSistema += n * probHallarExactementeNClientesSistema(lambd, mu, m, n)
    muSobreLambda = mu / lambd
    cliEsperadosSistema = m - muSobreLambda * probSistemaOcupadoPFCS(lambd, mu, m)
    return cliEsperadosSistema

# Número esperado de clientes en la cola
def numEsperadoClientesColaPFCS(lambd, mu, m):
    lambdMuSobreLambda = (lambd + mu) / lambd
    cliEsperadosCola = m - (lambdMuSobreLambda * probSistemaOcupadoPFCS(lambd, mu, m))
    return cliEsperadosCola

# Número esperado de clientes en la cola no vacía
def numEsperadoClienteColaNoVaciaPFCS(lambd, mu, m):
    cliColaNoVacia = numEsperadoClientesColaPFCS(lambd, mu, m) / probSistemaOcupadoPFCS(lambd, mu, m)
    return cliColaNoVacia

# Tiempo esperado en el sistema
def tiempoEsperadoSistemaPFCS(lambd, mu, m):
    tEsperadoSistema = tiempoEsperadoColaPFCS(lambd, mu, m) + (1/mu)
    return tEsperadoSistema

# Tiempo esperado en cola
def tiempoEsperadoColaPFCS(lambd, mu, m):
    tEsperadoCola = numEsperadoClientesColaPFCS(lambd, mu, m) / ((m - numEsperadoClientesSistemaPFCS(lambd, mu, m)) * lambd)
    return tEsperadoCola

# Tiempo esperado en cola para colas no vacías
def tiempoEsperadoColaNoVaciaPFCS(lambd, mu, m):
    tEsperadoColaNoVacia = tiempoEsperadoColaPFCS(lambd, mu, m) / probSistemaOcupadoPFCS(lambd, mu, m)
    return tEsperadoColaNoVacia


# FORMULAS DE COSTOS
# Costo Diario por el Tiempo de Espera en Cola
def costoTiempoEsperaEnColaPFCS(lambd, mu, m, cte):
    costoTiempoEspera = lambd * 8 * tiempoEsperadoColaPFCS(lambd, mu, m) * cte
    return costoTiempoEspera

# Costo Diario por el Tiempo en el Sistema 
def costoTiempoEnSistemaPFCS(lambd, mu, m, cts):
    costoTiempoEnSistema = lambd * 8 * tiempoEsperadoSistemaPFCS(lambd, mu, m) * cts
    return costoTiempoEnSistema

# Costo Diario por el Tiempo de Servicio
def costoTiempoServicioPFCS(lambd, mu, ctse):
    costoTiempoDeServicio = lambd * 8 * (1/mu) * ctse
    return costoTiempoDeServicio

# Costo Diario del Servidor
def costoDiarioServidorPFCS(cs):
    return cs

# Costo Total Diario del Sistema
def costoTotalSistemaPFCS(lambd, mu, m, cte, cts, ctse, cs):
    costoTotal = costoTiempoEsperaEnColaPFCS(lambd, mu, m, cte) + costoTiempoEnSistemaPFCS(
        lambd, mu, m, cts) + costoTiempoServicioPFCS(lambd, mu, ctse) + costoDiarioServidorPFCS(cs)
    return costoTotal


def prueba(lambd, mu, m):
    print("")
    print("Sistema Vacio Po        : ", probSistemaVacioPFCS(lambd, mu, m))
    print("Sistema Ocupado Pe      : ", probSistemaOcupadoPFCS(lambd, mu, m))
    print("")
    print("1 usuario Sistema       : ", probHallarExactementeNClientesSistemaPFCS(lambd, mu, m, 1))
    print("Max 2 usuarios Sistema  : ", probHallarMaxClientesSistemaPFCS(lambd, mu, m, 2))
    print("Min 2 usuarios Sistema  : ", probHallarMinClienteSistemaPFCS(lambd, mu, m, 2))
    print("")
    print("2 usuario en Cola       : ", probHallarExactamenteNClientesColaPFCS(lambd, mu, m, 2))
    print("Max 2 usuario en Cola   : ", probHallarMaxClientesColaPFCS(lambd, mu, m, 2))
    print("Min 1 usuario en Cola   : ", probHallarMinClientesColaPFCS(lambd, mu, m, 1))
    print("")
    print("Cliente en sistema L    : ", numEsperadoClientesSistemaPFCS(lambd, mu, m))
    print("Clientes en cola Lq     : ", numEsperadoClientesColaPFCS(lambd, mu, m))
    print("Clientes en cola NA Ln  : ", numEsperadoClienteColaNoVaciaPFCS(lambd, mu, m))
    print("")
    print("Tiempo en sistema W     : ", tiempoEsperadoSistemaPFCS(lambd, mu, m))
    print("Tiempo en cola Wq       : ", tiempoEsperadoColaPFCS(lambd, mu, m))
    print("Tiempo en cola NA Wn    : ", tiempoEsperadoColaNoVaciaPFCS(lambd, mu, m))

prueba(0.1, 0.5, 4)
# revisar los numeros esperados de clietnes y los tiempos
# no cuadran con los valores de prueba del pdf