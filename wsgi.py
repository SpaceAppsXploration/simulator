#!/usr/bin/env python
import os.path
import tornado.ioloop as ioloop
import tornado.web as web

from sockjs.tornado import SockJSRouter

from Socketing.connections import *
from Handling.handlers import *

PATH = os.path.dirname(__file__)

settings = {
    'template_path': os.path.join(PATH, "Templates"),
    'static_path': os.path.join(PATH, 'static')
}

if __name__ == '__main__':
    import logging
    logging.getLogger().setLevel(logging.DEBUG)

    EchoRouter = SockJSRouter(EchoConnection, '/echo')

    app = tornado.web.Application(
            [(r"/", IndexHandler)] + EchoRouter.urls,
            (r"/static/(.*)", web.StaticFileHandler, {"path": settings['static_path']}),
            **settings
    )
    app.listen(3000)
    ioloop.IOLoop.instance().start()

