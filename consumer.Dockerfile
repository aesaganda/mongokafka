FROM python:3.9-alpine

# Set the working directory to /app

WORKDIR /app

# Copy the current directory contents into the container at /app

COPY requirements.txt /app

COPY src/consumer.py /app

RUN apk update

RUN pip3 install -r requirements.txt

CMD [ "python3" , "consumer.py"]