FROM python:3.8

ENV PYTHONUNBUFFERED 1

WORKDIR /home/ubuntu/Syrga-Salima/actions-runner/_work/Syrga-Salima/Syrga-Salima

COPY . .

RUN python -m pip install --upgrade pip setuptools wheel

RUN pip install -r requirements.txt
