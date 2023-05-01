# Phonebook Django app

## Running the app through Docker
* Make sure you have docker installed on your machine
* Run `docker build --tag phonebook .` to build the image
* Run `docker run -p 8000:8000 phonebook` to run the container
* Visit `http://0.0.0.0:8000/phonebook`

## Database schema

We have two models
* 1- Contact model [first name, last name, email]
* 2- PhoneNumber model [phone_number, category, reference_to_contact]

![alt text](https://github.com/mohamedmousa1989/phonebook/blob/master/db_schema_diagram.png)