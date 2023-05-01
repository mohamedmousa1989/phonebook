FROM python:3.8-slim-buster

WORKDIR /phonebook

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD [ "python", "manage.py" , "runserver"]