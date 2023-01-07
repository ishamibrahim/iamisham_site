FROM python:3.10.8-bullseye


# install nginx
RUN apt-get update && apt-get install nginx vim -y --no-install-recommends
COPY nginx.default /etc/nginx/sites-available/default
RUN ln -sf /dev/stdout /var/log/nginx/access.log \
    && ln -sf /dev/stderr /var/log/nginx/error.log

RUN mkdir -p /opt/app
RUN mkdir -p /opt/app/pip_cache
RUN mkdir -p /opt/app/iamisham_site
COPY requirements.txt start_server.sh /opt/app/
COPY .pip_cache /opt/app/pip_cache/
COPY . /opt/app/iamisham_site/
WORKDIR /opt/app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt --cache-dir /opt/app/pip_cache
RUN chown -R www-data:www-data /opt/app

EXPOSE 8080
STOPSIGNAL SIGTERM
CMD ["/opt/app/start_server.sh"]


