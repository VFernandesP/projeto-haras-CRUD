from django.shortcuts import render, get_object_or_404, redirect
from .models import Cavalo
from django.urls import reverse
from .forms import CavaloForm
from django.contrib import messages

def lista_cavalos(request):
    cavalos = Cavalo.objects.all()
    return render(request, 'cavalos/lista.html', {'cavalos': cavalos})

def detalhe_cavalo(request, pk):
    cavalo = get_object_or_404(Cavalo, pk=pk)
    return render(request, 'cavalos/detalhe.html', {'cavalo': cavalo})

def criar_cavalo(request):
    if request.method == 'POST':
        form = CavaloForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('cavalos:lista_cavalos'))
    else:
        form = CavaloForm()
    return render(request, 'cavalos/form.html', {'form': form, 'acao': 'Criar'})

def editar_cavalo(request, pk):
    cavalo = get_object_or_404(Cavalo, pk=pk)
    if request.method == 'POST':
        form = CavaloForm(request.POST, request.FILES, instance=cavalo)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cavalo atualizado com sucesso!')
            return redirect('cavalos:detalhe_cavalo', pk=cavalo.pk)
    else:
        form = CavaloForm(instance=cavalo)
    return render(request, 'cavalos/form.html', {
        'form': form,
        'acao': 'Editar',
        'cavalo': cavalo,  
    })

def excluir_cavalo(request, pk):
    cavalo = get_object_or_404(Cavalo, pk=pk)
    if request.method == 'POST':
        cavalo.delete()
        return redirect(reverse('cavalos:lista_cavalos'))
    return render(request, 'cavalos/confirmar_exclusao.html', {'cavalo': cavalo})

