# FROM python:3.8.13

# WORKDIR /app

# COPY . .

# RUN python -m pip install -r requirements.txt

# RUN python -m pip install git+https://github.com/mit-nlp/MITIE.git

# # RUN rasa train

# # USER 1001

# EXPOSE 5005

# ENTRYPOINT [ "rasa" ]

# CMD ["run", "--enable-api", "--cors="*"]

FROM rasa/rasa:3.2.4-full

USER root

WORKDIR /app

COPY . .

RUN apt-get -y update

RUN apt-get -y install git

RUN python -m pip install git+https://github.com/mit-nlp/MITIE.git

USER 1001

EXPOSE 5005

ENTRYPOINT [ "rasa" ]

CMD ["run", "--enable-api", "--cors="*"]