from typing import Dict, Text, Any
from json import loads
from utils import construct_url, get_http_headers


class Request:
    def __init__(self, environ: Dict[Text, Any]):
        self.scheme = environ["wsgi.url_scheme"]
        self.protocol = environ["SERVER_PROTOCOL"]
        self.method = environ["REQUEST_METHOD"]
        self.port = environ["SERVER_PORT"]
        self.server_address = environ["SERVER_ADDR"]
        self.server_name = environ["SERVER_NAME"]
        self.query = environ["QUERY_STRING"]
        self.path = environ["PATH_INFO"]
        self.url = construct_url(environ)
        self.content_type = environ.get("CONTENT_TYPE", "text/plain")
        self.headers = get_http_headers(environ)
        if "content-type" not in self.headers:
            self.headers["content-type"] = self.content_type
        self.content = environ["wsgi.input"].read()

    @property
    def body(self):
        content_type = self.headers["content-type"]
        if content_type == "application/json":
            return loads(self.content.decode())
        return self.content.decode()
