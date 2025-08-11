const net = requier('net');
const readline = require('readline');

const PORT = 8080;

class Server{
    constructor() {
        this.server = net.createServer();
        this.server.on('connection', (socket) => {
        console.log('Client connected');
        socket.on('data', (data) => {
            console.log(`Received: ${data}`);
        });
        socket.on('end', () => {
            console.log('Client disconnected');
        });
        });
    }
    
    start() {
        this.server.listen(PORT, () => {
        console.log(`Server listening on port ${PORT}`);
        });
    }
}
