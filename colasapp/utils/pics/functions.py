from ast import Lambda
import math

# Probabilidad de hallar el sistema ocupado P
def probSistemaOcupado(lambd, mu):
    ocupado = lambd / mu
    return ocupado

# La probabilidad de hallar el sistema vacío Po
def probSistemaVacio(lambd, mu):
    vacio = 1 - probSistemaOcupado(lambd, mu)
    return vacio

#  La probabilidad de hallar exactamente n clientes dentro del sistema Pn
def probHallarExactamenteNClientesSistema(lambd, mu, n):
    probClienteN = probSistemaVacio(
        lambd, mu) * math.pow((probSistemaOcupado(lambd, mu)), n)
    return probClienteN

#  La probabilidad de hallar maximo n clientes dentro del sistema
def probHallarMaxNClientesSistema(lambd, mu, max):
    sumatoria = 0
    for n in range(max+1):
        sumatoria += probHallarExactamenteNClientesSistema(lambd, mu, n)
    return sumatoria

#  La probabilidad de hallar al menos n clientes dentro del sistema
def probHallarMinNClientesSistema(lambd, mu, min):
    sumatoria = 0
    for n in range(min):
        sumatoria += probHallarExactamenteNClientesSistema(lambd, mu, n)
    return 1 - sumatoria

#  La probabilidad de hallar exactamente n clientes en cola
def probHallarExactamenteNClientesCola(lambd, mu, n):
    probClienteN = probHallarExactamenteNClientesSistema(lambd, mu, n+1)
    return probClienteN

#  La probabilidad de hallar maximo n clientes en cola
def probHallarMaxNClientesCola(lambd, mu, max):
    sumatoria = 0
    for n in range(max+2):
        sumatoria += probHallarExactamenteNClientesSistema(lambd, mu, n)
    return sumatoria

#  La probabilidad de hallar al menos n clientes en cola
def probHallarMinNClientesCola(lambd, mu, min):
    sumatoria = 0
    for n in range(min+1):
        sumatoria += probHallarExactamenteNClientesSistema(lambd, mu, n)
    return 1 - sumatoria


# FORMULAS CLIENTES ESPERADOS
def muMenosLambda(mu, lambd):
    return (mu - lambd)

# Número esperado de clientes en el sistema
def numEsperadoClienteSistema(lambd, mu):
    nEsperadoSistema = lambd / muMenosLambda(mu, lambd)  # L
    return nEsperadoSistema

# Número esperado de clientes en la cola
def numEsperadoClienteCola(lambd, mu):
    nEsperadoCola = math.pow(lambd, 2) / (mu * muMenosLambda(mu, lambd))  # Lq
    return nEsperadoCola

# Número esperado de clientes en la cola no vacía:
def numEsperadoClienteColaNoVacia(lambd, mu):
    return (numEsperadoClienteSistema(lambd, mu))  # Ln


# FORMULAS TIEMPOS
# Tiempo esperado en el sistema W
def tiempoEsperadoSistema(lambd, mu):
    tiempoEnSistema = 1 / muMenosLambda(mu, lambd)  
    return tiempoEnSistema

# Tiempo esperado en cola Wq
def tiempoEsperadoCola(lambd, mu):
    tiempoEnCola = lambd / (mu * muMenosLambda(mu, lambd))  
    return tiempoEnCola

# Tiempo esperado en cola para colas no vacías Wn
def tiempoEsperadoColaNoVacia(lambd, mu):
    return tiempoEsperadoSistema(lambd, mu)  


# FORMULAS DE COSTOS
# Costo Diario por el Tiempo de Espera en Cola
def costoTiempoEsperaEnCola(lambd, h, mu, cte):
    costoTiempoEspera = lambd * h * tiempoEsperadoCola(lambd, mu) * cte
    return costoTiempoEspera

# Costo Diario por el Tiempo en el Sistema 
def costoTiempoEnSistema(lambd, mu, h, cts):
    costoTiempoEnSistema = lambd * h * tiempoEsperadoSistema(lambd, mu) * cts
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
    costoTotal = costoTiempoEsperaEnCola(lambd, mu,h, cte) + costoTiempoEnSistema(
        lambd, mu, h, cts) + costoTiempoServicio(lambd, mu, h, ctse) + costoDiarioServidor(k, cs)
    return costoTotal

def prueba(lambd, mu):
    print("")
    print("Lambda                  : ", lambd)
    print("Mu                      : ", mu)
    print("")
    print("Sistema Ocupado         : ", probSistemaOcupado(lambd, mu))
    print("Sistema Vacio           : ", probSistemaVacio(lambd, mu))
    print("")
    print("Un usuario Sistema      : ", probHallarExactamenteNClientesSistema(lambd, mu, 1))
    print("Un usuario Sistema      : ", probHallarExactamenteNClientesSistema(lambd, mu, 2))
    print("Un usuario Sistema      : ", probHallarExactamenteNClientesSistema(lambd, mu, 3))
    # print("Max 2 usuarios Sistema  : ", probHallarMaxNClientesSistema(lambd, mu, 2))
    # print("Al menos 2 Sistema      : ", probHallarMinNClientesSistema(lambd, mu, 2))
    # print("")
    # print("2 usuario Cola          : ", probHallarExactamenteNClientesCola(lambd, mu, 2))
    # print("Max 2 usuarios Cola     : ", probHallarMaxNClientesCola(lambd, mu, 2))
    print("Al menos 2 usuario Cola : ", probHallarMinNClientesCola(lambd, mu, 2))
    print("")
    print("Clientes en Sistema L   : ", numEsperadoClienteSistema(lambd, mu))
    print("Clientes en Cola Lq     : ", numEsperadoClienteCola(lambd, mu))
    print("Clientes en Cola NA Ln  : ", numEsperadoClienteColaNoVacia(lambd, mu))
    print("")
    print("Tiempo en sistema W     : ", tiempoEsperadoSistema(lambd, mu))
    print("Tiempo en Cola Wq       : ", tiempoEsperadoCola(lambd, mu))
    print("Tiempo en Cola NA Wn    : ", tiempoEsperadoColaNoVacia(lambd, mu))
    print("")

# print("")
# print("Sistema Lento")
# # prueba(lambd=4, mu=2500)
# print("Costo de espera ", costoTotalSistema(lambd=4, mu=6, h=24, k=1, cte=0, cts=5000, ctse=0, cs=2500))

# print("Sistema Rápido")
# print("Costo de espera ", costoTotalSistema(lambd=4, mu=8, h=24, k=1, cte=0, cts=5000, ctse=0, cs=4500))

prueba(lambd=120, mu=60)