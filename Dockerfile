FROM python:3
# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1
# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1
WORKDIR /code
RUN python -m pip install pipenv
COPY Pipfile Pipfile.lock /code/
RUN pipenv install --system
COPY . /code/
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]