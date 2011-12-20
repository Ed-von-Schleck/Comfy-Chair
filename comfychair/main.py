import tornado.ioloop
import tornado.web

import mainresthandler

application = tornado.web.Application([
    (r"/", mainresthandler.MainRestHandler, {"db": DB}),
])

def main():
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()