FROM debian

RUN apt-get update && apt-get install -y apache2 python3-dev libapache2-mod-wsgi-py3

WORKDIR /var/www/wsgi-app

COPY . .

RUN a2enmod wsgi && mkdir -p /var/www/wsgi-app/logs && mkdir -p /var/www/wsgi-app/static && cp /var/www/wsgi-app/wsgi-app.conf /etc/apache2/sites-available && chown -R www-data:www-data . && a2ensite wsgi-app.conf

CMD ["apachectl", "-D", "FOREGROUND"]