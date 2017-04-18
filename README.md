# http://inside.gratipay.com/

[![Build Status](https://travis-ci.org/gratipay/inside.gratipay.com.svg)](https://travis-ci.org/gratipay/inside.gratipay.com)

Quickstart:

```
git clone https://github.com/gratipay/inside.gratipay.com.git
cd inside.gratipay.com
make run
```

Then: [http://localhost:8536/](http://localhost:8536/).

You need `python` and `make`.

### Deployment

Deployment of `master` to Heroku happens automatically [from Travis](http://docs.travis-ci.com/user/deployment/heroku/).
See also: [`.travis.yml`](https://github.com/gratipay/inside.gratipay.com/blob/master/.travis.yml).

### Manual development setup

For Windows, which comes without `make`, you can create
virtualenv, install dependencies and run it manually with:

```
virtualenv env
env\Scripts\pip install -f vendor -r requirements.txt
env\Scripts\python startapp.py
```
