from application import Application
from server import Server
from http.server import BaseHTTPRequestHandler, HTTPServer

if __name__ == '__main__':
    my_server = Server(Application)