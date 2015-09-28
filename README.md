# http://inside.gratipay.com/

[![Build Status](https://travis-ci.org/gratipay/inside.gratipay.com.svg)](https://travis-ci.org/gratipay/inside.gratipay.com)

**NOTE**: The quickstart may not work until vendorized
`virtualenv` + `pip` are upgraded to latest versions
that can handle wheels. So, for now you can create
virtualenv, install dependencies and run manually with:

```
virtualenv env
./env/bin/pip install -f vendor -r requirements.txt
./env/bin/python startapp.py
```


Quickstart:

```
git clone https://github.com/gratipay/inside.gratipay.com.git
cd inside.gratipay.com
make run
```

Then: [http://localhost:8536/](http://localhost:8536/).

You need `python` and `make`, which means you need Xcode.


### Deployment

Deployment of `master` to Heroku happens automatically.
