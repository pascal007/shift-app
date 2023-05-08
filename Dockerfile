# Pull official base image
FROM python:3.10-slim

# Set working directory
WORKDIR .

# Set env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
        && apt-get install -y gcc python3-dev musl-dev libmagic1


COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
# Copy entrypoint.sh
COPY entrypoint.sh .

EXPOSE 8000

RUN chmod +x /entrypoint.sh

COPY . .

ENTRYPOINT [ "/entrypoint.sh" ]