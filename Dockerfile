FROM python:3
# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1
# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY Pipfile Pipfile.lock /code/
RUN python -m pip install pipenv
RUN pipenv install --system
COPY . /code/
