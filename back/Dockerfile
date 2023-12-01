FROM python:3.11-alpine3.18

WORKDIR /code

COPY requirements.txt /code/requirements.txt
RUN pip install --upgrade pip
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./src /code/src
COPY ./db /code/db

EXPOSE 8000
ENTRYPOINT ["uvicorn", "src.main:app", "--port", "8000" ]
