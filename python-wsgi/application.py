class Application:
    """Produce the same output, but using a class

    (Note: 'Application' is the "application" here, so calling it
    returns an instance of 'Application', which is then the iterable
    return value of the "application callable" as required by
    the spec.

    If we wanted to use *instances* of 'Application' as application
    objects instead, we would have to implement a '__call__'
    method, which would be invoked to execute the application,
    and we would need to create an instance for use by the
    server or gateway.
    """

    def __init__(self, environ, start_response):
        self.environ = environ
        self.start = start_response
        self.HELLO_WORLD = b"Hello World!\n"

    def __iter__(self):
        status = '200 OK'
        response_headers = [('Content-type', 'text/plain')]
        self.start(status, response_headers)
        yield self.HELLO_WORLD