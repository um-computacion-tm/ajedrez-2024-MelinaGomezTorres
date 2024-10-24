FROM python:3-alpine

RUN apk add --no-cache git
RUN git clone https://github.com/um-computacion-tm/ajedrez-2024-MelinaGomezTorres.git

WORKDIR /ajedrez-2024-MelinaGomezTorres

RUN pip install -r requirements.txt

CMD ["sh", "-c", "coverage run -m unittest && coverage report -m && python -m chess.cli"]

# docker buildx build -t ajedrez-2024-melinagomeztorres .
# docker buildx build --no-cache -t ajedrez-2024-melinagomeztorres .
# docker run -i ajedrez-2024-melinagomeztorres