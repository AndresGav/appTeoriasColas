from cmath import exp
import math
from pydoc import cli


def mMenosN(m, n):
    return m-n

def lambdaSobreMu(lambd, mu):
    return lambd / mu

# La probabilidad de hallar el sistema vacío Po
def probSistemaVacio(lambd, mu, m):
    sumatoria = 0
    for n in range(m):
        factorial = math.factorial(m) / math.factorial(mMenosN(m, n))
        potencia = math.pow(lambdaSobreMu(lambd, mu), n)
        sumatoria += (factorial * potencia)
    probSisVacio = 1 / sumatoria
    return probSisVacio

# Probabilidad de hallar el sistema ocupado Pe
def probSistemaOcupado(lambd, mu, m):
    probSisOcupado = 1 - probSistemaVacio(lambd, mu, m)
    return probSisOcupado

# La probabilidad de hallar exactamente n clientes dentro del sistema Pn
def probHallarExactementeNClientesSistema(lambd, mu, m, n):
    factorial = math.factorial(m) / math.factorial(mMenosN(m, n))
    potencia = math.pow(lambdaSobreMu(lambd, mu), n)
    probClienteN = factorial * potencia * probSistemaVacio(lambd, mu, m)
    return probClienteN

# La probabilidad de hallar maximo n clientes dentro del sistema
def probHallarMaxClientesSistema(lambd, mu, m, max):
    sumatoria = 0
    for n in range(max+1):
        sumatoria += probHallarExactementeNClientesSistema(lambd, mu, m, n)
    return sumatoria

# La probabilidad de hallar al menos n clientes dentro del sistema
def probHallarMinClienteSistema(lambd, mu, m, min):
    sumatoria = 0
    for n in range(min):
        sumatoria += probHallarExactementeNClientesSistema(lambd, mu, m, n)
    return 1 - sumatoria

# La probabilidad de hallar exactamente n clientes dentro del sistema
def probHallarExactamenteNClientesCola(lambd, mu, m, n):
    probClienteN = probHallarExactementeNClientesSistema(lambd, mu, m, n+1)
    return probClienteN

# La probabilidad de hallar maximo n clientes en cola
def probHallarMaxClientesCola(lambd, mu, m, max):
    sumatoria = 0
    for n in range(max+2):
        sumatoria += probHallarExactementeNClientesSistema(lambd, mu, m, n)
    return sumatoria

# La probabilidad de hallar al menos n clientes en cola
def probHallarMinClientesCola(lambd, mu, m, min):
    sumatoria = 0
    for n in range(min+1):
        sumatoria += probHallarExactementeNClientesSistema(lambd, mu, m, n)
    return 1 - sumatoria

# Número esperado de clientes en el sistema
def numEsperadoClientesSistema(lambd, mu, m):
    cliEsperadosSistema = 0
    # for n in range(m+1):
    #     cliEsperadosSistema += n * probHallarExactementeNClientesSistema(lambd, mu, m, n)
    muSobreLambda = mu / lambd
    cliEsperadosSistema = m - muSobreLambda * probSistemaOcupado(lambd, mu, m)
    return cliEsperadosSistema

# Número esperado de clientes en la cola
def numEsperadoClientesCola(lambd, mu, m):
    lambdMuSobreLambda = (lambd + mu) / lambd
    cliEsperadosCola = m - (lambdMuSobreLambda * probSistemaOcupado(lambd, mu, m))
    return cliEsperadosCola

# Número esperado de clientes en la cola no vacía
def numEsperadoClienteColaNoVacia(lambd, mu, m):
    cliColaNoVacia = numEsperadoClientesCola(lambd, mu, m) / probSistemaOcupado(lambd, mu, m)
    return cliColaNoVacia

# Tiempo esperado en el sistema
def tiempoEsperadoSistema(lambd, mu, m):
    tEsperadoSistema = tiempoEsperadoCola(lambd, mu, m) + (1/mu)
    return tEsperadoSistema

# Tiempo esperado en cola
def tiempoEsperadoCola(lambd, mu, m):
    tEsperadoCola = numEsperadoClientesCola(lambd, mu, m) / ((m - numEsperadoClientesSistema(lambd, mu, m)) * lambd)
    return tEsperadoCola

# Tiempo esperado en cola para colas no vacías
def tiempoEsperadoColaNoVacia(lambd, mu, m):
    tEsperadoColaNoVacia = tiempoEsperadoCola(lambd, mu, m) / probSistemaOcupado(lambd, mu, m)
    return tEsperadoColaNoVacia


# FORMULAS DE COSTOS
# Costo Diario por el Tiempo de Espera en Cola
def costoTiempoEsperaEnCola(lambd, mu, m, cte):
    costoTiempoEspera = lambd * 8 * tiempoEsperadoCola(lambd, mu, m) * cte
    return costoTiempoEspera

# Costo Diario por el Tiempo en el Sistema 
def costoTiempoEnSistema(lambd, mu, m, cts):
    costoTiempoEnSistema = lambd * 8 * tiempoEsperadoSistema(lambd, mu, m) * cts
    return costoTiempoEnSistema

# Costo Diario por el Tiempo de Servicio
def costoTiempoServicio(lambd, mu, ctse):
    costoTiempoDeServicio = lambd * 8 * (1/mu) * ctse
    return costoTiempoDeServicio

# Costo Diario del Servidor
def costoDiarioServidor(cs):
    return cs

# Costo Total Diario del Sistema
def costoTotalSistema(lambd, mu, m, cte, cts, ctse, cs):
    costoTotal = costoTiempoEsperaEnCola(lambd, mu, m, cte) + costoTiempoEnSistema(
        lambd, mu, m, cts) + costoTiempoServicio(lambd, mu, ctse) + costoDiarioServidor(cs)
    return costoTotal


# print("Sistema Vacio Po        : ", probSistemaVacio(0.1, 0.5, 4))
# print("Sistema Ocupado Pe      : ", probSistemaOcupado(0.1, 0.5, 4))
# print("")
# print("2 usuario Sistema       : ", probHallarExactementeNClientesSistema(0.1, 0.5, 4, 2))
# print("Max 2 usuarios Sistema  : ", probHallarMaxClientesSistema(0.1, 0.5, 4, 2))
# print("Min 2 usuarios Sistema  : ", probHallarMinClienteSistema(0.1, 0.5, 4, 2))
# print("")
# print("2 usuario en Cola       : ", probHallarExactamenteNClientesCola(0.1, 0.5, 4, 2))
# print("Max 2 usuario en Cola   : ", probHallarMaxClientesCola(0.1, 0.5, 4, 2))
# print("Min 1 usuario en Cola   : ", probHallarMinClientesCola(0.1, 0.5, 4, 1))
# print("")
# print("Cliente en sistema L    : ", numEsperadoClientesSistema(0.1, 0.5, 4))
# print("Clientes en cola Lq     : ", numEsperadoClientesCola(0.1, 0.5, 4))
# print("Clientes en cola NA Ln  : ", numEsperadoClienteColaNoVacia(0.1, 0.5, 4))
# print("")
# print("Tiempo en sistema W     : ", tiempoEsperadoSistema(0.1, 0.5, 4))
# print("Tiempo en cola Wq       : ", tiempoEsperadoCola(0.1, 0.5, 4))
# print("Tiempo en cola NA Wn    : ", tiempoEsperadoColaNoVacia(0.1, 0.5, 4))

def prueba():
    print("Sistema Vacio Po        : ", probSistemaVacio(0.1, 0.5, 4))
    print("Cliente en sistema L    : ", numEsperadoClientesSistema(0.1, 0.5, 4))
    print("Costo Sistema L         : ", costoTiempoEnSistema(0.1, 0.5, 4, 20))
    print("Costo Servidor L        : ", costoDiarioServidor(50))

prueba()