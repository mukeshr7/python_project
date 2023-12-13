from django.shortcuts import render, get_object_or_404, redirect
from .models import Contact
from .forms import ContactForm
from django.utils import timezone

def list_contact(request):
    contacts = Contact.objects.all()
    return render(request, 'Phone_Book/list_contact.html', {'contacts': contacts})

def create_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Phone_Book:list_contact')
    else:
        form = ContactForm()
    return render(request, 'Phone_Book/create_contact.html', {'form': form})

def detail_contact(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id)
    return render(request, 'Phone_Book/detail_contact.html', {'contact': contact})

def edit_contact(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('Phone_Book:detail_contact', contact.id)
    else:
        form = ContactForm(instance=contact)
    return render(request, 'Phone_Book/edit_contact.html', {'form': form, 'contact': contact})

def delete_contact(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id)
    if request.method == 'POST':
        contact.delete()
        return redirect('Phone_Book:list_contact')
    return render(request, 'Phone_Book/delete_contact.html', {'contact': contact})
