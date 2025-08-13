const net = requier('net');
const readline = require('readline');

const PORT = 8080;

function showMenu(){
    console.log("<======= Broadcast App =======>");
    console.log("1. Create channel");
    console.log("2. Join channel");
    console.log("3. Show notifications");
    console.log("4. Exit");
    console.log("<=============================>");
}