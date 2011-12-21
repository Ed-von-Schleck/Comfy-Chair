import json
import os.path

import tornado.ioloop
import tornado.web

import mainresthandler

def main(app_dir):
    with open(os.path.join(app_dir, "app.json")) as app_json:
        config = json.load(app_json)
    
    application = tornado.web.Application([
        (r"/(\w*)/?(\w*)/?", mainresthandler.MainRestHandler, {"db": config["db"]}),
    ])

    application.listen(config.get("port", 8888))
    tornado.ioloop.IOLoop.instance().start()