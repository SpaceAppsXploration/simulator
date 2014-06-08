
import tornado.web
import tornado.httpclient
import tornado.gen
import json

from appdata.missions import missions

class IndexHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def get(self):
        client = tornado.httpclient.AsyncHTTPClient()
        targets_url = 'http://www.spacexplore.it:80/api/targets/'
        payload_url = 'http://www.spacexplore.it:80/api/components/'
        response = yield dict(targets=client.fetch(targets_url),
                               bus_payload=client.fetch(payload_url))
  
        if response['targets'].error or response['bus_payload'].error:
            print("Error:", response.error)
            return
        else:
            targets = json.loads(response['targets'].body.decode('UTF-8'))
            bus_payloads = json.loads(response['bus_payload'].body.decode('UTF-8'))
            #print(bus_payloads)
            targets = [t for t in targets if t['use_in_sim'] == True]
            payloads = [p for p in bus_payloads if p['category'] == 'payload']
            return self.render('index.html', targets=targets, missions=missions, payloads=payloads)


class TestHandler(tornado.web.RequestHandler):
    def get(self):
        return self.render('cursor-test.html')