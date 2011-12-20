import asyncmongo
import tornado.web

class MainRestHandler(tornado.web.RequestHandler):
    def initialize(self, db):
        self.db = db

    @tornado.web.asynchronous
    def get(self):
        self.db.users.find({'username': self.current_user}, limit=1, callback=self._on_response)
        # or
        # conn = self.db.connection(collectionname="...", dbname="...")
        # conn.find(..., callback=self._on_response)

    def _on_response(self, response, error):
        if error:
            raise tornado.web.HTTPError(500)
        self.render('template', full_name=response['full_name'])