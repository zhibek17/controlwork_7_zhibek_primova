from django.shortcuts import render, reverse, redirect, get_object_or_404
from .models import GuestBook
from .forms import GuestForm


def index(request):
    guests = GuestBook.objects.filter(status='active').order_by('-created_at')
    if request.method == 'POST':
        form = GuestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = GuestForm()
    return render(request, 'index.html', {'guests': guests, 'form': form})





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