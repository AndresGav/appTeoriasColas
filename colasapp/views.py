from django.http import HttpResponse
from django.shortcuts import  render
from numpy import double


def index(request):
    return render(request , 'colasapp/index.html')


def pics(request):
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

        return render(request , 'colasapp/pics.html', context)
    
    return render(request , 'colasapp/pics.html')


def picm(request):

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

        return render(request , 'colasapp/picm.html', context)

    return render(request , 'colasapp/picm.html')




def pfcs(request):
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

        return render(request , 'colasapp/pfcs.html', context)
    return render(request , 'colasapp/pfcs.html')




def pfcm(request):
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
    return render(request , 'colasapp/pfcm.html')