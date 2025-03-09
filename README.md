# Spacy environment

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

### Download UMLS Data with API Key

Make sure you have a file named ./secrets/umls_key.txt, containing your NLM/UMLS API key.

```sh
docker exec -it spacy-umls './python get_umls.py'
```

## OLD Attempts
Challenging to get working without root privileges

```sh
python -m venv env
source env/bin/activate
python -m pip install --upgrade pip
```

For some dev servers, may need to change temporary storage location - can run this command or add to ~/.bashrc
```sh
export TMPDIR=/data/tmp
export PIP_CACHE_DIR=/data/tmp/pip_tmp
export PYTHONUSERBASE=/data/home/<user>
```

can also try
```sh
pip cache purge
```

May need python-dev package or install from source to install quickumls.

```sh
pip install requests spacy medspacy 
pip install plyvel #to get precompiled leveldb
pip install unqlite
pip install quickumls
```