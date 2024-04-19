FROM python:3.11.4-bullseye

RUN mkdir -p /opt/app
RUN mkdir -p /opt/app/iamisham_site
RUN mkdir -p /opt/app/pip_cache
RUN apt-get update

COPY ./requirements.txt /opt/app
COPY . /opt/app/iamisham_site

WORKDIR /opt/app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt --cache-dir /opt/app/pip_cache
RUN mkdir static

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt .

expose 8000 80

# runs the production server
ENTRYPOINT ["python", "./iamisham_site/manage.py"]
CMD ["runserver", "0.0.0.0:8000"]

