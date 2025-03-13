FROM python:3.12.9

ENV PYTHONDONTWRITEBYRECODE=1
ENV PYTHONBUFFERED=1

RUN pip install --upgrade pip

RUN apt-get update && apt-get -qy install dos2unix gcc libjpeg-dev libxslt-dev libpq-dev libmariadb-dev \
    libmariadb-dev-compat gettext cron openssh-client flake8 locales vim

RUN useradd -rms /bin/bash admin
RUN chmod 777 /opt /run

WORKDIR /app

RUN mkdir ./data_storage/static && mkdir ./data_storage/media
RUN chown -R admin:admin /data_storage && chmod 755 /data_storage

COPY --chown=admin:admin . .

RUN pip install -r requirements.txt
RUN pip install gunicorn
RUN find . -type f -name "*.py" -exec dos2unix {} \;

USER admin

CMD ["gunicorn", "-b", "0.0.0.0:8000", "config.wsgi:application"]