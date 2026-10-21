from django.shortcuts import render, get_object_or_404, redirect
from .models import Cavalo, Proprietario, Veterinario, Atendimento
from django.urls import reverse
from .forms import CavaloForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.decorators import login_required


def lista_cavalos(request):
    query = request.GET.get('q')
    cavalos = Cavalo.objects.all()
    if query:
        cavalos = cavalos.filter(
            Q(nome__icontains=query) | Q(raca__icontains=query)
        )
    paginator = Paginator(cavalos, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'cavalos/lista.html', {'page_obj': page_obj})


@login_required
def detalhe_cavalo(request, pk):
    cavalo = get_object_or_404(Cavalo, pk=pk)
    return render(request, 'cavalos/detalhe.html', {'cavalo': cavalo})


@login_required
def criar_cavalo(request):
    if request.method == 'POST':
        form = CavaloForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('cavalos:lista_cavalos'))
    else:
        form = CavaloForm()
    return render(request, 'cavalos/form.html', {'form': form, 'acao': 'Criar'})


@login_required
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


@login_required
def excluir_cavalo(request, pk):
    cavalo = get_object_or_404(Cavalo, pk=pk)
    if request.method == 'POST':
        cavalo.delete()
        return redirect(reverse('cavalos:lista_cavalos'))
    return render(request, 'cavalos/confirmar_exclusao.html', {'cavalo': cavalo})

def dashboard(request):
   contexto = {
       'total_cavalos': Cavalo.objects.count(),
       'cavalos_ativos': Cavalo.objects.filter(ativo=True).count(),
       'total_proprietarios': Proprietario.objects.count(),
       'total_veterinarios': Veterinario.objects.count(),
       'total_atendimentos': Atendimento.objects.count(),
   }
   return render(request, 'cavalos/dashboard.html', contexto)