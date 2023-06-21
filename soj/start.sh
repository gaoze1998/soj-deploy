#!/bin/bash
apt update
apt install -y python3 python3-pip libmysqlclient-dev
pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt
python3 manage.py makemigrations oj
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver 0.0.0.0:8080
