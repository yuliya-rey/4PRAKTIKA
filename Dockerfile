FROM python:3.13
WORKDIR /usr/src/app
COPY . .
CMD ["python", "yuliya.py"]

