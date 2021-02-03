FROM python:3.8
COPY . /logjam
WORKDIR /logjam
RUN pip install pipenv &&\
    pipenv install --deploy --ignore-pipfile
ENTRYPOINT [ "pipenv", "run", "logjam" ]