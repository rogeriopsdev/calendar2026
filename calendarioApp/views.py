from django.shortcuts import render, redirect, get_object_or_404
from calendarioApp.forms import TipoForms, EventoForms
from calendarioApp.models import Tipo, Evento

# Create your views here.
def home(request):
    return render(request, 'calendario/home.html')


#-------------------tipo------------------------------
def index(request):
    tipos = Tipo.objects.all()
    form = TipoForms()
    if request.method == 'POST':
        form = TipoForms(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save()
            obj.save()
            form =TipoForms()
    return render(request, 'calendario/index1.html', {"form":form, "tipos":tipos})
#---------------------------------------- evento -----------------------------

def new_evento(request):
    eventos = Evento.objects.all()
    form1 = EventoForms()
    if request.method == 'POST':
        form1 = EventoForms(request.POST, request.FILES)
        if form1.is_valid():
            obj = form1.save()
            obj.save()
            form1 =EventoForms()
    return render(request, 'calendario/new_evento.html',{"form1":form1, "eventos":eventos})

def editar_evento(request, id):
    evento = get_object_or_404(Evento,pk=id)
    form =EventoForms(instance=evento)
    eventos = Evento.objects.all()
    if(request.method == "POST"):
        form =EventoForms(request.POST, request.FILES, instance=evento)
        if form.is_valid():
            form.save()
            return redirect('new_evento')
        else:
            return render(request, 'calendario/editar_evento.html', {'form':form, 'evento':evento, 'eventos':eventos})
    else:
        return render(request, 'calendario/editar_evento.html', {'form': form, 'evento': evento, 'eventos': eventos})

def delete_evento(request,id):
    evento = get_object_or_404(Evento, pk=id)
    if request.method =="POST":
        evento.delete()
        return redirect('new_evento')
    return render(request, 'calendario/delete_evento.html',{'evento':evento})