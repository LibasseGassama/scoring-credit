FROM python:3.11-slim

WORKDIR /app

# Installer Poetry et mettre à jour wheel pour corriger CVE-2026-24049
RUN pip install poetry && \
    pip install --upgrade wheel==0.46.2

COPY pyproject.toml poetry.lock ./

# Générer le lock avant d'installer
RUN poetry lock && \
    poetry install --without dev --no-root

COPY src ./src
COPY models/modele.pkl ./models/

CMD ["poetry", "run", "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]