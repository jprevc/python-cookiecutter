{% if cookiecutter.use_docker== 'y' -%}
FROM python:3.10-slim

WORKDIR /app

COPY src src
COPY setup.py .
COPY pyproject.toml .
COPY README.md .

RUN ["python3", "-m", "pip", "install", "-e", "."]

ENTRYPOINT ["python3", "-m", "{{ cookiecutter.project_slug }}"]
{%- endif %}