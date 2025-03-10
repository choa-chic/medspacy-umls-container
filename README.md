# Medspacy with UMLS using Docker

[![Publish Docker image](https://github.com/choa-chic/medspacy-umls-container/actions/workflows/publish.yml/badge.svg)](https://github.com/choa-chic/medspacy-umls-container/actions/workflows/publish.yml)

## Using Dockerfile


### Build Image
```sh
docker build -t spacy-umls .
```

### Start Conainer

Detached mode
```sh
docker run -d \
  --replace \
  --name spacy-umls \
  -v $(pwd)/app:/app \
  -v $(pwd)/secrets:/usr/secrets \
  -v $(pwd)/downloads:/usr/downloads \
  spacy-umls
```

### Access through CLI once running

```sh
docker exec -it spacy-umls /bin/sh
```

## Download UMLS Data with API Key

Make sure you have a file named ./secrets/umls_key.txt, containing your NLM/UMLS API key. If you api key is valid, this will put the umls data in ./Downloads/

```sh
docker exec -it spacy-umls python get_umls.py
```

## Extract the UMLS Files
This is probably best done from outside the container (e.g. on the host).

From the ./spacy directory (the root of the repository), run the following code. Note that this is a lot of data, so can take a while.

```sh
unzip  downloads/umlumls-2024AB-metathesaurus-full.zip
```

This should create a directory named "2024AB" (or whichever version you are using)

## Create a QuickUMLS Installation

[QuickUMLS Instructions on Github](https://github.com/Georgetown-IR-Lab/QuickUMLS)

RUN this INSIDE the container!

**Restart** the container with a volume mapped to the UMLS extraction directory.

```sh
docker run -d \
  --replace \
  --name spacy-umls \
  -v $(pwd)/app:/app \
  -v $(pwd)/secrets:/usr/secrets \
  -v $(pwd)/downloads:/usr/downloads \
  -v $(pwd)/2024AB/META/:/app/UMLS \
  spacy-umls
```

```sh
makedir /app/QuickUMLS

python -m quickumls.install /app/UMLS /app/QuickUMLS
```