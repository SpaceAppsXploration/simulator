from sockjs.tornado import SockJSConnection
import tornado.httpclient

import json

class SocketConnection(SockJSConnection):
    '''
        Class for Receiving and Transmitting via sockets.
        def send_error(self, message, error_type=None): Error handling
        def send_message(self, message, data_type): Standard message
        def on_open(self, request): when client open socket
        def on_message(self, msg): when client send a message
    '''

    clients = set()
    SOCK_MSGS = { 'get_target': 'http://www.spacexplore.it:80/api/targets/',
                  'get_physics': 'http://www.spacexplore.it:80/api/physics/planets/',
                  'destination': 'object'
                }

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

    def get(self, msg):
        url = self.SOCK_MSGS[msg['query']]
        q = msg['object']
        #query = self.get_argument('q')
        client = tornado.httpclient.HTTPClient()
        response = client.fetch(url+q)
        client.close()
        return json.loads(response.body.decode("utf-8"))
                
    '''
    def callback(self, response):
        if response.error:
            print("Error:", response.error)
            return
        else:
            return response.body.decode("utf-8")
    '''

    def on_open(self, request):
        """
        Request the client to authenticate and add them to client pool.
        """
        token = request.headers
        #self.send_message({ 'shake_hand': 200 }, 'shake_hand')
        self.clients.add(self)

    def on_message(self, msg):
        msg = json.loads(msg)
        if msg['query'] in self.SOCK_MSGS.keys():
            #print(msg)
            if msg['query'] == 'destination':
                # echo variable received via ack
                self.send_message(msg['object'], msg['query'])
                return
            # query REST endpoint and return json
            response = self.get(msg)
            self.send_message(response, msg['query'])
        else:
            #echo only server
            self.send_message({ 'status': 200, 'msg': str(msg) }, 'status')

    def on_close(self):
        """
        Remove client from pool. Unlike Socket.IO connections are not
        re-used on e.g. browser refresh.
        """
        self.clients.remove(self)
        return super(SocketConnection, self).on_close()
