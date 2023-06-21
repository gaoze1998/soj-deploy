# soj-deploy
simple online judge deploy

## quick start

### cmd: 
1. Linux:

./start.sh

2. Windows:

powershell: docker-compose up -d --build

wait until everything up and running(about 20-30s)

python3 manage.py createsuperuser --user admin

input email and password

open http://localhost:8080/admin.
