from django.shortcuts import redirect, render
from .models import Supercomputer
from .forms import SupercomputerForm

# Create your views here.
def supercomputer_list(request):
    supercomputers = Supercomputer.objects.all()
    return render(request, 'supercomputer/supercomputer_list.html', {'supercomputers': supercomputers})

def add_supercomputer(request):
    if request.method == 'POST':
        form = SupercomputerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('supercomputer_list')  # Redirige a la lista de supercomputadoras
    else:
        form = SupercomputerForm()
    return render(request, 'supercomputer/add_supercomputer.html', {'form': form})

def edit_supercomputer(request, pk):
    supercomputer = Supercomputer.objects.get(pk=pk)
    if request.method == 'POST':
        form = SupercomputerForm(request.POST, instance=supercomputer)
        if form.is_valid():
            form.save()
            return redirect('supercomputer_list')  # Redirige a la lista de supercomputadoras
    else:
        form = SupercomputerForm(instance=supercomputer)
    return render(request, 'supercomputer/edit_supercomputer.html', {'form': form})

def delete_supercomputer(request,pk):
    supercomputer = Supercomputer.objects.get(pk=pk)
    supercomputer.delete()
    return redirect('supercomputer_list')


