from xmlrpc.server import SimpleXMLRPCServer
from threading import Thread

if __name__ == "__main__":
    server = SimpleXMLRPCServer(("127.0.0.1", 8080), allow_none=True)
    print("Server is running on port: 8080")