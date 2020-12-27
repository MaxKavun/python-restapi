import os
import sys
from http.server import HTTPServer

class Server(HTTPServer):

    def __init__(self, application):
        self.server_address = ["localhost", "8080"]

        self.enc, self.esc = sys.getfilesystemencoding(), 'surrogateescape'
        self.environ = {k: self.unicode_to_wsgi(v) for k,v in os.environ.items()}
        self.environ['wsgi.input']        = sys.stdin.buffer
        self.environ['wsgi.errors']       = sys.stderr
        self.environ['wsgi.version']      = (1, 0)
        self.environ['wsgi.multithread']  = False
        self.environ['wsgi.multiprocess'] = True
        self.environ['wsgi.run_once']     = True
        if self.environ.get('HTTPS', 'off') in ('on', '1'):
            self.environ['wsgi.url_scheme'] = 'https'
        else:
            self.environ['wsgi.url_scheme'] = 'http'

        self.headers_set = []
        self.headers_sent = []

        result = application(self.environ, self.start_response)
        try:
            for data in result:
                if data:
                    self.write(data)
            if not self.headers_sent:
                self.write('')
        finally:
            if hasattr(result, 'close'):
                result.close()


    def server_bind(self):
        HTTPServer.server_bind(self)

    def unicode_to_wsgi(self, u):
        return u.encode(self.enc, self.esc).decode('iso-8859-1')

    def wsgi_to_bytes(self, s):
        return s.encode('iso-8859-1')

    def write(self, data):
        out = sys.stdout.buffer

        if not self.headers_set:
            raise AssertionError("write() before start_response()")

        elif not self.headers_sent:
            status, response_headers = self.headers_sent[:] = self.headers_set
            out.write(self.wsgi_to_bytes('Status: %s\r\n' % status))
            for header in response_headers:
                out.write(self.wsgi_to_bytes('%s: %s\r\n' % header))
            out.write(self.wsgi_to_bytes('\r\n'))
        
        out.write(data)
        out.flush()

    def start_response(self, status, response_headers, exc_info=None):
        if exc_info:
            try:
                if self.headers_sent:
                    # Re-raise original exception if headers sent
                    raise exc_info[1].with_traceback(exc_info[2])
            finally:
                exc_info = None     # avoid dangling circular ref
        elif self.headers_set:
            raise AssertionError("Headers already set!")

        self.headers_set[:] = [status, response_headers]

        # Note: error checking on the headers should happen here,
        # *after* the headers are set.  That way, if an error
        # occurs, start_response can only be re-called with
        # exc_info set.

        return self.write