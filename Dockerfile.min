FROM python:3.9-alpine as base
ENV PYTHONFAULTHANDLER=1 \
    PYTHONHASHSEED=random \
    PYTHONUNBUFFERED=1
ENV VENV_PATH="/venv"
ENV PATH="$VENV_PATH/bin:$PATH"
RUN apk add --no-cache libffi libpq ffmpeg tesseract-ocr
WORKDIR /app


FROM base as builder
ENV PIP_DEFAULT_TIMEOUT=100 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1
ENV CRYPTOGRAPHY_DONT_BUILD_RUST=1
RUN apk add --no-cache gcc libffi-dev musl-dev postgresql-dev zlib zlib-dev jpeg-dev
RUN pip install --upgrade pip poetry
RUN python -m venv /venv
COPY . .
RUN poetry build && /venv/bin/pip install dist/*.whl


FROM base as final
COPY --from=builder /venv /venv
COPY LICENSE LICENSE
CMD tgcf --loud
