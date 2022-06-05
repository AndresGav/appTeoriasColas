from django.http import HttpResponse
from django.shortcuts import  render
from numpy import double
from .utils.pics.functions  import *
from .utils.picm.functions  import *
from .utils.pfcs.functions  import *
from .utils.pfcm.functions  import *

def index(request):
    return render(request , 'colasapp/index.html')


def pics(request):
    context = {
            'lambda':0,
            'mu':0,
            'clientes':0,
            'ro': 0,
            'p0':0,
            'pn': 0,
            'lq':0,
            'l':0,
            'wq':0,
            'w':0,
            'ln':0,
            'wn':0
    }
    if request.method == "POST":
        print("METODO POST")
        id_lambda = double( request.POST["id_lambda"])
        id_mu =  double( request.POST["id_mu"])
        id_clientes = double( request.POST["id_clientes"])

        context = {
            'lambda':id_lambda,
            'mu':id_mu,
            'clientes':id_clientes,
            'ro': probSistemaOcupado(id_lambda, id_mu),
            'p0': probSistemaVacio(id_lambda,id_mu),
            'pn': probHallarExactamenteNClientesSistema(id_lambda, id_mu,id_clientes),
            'lq':numEsperadoClienteCola(id_lambda,id_mu),
            'l':numEsperadoClienteSistema(id_lambda, id_mu),
            'wq':tiempoEsperadoCola(id_lambda, id_mu),
            'w':tiempoEsperadoSistema(id_lambda, id_mu),
            'ln':numEsperadoClienteColaNoVacia(id_lambda, id_mu),
            'wn':tiempoEsperadoColaNoVacia(id_lambda, id_mu)
        }
        print("LAMBDA",id_lambda)

        return render(request , 'colasapp/pics.html', context)
    
    return render(request , 'colasapp/pics.html', context)


def picm(request):
    context = {
            'lambda':0,
            'mu':0,
            'servidores':0,
            'clientes':0,
            'pk': 0,
            'p0':0,
            'pn': 0,
            'lq':0,
            'l':0,
            'wq':0,
            'w':0,
            'ln':0,
            'wn':0
    }
    if request.method == "POST":
        print("METODO POST")
        id_lambda = double( request.POST["id_lambda"])
        id_mu =  double( request.POST["id_mu"])
        id_clientes = double( request.POST["id_clientes"])
        id_servidores = int(request.POST["id_servidores"])
        context = {
            'lambda':id_lambda,
            'mu':id_mu,
            'servidores':id_servidores,
            'clientes':id_clientes,
            'pk': probClienteEsperarPICM(id_lambda, id_mu, id_servidores),
            'p0': probSistemaVacioPICM(id_lambda, id_mu, id_servidores),
            'pn': probHallarExactamenteNClientesSistemaPICM(id_lambda, id_mu, id_servidores, 1),#REVISAR OJO
            'lq':numEsperadoClientesColaPICM(id_lambda, id_mu, id_servidores),
            'l':numEsperadoClientesSistemaPICM(id_lambda, id_mu, id_servidores),
            'wq':tiempoEsperadoColaPICM(id_lambda, id_mu, id_servidores),
            'w':tiempoEsperadoSistemaPICM(id_lambda, id_mu, id_servidores),
            'ln':numEsperadoClientesColaNoVaciaPICM(id_lambda, id_mu, id_servidores),
            'wn':tiempoEsperadoColaNoVaciaPICM(id_lambda, id_mu, id_servidores)
        }

        print("LAMBDA",id_lambda)

        return render(request , 'colasapp/picm.html', context)

    return render(request , 'colasapp/picm.html', context)




def pfcs(request):
    context = {
            'lambda':0,
            'mu':0,
            'm':0,
            'clientes':0,
            'pe': 0,
            'p0':0,
            'pn': 0,
            'lq':0,
            'l':0,
            'wq':0,
            'w':0,
            'ln':0,
            'wn':0
    }
    if request.method == "POST":
        print("METODO POST")
        id_lambda = double( request.POST["id_lambda"])
        id_mu =  double( request.POST["id_mu"])
        id_clientes = double( request.POST["id_clientes"])
        id_poblacion = int( request.POST["id_poblacion"])

        context = {
            'lambda':id_lambda,
            'mu':id_mu,
            'm':id_poblacion,
            'clientes':id_clientes,
            'pe': probSistemaOcupadoPFCS(id_lambda, id_mu , id_poblacion),
            'p0': probSistemaVacioPFCS(id_lambda, id_mu , id_poblacion),
            'pn': (1 - (id_lambda/id_mu))*(id_lambda/id_mu)**id_clientes,
            'lq':id_lambda**2/id_mu*(id_mu-id_lambda),
            'l':id_lambda/(id_mu-id_lambda),
            'wq':id_lambda/id_mu*(id_mu-id_lambda),
            'w':1/(id_mu-id_lambda),
            'ln':id_lambda/(id_mu-id_lambda),
            'wn':1/(id_mu-id_lambda)
        }
        print("LAMBDA",id_lambda)

        return render(request , 'colasapp/pfcs.html', context)
    return render(request , 'colasapp/pfcs.html', context)




def pfcm(request):
    context = {
            'lambda':0,
            'mu':0,
            'clientes':0,
            'ro': 0,
            'p0':0,
            'pn': 0,
            'lq':0,
            'l':0,
            'wq':0,
            'w':0,
            'ln':0,
            'wn':0
    }
    if request.method == "POST":
        print("METODO POST")
        id_lambda = double( request.POST["id_lambda"])
        id_mu =  double( request.POST["id_mu"])
        id_clientes = double( request.POST["id_clientes"])

        context = {
            'lambda':id_lambda,
            'mu':id_mu,
            'clientes':id_clientes,
            'ro': id_lambda/id_mu,
            'p0': 1 - (id_lambda/id_mu),
            'pn': (1 - (id_lambda/id_mu))*(id_lambda/id_mu)**id_clientes,
            'lq':id_lambda**2/id_mu*(id_mu-id_lambda),
            'l':id_lambda/(id_mu-id_lambda),
            'wq':id_lambda/id_mu*(id_mu-id_lambda),
            'w':1/(id_mu-id_lambda),
            'ln':id_lambda/(id_mu-id_lambda),
            'wn':1/(id_mu-id_lambda)
        }
        print("LAMBDA",id_lambda)

        return render(request , 'colasapp/pfcm.html', context)
    return render(request , 'colasapp/pfcm.html', context)