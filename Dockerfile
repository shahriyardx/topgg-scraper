FROM python:3.11-alpine

WORKDIR /app

ENV HOST 0.0.0.0
ENV PORT 5000

COPY main.py server.py requirements.txt ./
COPY utils ./utils
RUN pip install -r requirements.txt

EXPOSE 5000
CMD [ "python", "-u", "server.py" ]