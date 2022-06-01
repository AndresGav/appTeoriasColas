from django.http import HttpResponse
from django.shortcuts import  render


def index(request):
    return render(request , 'colasapp/index.html')


def pics(request):

    if request.method == "POST":
        print("METODO POST")
        id_lambda =  request.POST["id_lambda"]
        id_clientes =  request.POST["id_clientes"]
        id_mu =  request.POST["id_mu"]

        context = {
            'ro':2
        }
        print("LAMBDA",id_lambda)

        return render(request , 'colasapp/pics.html', context)
    
    return render(request , 'colasapp/pics.html')


def picm(request):
    return render(request , 'colasapp/picm.html')

def pfcs(request):
    return render(request , 'colasapp/pfcs.html')

def pfcm(request):
    return render(request , 'colasapp/pfcm.html')