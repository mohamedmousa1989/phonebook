from django import forms
from phonenumber_field.formfields import PhoneNumberField

from phonebook_app.models import Contact, PhoneNumber


class AddContactForm(forms.Form):
    """Form to add a contact and associated phone numbers."""

    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    home_phone_number = PhoneNumberField(required=True)
    personal_phone_number = PhoneNumberField()
    business_phone_number = PhoneNumberField()

    def clean_email(self):
        # Return a validation error if the contact exists
        if Contact.objects.filter(email=self.cleaned_data['email'].strip()).exists():
            raise forms.ValidationError('A Contact with this emails already exists')
    
    def save(self):
        contact = Contact.objects.create(
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            email=self.cleaned_data['email']
        )

        if self.cleaned_data['home_phone_number']:
            PhoneNumber.objects.create(
                phone_number=self.cleaned_data['home_phone_number'],
                category=PhoneNumber.PHONE_NUMBER_CATEGORY_HOME,
                contact=contact
            )
        if self.cleaned_data['personal_phone_number']:
            PhoneNumber.objects.create(
                phone_number=self.cleaned_data['personal_phone_number'],
                category=PhoneNumber.PHONE_NUMBER_CATEGORY_PERSONAL,
                contact=contact
            )
        if self.cleaned_data['business_phone_number']:
            PhoneNumber.objects.create(
                phone_number=self.cleaned_data['business_phone_number'],
                category=PhoneNumber.PHONE_NUMBER_CATEGORY_BUSINESS,
                contact=contact
            )