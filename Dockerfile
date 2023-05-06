FROM python:3.7.12
#FROM python:3.7.12-slim-buster

WORKDIR /app

COPY requirements.txt .

RUN apt-get update
RUN apt-get -y upgrade
RUN apt-get install -y ffmpeg
RUN pip install -r requirements.txt

EXPOSE 8501

COPY . /app

ENTRYPOINT ["streamlit", "run"]

CMD ["main.py"]
