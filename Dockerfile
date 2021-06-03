FROM python:3.8

ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY ./config/requirements/base.txt /code/base.txt
RUN pip install -r /code/base.txt
COPY . /code/

EXPOSE 8000
CMD ["python", "manage.py","migrate"]
CMD ["python", "manage.py","runserver", "0.0.0.0:8000"]


