from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.email}'


class PhoneNumber(models.Model):
    PHONE_NUMBER_CATEGORY_HOME = 'Home'
    PHONE_NUMBER_CATEGORY_PERSONAL = 'Personal'
    PHONE_NUMBER_CATEGORY_BUSINESS = 'Business'
    PHONE_NUMBER_CATEGORY_CHOICES = (
        (PHONE_NUMBER_CATEGORY_HOME, 'Home'),
        (PHONE_NUMBER_CATEGORY_PERSONAL, 'Personal'),
        (PHONE_NUMBER_CATEGORY_BUSINESS, 'Business'),
    )
    phone_number = PhoneNumberField(db_index=True)
    category = models.CharField(max_length=12, choices=PHONE_NUMBER_CATEGORY_CHOICES)
    contact = models.ForeignKey('phonebook_app.Contact', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.contact} - {self.category}'