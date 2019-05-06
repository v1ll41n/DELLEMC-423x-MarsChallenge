#baseImage
FROM python:2.7-alpine

COPY . /mars-challenge/client/

WORKDIR ./mars-challenge/client/

RUN pip install -r requirements.txt

CMD ["python","Team-Client.py"]


