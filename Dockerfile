FROM python:3.8-slim-buster
COPY . .
RUN pip install .[server]
ENTRYPOINT ["yamldash"]