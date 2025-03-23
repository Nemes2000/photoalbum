FROM python:3.12

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PYTHONUNBUFFERED=1
RUN python manage.py collectstatic --noinput

RUN python manage.py migrate
RUN python manage.py createsuperuser --noinput

EXPOSE 8000

# Start Gunicorn server
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "photoalbum.wsgi"]