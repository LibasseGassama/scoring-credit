FROM python:3.11-slim

WORKDIR /app

# Installer Poetry et les versions sécurisées
RUN pip install poetry && \
    pip install --upgrade wheel==0.46.2 setuptools==78.1.1

# Copier les dépendances
COPY pyproject.toml poetry.lock ./

# Installer avec les versions corrigées
RUN poetry lock && \
    poetry install --without dev --no-root --no-interaction && \
    poetry cache clear --all pypi

COPY src ./src
COPY models/modele.pkl ./models/

EXPOSE 8000

CMD ["poetry", "run", "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]