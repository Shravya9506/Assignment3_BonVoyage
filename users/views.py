from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, get_object_or_404, redirect
from django.template.context_processors import csrf
from django.utils import timezone
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
now = timezone.now()


def register_customer(request):
    if request.method == 'POST':
        form = CustomerSignUpForm(request.POST)
        if form.is_valid():
            form.save(request.POST.get('marital_status', ''))
            return redirect('users:login')
    args = {}
    args.update(csrf(request))
    args['form'] = CustomerSignUpForm()
    return render(request, 'registration/signup.html', args)


@login_required
def edit_customer(request):
    customer = get_object_or_404(User, pk=request.user.id)
    if request.method == "POST":
        # update
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            customer = form.save(commit=False)
            customer.marital_status = request.POST.get('marital_status', '')
            customer.save()
            return redirect('bonvoyage:home')
    else:
        # edit
        form = CustomerForm(instance=customer)
    return render(request, 'registration/edit_customer.html', {'form': form})


@login_required
def mark_as_favorite(request, pk):
    customer = get_object_or_404(Customer, pk=request.user.id)
    vacation = get_object_or_404(Vacation, id=pk)
    CustomerFavoriteVacation.objects.create(customer = customer, vacation = vacation)
    return redirect('vacations:vacation_details' , pk=pk)


@login_required
def unmark_as_favorite(request, pk):
    customer = get_object_or_404(Customer, pk=request.user.id)
    vacation = get_object_or_404(Vacation, id=pk)
    CustomerFavoriteVacation.objects.filter(customer = customer, vacation = vacation).delete()
    return redirect('vacations:vacation_details' , pk=pk)

