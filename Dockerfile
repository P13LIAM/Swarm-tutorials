FROM python:3.8-slim-buster

WORKDIR /app

COPY ./Dockerfile /app/Dockerfile
COPY ./main.py /app/main.py
COPY ./requirements.txt /app/requirements.txt

RUN pip3 install --no-cache-dir -r requirements.txt
RUN rm -rf /root/.ssh

CMD ["uvicorn", "main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "80"]
