FROM python:3.10
ENV VENV_PATH="/venv"
ENV PATH="$VENV_PATH/bin:$PATH"
WORKDIR /app
RUN apt-get update && \
    apt-get install -y --no-install-recommends apt-utils && \
    apt-get upgrade -y && \
    apt-get install ffmpeg tesseract-ocr -y && \
    apt-get autoclean
RUN pip install --upgrade poetry
RUN pip install --upgrade pip poetry

# Create and activate virtual environment
RUN python -m venv ${VENV_PATH}

# Copy project files
COPY . .

# Ensure build tools in venv are up-to-date before installing project wheel
RUN ${VENV_PATH}/bin/pip install --upgrade pip wheel setuptools

# Build the project wheel using Poetry (uses poetry.lock for dependencies)
# and then install it using pip into the virtual environment
RUN poetry build && \
    ${VENV_PATH}/bin/pip install dist/*.whl

EXPOSE 8501
CMD ["tgcf-web"]
