
import tornado.web

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        greetings = 'Hello'
        return self.render('index.html', greetings=greetings)
