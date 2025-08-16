from xmlrpc.server import SimpleXMLRPCServer
from threading import Thread
import Logic

class BroadcastServer:

# --------------------- Authentication Methods ---------------------

    def register_user(self, username, password):
        return Logic.register()
    
    def login_user(self, username, password):
        return Logic.login()

# --------------------- Channel Methods ---------------------

    def create_channel(self, leader_id, channel_name):
        return Logic.create_channel()
    
    def join_channel(self, channel_id, user_id):
        return Logic.join_channel()
    
    def leave_channel(self, channel_id, user_id):
        return Logic.leave_channel()

if __name__ == "__main__":
    server = SimpleXMLRPCServer(("127.0.0.1", 8080), allow_none=True)
    print("Server is running on port: 8080")