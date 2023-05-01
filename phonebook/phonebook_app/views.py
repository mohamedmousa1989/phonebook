from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from django.views.generic.list import ListView
from django.urls import reverse

from phonebook_app.forms import AddContactForm
from phonebook_app.models import Contact, PhoneNumber


class HomeView(View):
    """Render home page."""

    def get(self, request):

        return render(request, 'phonebook_app/home.html')


class ShowContactsView(ListView):
    """Show all contacts."""

    template_name = 'phonebook_app/show_contacts.html'
    model = Contact


class ContactDetailView(View):
    """Show contact details."""

    def get(self, request, contact_id):

        try:
            contact = Contact.objects.get(id=contact_id)
            phone_numbers = PhoneNumber.objects.filter(contact=contact)
            context = {
                'contact': contact,
                'phone_numbers': phone_numbers
            }
        except Contact.DoesNotExist:
            return render(request, '404.html')

        return render(request, 'phonebook_app/contact_details.html', context)



class AddContactView(View):
    """Adding a contact and associated phone numbers."""

    def get(self, request):

        add_contact_form = AddContactForm()
        return render(request, 'phonebook_app/add_contact.html', {'add_contact_form': add_contact_form})

    def post(self, request):
        add_contact_form = AddContactForm(request.POST)
        if not add_contact_form.is_valid():
            context = {
                'add_contact_form': add_contact_form,
                'form_errors': add_contact_form.errors
            }

            return render(request, 'phonebook_app/add_contact.html', {'add_contact_form': add_contact_form})
        
        add_contact_form.save()
        messages.success(request, 'Contact created successfully.')

        return redirect(reverse('phonebook_app:home'))