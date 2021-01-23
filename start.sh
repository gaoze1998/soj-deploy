#!/bin/bash
sudo docker-compose up -d --build
sudo docker exec -it soj-backend /bin/bash -c "python3 manage.py createsuperuser"

