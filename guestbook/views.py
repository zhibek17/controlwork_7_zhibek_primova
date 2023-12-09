from django.shortcuts import render, reverse, redirect, get_object_or_404
from .models import GuestBook
from .forms import GuestForm
from django.http import HttpResponseRedirect


def index(request):
    guests = GuestBook.objects.filter(status='active').order_by('-created_at')
    return render(request, 'index.html', {'guests': guests})


def guest_add(request):
    if request.method == 'POST':
        form = GuestForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = GuestForm()
    return render(request, 'guest_add.html', {'form': form})


def guest_update(request, pk):
    guest = get_object_or_404(GuestBook, pk=pk)
    if request.method == 'POST':
        form = GuestForm(request.POST, instance=guest)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = GuestForm(instance=guest)
    return render(request, 'guest_update.html', {'form': form, 'guest': guest})


def guest_delete(request, pk):
    guest = get_object_or_404(GuestBook, pk=pk)
    if request.method == 'GET':
        return render(request, 'guest_delete.html', {'guest': guest})
    elif request.method == 'POST':
        guest.delete()
        return redirect('index')
