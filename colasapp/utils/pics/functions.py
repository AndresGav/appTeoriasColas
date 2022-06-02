import math


def probSistemaOcupado(lambd, mu):
    ro = lambd / mu
    return ro


def probSistemaVacio(lambd, mu):
    vacio = 1 - probSistemaOcupado(lambd, mu)
    return vacio


# Funcion pendiente
def probHallarNClientes(lambd, mu, n):
    nCliente = 0
    for num in range(0, n):
        clientePosN = probSistemaVacio(
            lambd, mu) * math.pow((probSistemaOcupado(lambd, mu)), num)
        nCliente += clientePosN
    return nCliente


def muMenosLambda(mu, lambd):
    return (mu - lambd)


# FORMULAS CLIENTES ESPERADOS
def numEsperadoClienteSistema(lambd, mu):
    nEsperadoSistema = lambd / muMenosLambda(mu, lambd)  # L
    return nEsperadoSistema


def numEsperadoClienteCola(lambd, mu):
    nEsperadoCola = math.pow(lambd, 2) / (mu * muMenosLambda(mu, lambd))  # Lq
    return nEsperadoCola


def numEsperadoClienteColaNoVacia(lambd, mu):
    return (numEsperadoClienteSistema(lambd, mu))  # Ln


# FORMULAS TIEMPOS
def tiempoEsperadoSistema(lambd, mu):
    tiempoEnSistema = 1 / muMenosLambda(mu, lambd)  # w
    return tiempoEnSistema


def tiempoEsperadoCola(lambd, mu):
    tiempoEnCola = lambd / (mu * muMenosLambda(mu, lambd))  # Wq
    return tiempoEnCola


def tiempoEsperadoColaNoVacia(lambd, mu):
    return tiempoEsperadoSistema(lambd, mu)  # Wn


# FORMULAS DE COSTOS
def costoTiempoEsperaEnCola(lambd, mu, cte):
    costoTiempoEspera = lambd * 8 * tiempoEsperadoCola(lambd, mu) * cte
    return costoTiempoEspera


def costoTiempoSistema(lambd, mu, cts):
    costoTiempoEnSistema = lambd * 8 * tiempoEsperadoSistema(lambd, mu) * cts
    return costoTiempoEnSistema


def costoTiempoServicio(lambd, mu, ctse):
    costoTiempoDeServicio = lambd * 8 * (1/mu) * ctse
    return costoTiempoDeServicio


def costoDiarioServidor(cs):
    return cs


print(costoTiempoSistema(2, 6, 8.5))
