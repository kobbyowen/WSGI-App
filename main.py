from wsgiapplication import WSGIApplication
from io import BytesIO

app = WSGIApplication("my-name")


def home_request( request, response):
    return response.status(200).html("<h1>This is how we win</h1>")


def handle_request_body(request, response):
    body = request.body
    return response.status(201).json({
        "success" : "OK"
    })


app.register_url("/home", "GET", home_request)
app.register_url("/submit-request", "POST", handle_request_body )

if __name__ == "__main__":


    start_response_mock = lambda status, headers : None
    fake_environs = {
        "GATEWAY_INTERFACE": "CGI/1.1",
        "SERVER_PROTOCOL": "HTTP/1.1",
        "REQUEST_METHOD": "POST",
        "QUERY_STRING": "",
        "REQUEST_URI": "/submit-request",
        "SCRIPT_NAME": "",
        "PATH_INFO": "/submit-request",
        "PATH_TRANSLATED": "/var/www/insight/app.wsgi/favicon.ico",
        "HTTP_HOST": "localhost:8000",
        "HTTP_CONNECTION": "keep-alive",
        "HTTP_SEC_CH_UA_MOBILE": "?0",
        "HTTP_USER_AGENT": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
        "HTTP_ACCEPT": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
        "HTTP_SEC_FETCH_SITE": "same-origin",
        "HTTP_SEC_FETCH_MODE": "no-cors",
        "HTTP_SEC_FETCH_DEST": "image",
        "HTTP_REFERER": "http://localhost:8000/",
        "HTTP_CONTENT_TYPE": "application/json",
        "HTTP_ACCEPT_ENCODING": "gzip, deflate, br",
        "HTTP_ACCEPT_LANGUAGE": "en-US,en;q=0.9",
        "SERVER_SIGNATURE": "<address>Apache/2.4.54 (Debian) Server at localhost Port 8000</address>\n",
        "SERVER_SOFTWARE": "Apache/2.4.54 (Debian)",
        "SERVER_NAME": "localhost",
        "SERVER_ADDR": "172.17.0.2",
        "SERVER_PORT": "8000",
        "REMOTE_ADDR": "172.17.0.1",
        "DOCUMENT_ROOT": "/var/www/html",
        "REQUEST_SCHEME": "http",
        "CONTEXT_PREFIX": "",
        "CONTEXT_DOCUMENT_ROOT": "/var/www/html",
        "SERVER_ADMIN": "webmaster@localhost",
        "SCRIPT_FILENAME": "/var/www/insight/app.wsgi",
        "REMOTE_PORT": "64534",
        "mod_wsgi.script_name": "",
        "mod_wsgi.path_info": "/favicon.ico",
        "mod_wsgi.process_group": "insight",
        "mod_wsgi.application_group": "localhost:8000|",
        "mod_wsgi.callable_object": "application",
        "mod_wsgi.request_handler": "wsgi-script",
        "mod_wsgi.handler_script": "",
        "mod_wsgi.script_reloading": "1",
        "mod_wsgi.listener_host": "",
        "mod_wsgi.listener_port": "80",
        "mod_wsgi.enable_sendfile": "0",
        "mod_wsgi.ignore_activity": "0",
        "mod_wsgi.request_start": "1663701055010261",
        "mod_wsgi.request_id": "1XVlljDeCow",
        "mod_wsgi.queue_start": "1663701055010412",
        "mod_wsgi.daemon_connects": "1",
        "mod_wsgi.daemon_restarts": "0",
        "mod_wsgi.daemon_start": "1663701055010810",
        "mod_wsgi.script_start": "1663701055011199",
        "wsgi.version": (1, 0),
        "wsgi.multithread": True,
        "wsgi.multiprocess": False,
        "wsgi.run_once": False,
        "wsgi.url_scheme": "http",
        "wsgi.errors": "",
        "wsgi.input": BytesIO(b'{"name" : "Kobby"}'),
        "wsgi.input_terminated": True,
        "wsgi.file_wrapper": "",
        "mod_wsgi.version": (4, 7, 1),
        "mod_wsgi.total_requests": 1,
        "mod_wsgi.thread_id": 2,
        "mod_wsgi.thread_requests": 0
    }

    results = app(fake_environs, start_response_mock)