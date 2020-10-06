FROM python:3

WORKDIR /usr/src/app


RUN pip install --no-cache-dir schedule

COPY . .

CMD [ "python", "./Schedule.py" ]
