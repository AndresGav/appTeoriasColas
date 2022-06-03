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
    factorial = math.factorial(m) / math.factorial(mMenosN(m, n+1))
    potencia = math.pow(lambdaSobreMu(lambd, mu), n+1)
    probClienteN = factorial * potencia * probSistemaVacio(lambd, mu, m)
    return probClienteN 

def probHallarMaxMinNClientCola(lambd, mu, m, n):
    factorial = math.factorial(m) / math.factorial(mMenosN(m, n))
    potencia = math.pow(lambdaSobreMu(lambd, mu), n)
    probClienteN = factorial * potencia * probSistemaVacio(lambd, mu, m)
    return probClienteN 

# La probabilidad de hallar maximo n clientes en cola
def probHallarMaxClientesCola(lambd, mu, m, max):
    sumatoria = 0
    for n in range(max+2):
        sumatoria += probHallarMaxMinNClientCola(lambd, mu, m, n)
    return sumatoria

# La probabilidad de hallar al menos n clientes en cola
def probHallarMinClientesCola(lambd, mu, m, min):
    sumatoria = 0
    for n in range(min+1):
        sumatoria += probHallarMaxMinNClientCola(lambd, mu, m, n)
    return 1 - sumatoria

# Número esperado de clientes en el sistema
def numEsperadoClientesSistema(lambd, mu, m):
    cliEsperadosSistema = 0
    for n in range(m+1):
        cliEsperadosSistema += n * probHallarExactementeNClientesSistema(lambd, mu, m, n)
    # muSobreLambda = mu / lambd
    # cliEsperadosSistema = m - muSobreLambda * probSistemaOcupado(lambd, mu, m)
    return cliEsperadosSistema

# Número esperado de clientes en la cola
def numEsperadoClientesCola(lambd, mu, m):
    lambdMuSobreLambda = (lambd + mu) / lambd
    cliEsperadosCola = m - lambdMuSobreLambda * probSistemaOcupado(lambd, mu, m)
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



print("Sistema Vacio           : ", probSistemaVacio(0.1, 0.5, 4))
print("Sistema Ocupado         : ", probSistemaOcupado(0.1, 0.5, 4))
print("")
print("2 usuario Sistema       : ", probHallarExactementeNClientesSistema(0.1, 0.5, 4, 2))
print("Max 2 usuarios Sistema  : ", probHallarMaxClientesSistema(0.1, 0.5, 4, 2))
print("Min 2 usuarios Sistema  : ", probHallarMinClienteSistema(0.1, 0.5, 4, 2))
print("")
print("2 usuario en Cola       : ", probHallarExactamenteNClientesCola(0.1, 0.5, 4, 2))
print("Max 2 usuario en Cola   : ", probHallarMaxClientesCola(0.1, 0.5, 4, 2))
print("Min 1 usuario en Cola   : ", probHallarMinClientesCola(0.1, 0.5, 4, 1))
print("")
print("Cliente en sistema      : ", numEsperadoClientesSistema(0.1, 0.5, 4))
print("Clientes en cola        : ", numEsperadoClientesCola(0.1, 0.5, 4))
print("Clientes en cola NA     : ", numEsperadoClienteColaNoVacia(0.1, 0.5, 4))
print("")
print("Tiempo en sistema      : ", tiempoEsperadoSistema(0.1, 0.5, 4))
print("Tiempo en cola         : ", tiempoEsperadoCola(0.1, 0.5, 4))
print("Tiempo en cola NA      : ", tiempoEsperadoColaNoVacia(0.1, 0.5, 4))