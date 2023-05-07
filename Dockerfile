FROM rasa/rasa
COPY . /app
WORKDIR /app
USER root
COPY ./actions /app/actions
USER 1001