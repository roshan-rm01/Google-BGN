FROM python:3.8
WORKDIR /app

ADD requirements.txt requirements.txt

RUN pip install --upgrade -r requirements.txt

COPY ./ /app

EXPOSE 8080

CMD ["python", "main.py"]
