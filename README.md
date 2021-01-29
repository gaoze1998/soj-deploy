# soj-deploy
simple online judge deploy

## quick start

cmd: 

./start.sh

wait until everything up and running(about 20-30s)

sudo docker exec -it soj-backend /bin/bash

python3 manage.py makemigrations

python3 manage.py migrate

python3 manage.py createsuperuser

python3 manage.py runserver 0.0.0.0:8080
