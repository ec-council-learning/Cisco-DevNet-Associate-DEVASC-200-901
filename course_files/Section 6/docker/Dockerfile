FROM  ubuntu
RUN apt update && apt-get install -y python3 python3-pip

WORKDIR /root

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY  ./app  /root/app


CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]