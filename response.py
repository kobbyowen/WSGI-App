from typing import Callable, Text, Tuple, List, Dict, Any
from http.client import responses
from json import dumps

ResponseHeaders = List[Tuple[Text]]
WriteFunc = Callable[[bytes], None]
StartResponseFunc = Callable[[Text, ResponseHeaders ], WriteFunc]


class Response:
    def __init__(self, start_response: StartResponseFunc):
        self.response_manufacturer = start_response
        self.headers = {}
        self.status_code = 200
        self.data = b""

    def status(self, status_code: int ):
        self.status_code = status_code
        return self

    def json(self, json: Dict[Text, Any]):
        json_results = dumps(json)
        self.headers["Content-Type"] = "application/json"
        self.data = json_results.encode()
        return self

    def body(self, content: Text):
        self.headers["Content-Type"] = "text/plain"
        self.data = content.encode()
        return self

    def html(self, content: Text):
        self.headers["Content-Type"] = "text/html"
        self.data = content.encode()
        return self

    def __iter__(self):
        http_message = responses[self.status_code]
        self.response_manufacturer(f"{self.status_code} {http_message}", list(self.headers.items()))
        return iter([self.data])