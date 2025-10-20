from django.shortcuts import render
from .models import Medicamento
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import MedicamentoForm

# Create your views here.
def index(request):
    return render(request, 'app_medicamentos/index.html', {
        "medicamentos": Medicamento.objects.all()
    })

def view_medicamento(request, id):
    medicamento = Medicamento.objects.get(pk=id)
    return HttpResponseRedirect(reverse('index'))

def add(request):
    if request.method == 'POST':
        form = MedicamentoForm(request.POST)
        if form.is_valid():
            nuevo_medicamento_id_proveedor = form.cleaned_data['medicamento_id_proveedor'],
            nuevo_medicamento_nombre = form.cleaned_data['medicamento_nombre'],
            nuevo_medicamento_funcion = form.cleaned_data['medicamento_funcion'],
            nuevo_medicamento_presentacion = form.cleaned_data['medicamento_presentacion'],
            nuevo_medicamento_precio = form.cleaned_data['medicamento_precio'],
            nuevo_medicamento_stock = form.cleaned_data['medicamento_stock'],
            nuevo_medicamento_f_caducidad = form.cleaned_data['medicamento_f_caducidad'],

        nuevo_medicamento = Medicamento(
            id_proveedor = nuevo_medicamento_id_proveedor,
            nombre = nuevo_medicamento_nombre,
            funcion = nuevo_medicamento_funcion,
            presentacion = nuevo_medicamento_presentacion,
            precio = nuevo_medicamento_precio,
            stock = nuevo_medicamento_stock,
            f_caducidad = nuevo_medicamento_f_caducidad,
        )

        nuevo_medicamento.save()
        return render(request, 'app_medicamentos/add.html', {
            'form': MedicamentoForm(),
            'succes': True
        })
    else:
        form = MedicamentoForm()
    return render(request, 'app_medicamentos/add.html', {
        'form': MedicamentoForm()
    })

def edit(request, id):
    if request.method == 'POST':
        medicamento = Medicamento.objects.get(pk=id)
        form = MedicamentoForm(request.POST, instance=medicamento)
        if form.is_valid():
            form.save()
            return render(request, 'app_medicamentos/edit.html', {
                'form': form,
                'success': True
            })
    else:
        medicamento = Medicamento.objects.get(pk=id)
        form = MedicamentoForm(instance=medicamento)
    return render(request, 'medicamentos/edit.html', {
        'form': form
    })

def delete(request, id):
    if request.method == 'POST':
        medicamento = Medicamento.objects.get(pk=id)
        medicamento.delete()
    return HttpResponseRedirect(reverse('index'))