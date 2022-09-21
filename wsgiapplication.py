from typing import Text, Dict, Any, Callable, Iterable, ByteString, Optional
from traceback import print_exc, format_exc
import sys
from request import Request
from response import Response
from errors import NotFoundError, ServerError

URLHandler = Callable[[Request, Response], Response]


class WSGIApplication:
    def __init__(self, application_name: Text):
        sys.stdout = sys.stderr
        self.application_name = application_name
        self.url_map = []
        self.error_handlers = [
            (NotFoundError, lambda req, res : res.status(404).body("Resource not found")),
            (ServerError, lambda req, res: res.status(500).body("An error occurred on the server " + format_exc() )),
        ]

    def register_url(self, url_name: Text, method: Text, handler : URLHandler ):
        self.url_map.append((method.upper(), url_name, handler))

    def _find_error_handler(self, exception: Exception):
        for exception_class, handler in self.error_handlers:
            if isinstance(exception, exception_class):
                return handler
        return self._find_error_handler(ServerError())

    def _find_url_handler(self, url_path : Text , http_method: Text ) -> Optional[URLHandler]:
        for method, path, handler in self.url_map:
            if method == http_method and path == url_path:
                return handler
        return None

    def _process_response(self, handler: URLHandler, request: Request, response: Response) -> Iterable[ByteString]:
        try:
            results =  handler(request, response)
            if not isinstance(results, Response):
                raise
        except Exception as e:
            exception_handler = self._find_error_handler(e)
            return exception_handler(request, response)
        return results

    def __call__(self, environs: Dict[Text, Any], start_response):
        request = Request(environs)
        response = Response(start_response)

        url_handler = self._find_url_handler(environs["PATH_INFO"], environs["REQUEST_METHOD"])

        if not url_handler:
            exception_handler = self._find_error_handler(NotFoundError())
            return exception_handler(request, response)

        return self._process_response(url_handler, request, response)


