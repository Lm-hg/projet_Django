from django.shortcuts import render
from django.http import HttpResponse
from random import randint #générer un nombre aléatoirement avec randint
from ratp.models import Train
def index(request):
    trai=Train.objects.all()
    return render(request,"ratp/index.html",{
        "train":trai,
        
    })
def show(request,body):
    a=int(body)
    trai=Train.objects.all()[a-1]
    return render(request,"ratp/show.html",{
        "id":trai.id,
        "arrets":trai.arrets,
        "destination":trai.destination,
        "depart":trai.depart,
        "arrive":trai.arrivee
    })
def random(request):
    
    id = randint(0,19) #génèrera un nombre compris enntre 0 et 19
    trai=Train.objects.all()[id]
    return render(request,"ratp/random.html",{
        "id":trai.id,
        "arrets":trai.arrets,
        "destination":trai.destination,
        "depart":trai.depart,
        "arrive":trai.arrivee
    })
def create(request):
    return render(request,"ratp/create.html",{})
# Create your views here.
