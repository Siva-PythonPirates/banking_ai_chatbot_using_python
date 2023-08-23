from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket
from chatbot import get_response,get_response2
class ChatServer(WebSocket):
    def handleMessage(self):
        message = self.data
        response = get_response(message)
        a = get_response2(message)
        self.sendMessage(response)
        self.sendMessage(a)
    def handleConnected(self):
        print(self.address, 'connected')
    def handleClose(self):
        print(self.address, 'closed')
server = SimpleWebSocketServer('', 8000, ChatServer)
server.serveforever()