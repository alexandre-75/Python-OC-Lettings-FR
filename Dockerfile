FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE=1

RUN mkdir /code

WORKDIR /code

COPY requirements.txt /code/

RUN pip install -r requirements.txt

COPY . /code/

RUN python manage.py collectstatic --noinput

# CMD python3 manage.py runserver 0.0.0.0:$PORT
# CMD gunicorn --bind 0.0.0.0:$PORT p13ocr.wsgi
CMD gunicorn p13ocr.wsgi:application --bind 0.0.0.0:$PORT