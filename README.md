# http://inside.gratipay.com/

[![Build Status](https://travis-ci.org/gratipay/inside.gratipay.com.svg)](https://travis-ci.org/gratipay/inside.gratipay.com)

**NOTE**: The quickstart may not work until vendorized
`virtualenv` + `pip` are not upgraded to latest versions
that can handle wheels. So, for now create virtualenv
manually and install dependencies with:

```
pip install -f vendor -r requirements.txt
```


Quickstart:

```
$ git clone https://github.com/gratipay/inside.gratipay.com.git
$ cd inside.gratipay.com
$ make run
[...]
```

Then: [http://localhost:8536/](http://localhost:8536/).

You need `python` and `make`, which means you need Xcode.


### Deployment

Deployment of `master` to Heroku happens automatically.
