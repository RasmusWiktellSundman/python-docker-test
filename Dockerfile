FROM python:3.10-buster

WORKDIR /usr/src/app

COPY requirements_prod.txt requirements_dev.txt ./
RUN pip install --no-cache-dir -r requirements_prod.txt

COPY . .

EXPOSE 4421/tcp

CMD ["uwsgi", "production.ini"]