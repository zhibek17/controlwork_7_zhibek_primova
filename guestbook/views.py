from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse, redirect
from .models import GuestBook
from .forms import GuestForm


def index(request):
    guests = GuestBook.objects.filter(status='active').order_by('-created_at')
    return render(request, 'index.html', {'guests': guests})


def guest_add(request):
    if request.method == 'POST':
        form = GuestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = GuestForm()
    return render(request, 'guest_add.html', {'form': form})
