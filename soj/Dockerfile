FROM ubuntu
WORKDIR /soj
COPY . .
RUN mv /etc/apt/sources.list /etc/apt/sources.list.bak
COPY ./sources.list /etc/apt/sources.list
RUN apt update
RUN apt install -y python3 python3-pip libmysqlclient-dev
RUN pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt
