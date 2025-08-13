const net = require('net');
const readline = require('readline');
const {parentWorker} = require('worker_threads');
const logic = require('./logic');

const PORT = 8080;

class Server {
    constructor() {
        this.server = net.createServer();
        this.channels = new Map();
        this.userConnections = new Map();
        
        this.server.on('connection', (socket) => {
            console.log('Client connected');
            
            socket.on('data', (data) => {
                try {
                    const message = JSON.parse(data.toString());
                    this.handleMessage(socket, message);
                } catch (e) {
                    socket.write(JSON.stringify({ error: 'Invalid message format' }));
                }
            });
            
            socket.on('end', () => {
                console.log('Client disconnected');
                // Clean up user connections
                for (const [userId, userSocket] of this.userConnections) {
                    if (userSocket === socket) {
                        this.userConnections.delete(userId);
                        break;
                    }
                }
            });
        });
    }


    handleMessage(socket, message) {
        // Handle incoming messages from clients
    }
}