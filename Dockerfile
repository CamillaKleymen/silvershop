FROM python:3.12
COPY . /silvershop
WORKDIR /silvershop
RUN pip install -r requirements.txt
CMD ["python", "manage.py", "runserver"]

