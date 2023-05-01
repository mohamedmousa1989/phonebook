FROM python:3.9-slim-buster

WORKDIR /phonebook

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

RUN python phonebook/manage.py migrate

ENV PYTHONUNBUFFERED=1

EXPOSE 8000

CMD ["python", "phonebook/manage.py", "runserver", "0.0.0.0:8000"]