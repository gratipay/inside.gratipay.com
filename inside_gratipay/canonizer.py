# Hostname canonicalization
# =========================
# Upstreaming: https://github.com/gratipay/aspen-python/pull/382

def _extract_scheme(request):
    return request.headers.get('X-Forwarded-Proto', 'http')  # Heroku

def _extract_host(request):
    return request.headers['Host']  # will 400 if missing

def Canonizer(expected, permanent_redirect=False, extract_scheme=_extract_scheme,
        extract_host=_extract_host):
    """Takes a netloc such as http://localhost:8080 (no path part).
    """

    def noop(request):
        pass

    def canonize(request):
        """Enforce a certain network location.
        """

        scheme = extract_scheme(request)
        host = extract_host(request)

        actual = scheme + "://" + host

        if actual != expected:
            uri = expected
            if request.line.method in ('GET', 'HEAD', 'OPTIONS', 'TRACE'):
                # Redirect to a particular path for idempotent methods.
                uri += request.line.uri.path.raw
                if request.line.uri.querystring:
                    uri += '?' + request.line.uri.querystring.raw
            else:
                # For non-idempotent methods, redirect to homepage.
                uri += '/'
            request.redirect(uri, permanent=permanent_redirect)

    return expected and canonize or noop
