import asyncmongo
import tornado.web

class MainRestHandler(tornado.web.RequestHandler):
    def initialize(self, db):
        self.db = asyncmongo.Client(
            pool_id=db["pool_id"],
            dbname=db["dbname"],
            host=db.get("host", "127.0.0.1"),
            port=db.get("port", 27017),
            maxcached=db.get("maxcached", 10),
            maxconnections=db.get("maxconnections", 50)
        )
        #self.db = db

    @tornado.web.asynchronous
    def get(self, collection, document):
        self.db[collection].find_one({"_id": document}callback=self._on_response)
        # or
        # conn = self.db.connection(collectionname="...", dbname="...")
        # conn.find(..., callback=self._on_response)
        #self._on_response({"collection": collection, "document": document}, None)

    def _on_response(self, response, error):
        if error:
            raise tornado.web.HTTPError(500)
        self.write(response)
        #self.render('template', full_name=response['full_name'])
        self.finish()