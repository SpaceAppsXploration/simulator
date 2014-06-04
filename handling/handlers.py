
import tornado.web
import tornado.httpclient
import json

class IndexHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(self):
        url = 'http://www.spacexplore.it:80/api/targets/'
        #query = self.get_argument('q')
        client = tornado.httpclient.AsyncHTTPClient()
        client.fetch(url, self.on_response)
                
    def on_response(self, response):
        if response.error:
            print("Error:", response.error)
            return
        else:
            jsonp = response.body.decode("utf-8")
            targets = json.loads(response.body.decode("utf-8"))
            #print(jsonp)
            targets = [t for t in targets if t['use_in_sim'] == True]
            return self.render('index.html', targets=targets, jsonp=jsonp)


class TestHandler(tornado.web.RequestHandler):
    def get(self):
        return self.render('cursor-test.html')