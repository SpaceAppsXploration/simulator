from sockjs.tornado import SockJSConnection

import json

class EchoConnection(SockJSConnection):
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
