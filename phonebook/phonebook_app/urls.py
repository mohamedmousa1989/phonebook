
from django.urls import path, include
from phonebook_app.views import HomeView, AddContactView, ShowContactsView, ContactDetailView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('add/', AddContactView.as_view(), name='add_contact'),
    path('contacts/', ShowContactsView.as_view(), name='show_contacts'),
    path('contacts/<int:contact_id>', ContactDetailView.as_view(), name='show_contact_details')
]