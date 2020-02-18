from django.shortcuts import render, redirect
from .forms import clienteForm
from .models import cliente


# Create your views here.


def show(request):
    queryset = request.GET.get("buscar")
    asignatura = cliente.objects.all()
    if queryset:
        asignatura = cliente.objects.filter(
            Q(ciudad__icontains=queryset)
        )
    return render(request, "filtrarClientes.html", {'asignaturas': asignatura})


def crearCliente(request):
    if request.method == 'POST':
        cliente_form = clienteForm(request.POST)
        if cliente_form.is_valid():
            cliente_form.save()
            return redirect('home')
    else:
        cliente_form = clienteForm()
    return render(request, 'crear_cliente.html', {'cliente_form': cliente_form})


def Home(request):
    return render(request, 'index.html')
