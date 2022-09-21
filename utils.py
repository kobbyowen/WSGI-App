from typing import Dict, Text, Any
from urllib.parse import quote


def construct_url(environ: Dict[Text, Any]) -> Text:
    url = environ['wsgi.url_scheme'] + '://'

    if environ.get('HTTP_HOST'):
        url += environ['HTTP_HOST']
    else:
        url += environ['SERVER_NAME']

        if environ['wsgi.url_scheme'] == 'https':
            if environ['SERVER_PORT'] != '443':
                url += ':' + environ['SERVER_PORT']
        else:
            if environ['SERVER_PORT'] != '80':
                url += ':' + environ['SERVER_PORT']

    url += quote(environ.get('SCRIPT_NAME', ''))
    url += quote(environ.get('PATH_INFO', ''))
    if environ.get('QUERY_STRING'):
        url += '?' + environ['QUERY_STRING']
    return url


def get_http_headers(environ: Dict[Text, Any]) -> Dict[Text, Text]:
    all_headers = {}
    for key, value in environ.items():
        if key.startswith("HTTP_"):
            all_headers[key[5:].lower().replace("_", "-")] = value
    return all_headers
