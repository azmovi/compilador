FROM python:3.13-slim

WORKDIR /app

COPY . .

RUN apt-get update && apt-get upgrade -y && apt-get install -y \
    openjdk-17-jre-headless \
    gcc 

WORKDIR /app/compilador
RUN pip install .
WORKDIR /app

CMD bash

# CMD ["java", "-jar", "compiladores-corretor-automatico-1.0-SNAPSHOT-jar-with-dependencies.jar", \
#      "compilador", \
#      "gcc", \
#      "/app/compilador/temp", \
#      "/app/compilador/casos-de-teste", \
#      "811455,802534,811797", \
#      "t1"]
