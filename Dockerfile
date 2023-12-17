## Base Image
#FROM python:3.10
#
## set default environment variables
#ENV PYTHONUNBUFFERED 1
#ENV DEBUG=1
#
## set working directory
#WORKDIR /app
#COPY pyproject.toml poetry.lock ./
#RUN pip install --upgrade pip setuptools poetry
#RUN poetry config virtualenvs.create false
#RUN poetry export --dev --without-hashes --no-interaction --no-ansi -f requirements.txt -o requirements.txt
#RUN pip install --no-cache-dir -r requirements.txt
#
#COPY . .