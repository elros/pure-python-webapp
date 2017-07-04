# -*- coding: utf-8 -*-
from wsgiref.simple_server import make_server

import app
import settings


def main():
    run_development_server(
        host=settings.DEV_SERVER_HOST,
        port=settings.DEV_SERVER_PORT,
        app=app.wsgi_handler,
    )


def run_development_server(host, port, app):
    print('Starting server at %s:%s' % (host, port))
    httpd = make_server(host, port, app)
    httpd.serve_forever()


if __name__ == '__main__':
    main()
