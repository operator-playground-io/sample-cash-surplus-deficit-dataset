FROM python:3.9-slim

WORKDIR /project

RUN apt-get update && \
apt-get install -y git && \
pip install Flask==1.1.2 && \
pip install dash==1.18.1 && \
pip install pandas==1.1.5

EXPOSE 8050

COPY . .

CMD ["python", "app.py"]
