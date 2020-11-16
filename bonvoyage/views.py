from django.shortcuts import redirect, render
from vacations.models import Vacation, Trip
from .models import *
from .forms import *
from django.shortcuts import get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required

def home(request):
    vacations = Vacation.objects.all()
    return render(request, 'home.html', {'vacations': vacations})

def message(request):
    if request.method == 'POST':
        firstname = request.POST.get('first_name', '')
        lastname = request.POST.get('last_name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        message = request.POST.get('message', '')
        print(firstname,lastname, email, phone,message)
        Message.objects.create(sender_name = firstname + " " + lastname, email = email, phone = phone, message = message)
        return render(request, 'contact_us_done.html')

def about_us(request):
    return render(request, 'about_us.html')

def contact_us(request):
    return render(request, 'contact_us.html')


@staff_member_required
def view_messages(request):
    messages = Message.objects.all()
    return render(request, 'messages_list.html', {'messages' : messages})

@staff_member_required
def edit_message(request,pk):
    message = get_object_or_404(Message, pk=pk)
    if request.method == "POST":
        form = MessageForm(request.POST, instance=message)
        if form.is_valid():
            message = form.save()
            message.save()
            return redirect('bonvoyage:view_messages')
    else:
        form = MessageForm(instance=message)
    return render(request, 'edit_message.html', {'form': form, 'pk': pk})


