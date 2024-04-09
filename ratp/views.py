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
    long=len(Train.objects.all())
    return render(request,"ratp/show.html",{
        "id":trai.id,
        "arrets":trai.arrets,
        "destination":trai.destination,
        "depart":trai.depart,
        "arrive":trai.arrivee,
        "len":long
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
    trai=len(Train.objects.all()) + 1#ceci, c'est pour l'id, pour chaque nouvelle destination qu'on va entrer, l'id sera incrémenté
    if request.method=='POST':
        #on récupère les données du formulaire
        destination=request.POST.get('destination')
        arrets=request.POST.get('arrets')
        depart=request.POST.get('depart')
        arrivee=request.POST.get('arrivee')
        arret=arrets + "arrets"
        
        #insertion
        train=Train(id=trai, arrets=arret, destination=destination,depart=depart, arrivee=arrivee)
        train.save()
        return HttpResponse('Donées insérées')
    else:
        return render(request,"ratp/create.html",{
        
    })
# Create your views here.
