from sockjs.tornado import SockJSConnection
import tornado.httpclient

import json

class RESTandCache(object):
    '''
        Class for Tornado to Async-Call the REST endpoints:
        def get(self, what): client instantiation and fetch
        def on_response(self, response): callback 
    '''
    def __init__(self, what):
        self.urls = { 'get_targets': 'http://www.spacexplore.it:80/api/targets/',
                      'get_physics': 'http://www.spacexplore.it:80/api/physics/planets/'
                    }
        self.what = what

    @tornado.web.asynchronous
    def _get(self, what):
        url = self.urls[what]
        #query = self.get_argument('q')
        client = tornado.httpclient.AsyncHTTPClient()
        client.fetch(url, self.on_response)
                
    def _on_response(self, response):
        if response.error:
            print("Error:", response.error)
            return
        else:
            return json.loads(response.body.decode("utf-8"))

class SocketConnection(SockJSConnection):
    '''
        Class for Receiving and Transmitting via sockets.
        def send_error(self, message, error_type=None): Error handling
        def send_message(self, message, data_type): Standard message
        def on_open(self, request): when client open socket
        def on_message(self, msg): when client send a message
    '''

    clients = set()

    def send_error(self, message, error_type=None):
        """
        Standard format for all errors
        """
        return self.send(json.dumps({
            'data_type': 'error' if not error_type else '%s_error' % error_type,
            'data': {
                'message': message
            }
        }))

    def send_message(self, message, data_type):
        """
        Standard format for all messages
        """
        return self.send(json.dumps({
            'data_type': data_type,
            'data': message,
        }))

    def on_open(self, request):
        """
        Request the client to authenticate and add them to client pool.
        """
        token = request.headers
        self.send_message({ 'shake_hand': 200 }, 'shake_hand')
        self.clients.add(self)

    def on_message(self, msg):
        self.send_message({ 'status': 200 }, 'status')
        self.send_message({ 'token': msg }, 'token')
