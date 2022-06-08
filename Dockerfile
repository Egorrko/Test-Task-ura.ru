FROM python:slim-bullseye

WORKDIR FizzBuzz
COPY requirements.txt ./
RUN pip install --no-cache-dir install -r requirements.txt
COPY app app
ENTRYPOINT ["python", "app/main.py"]