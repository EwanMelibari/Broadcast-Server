const net = requier('net');
const { parentPort } = require('worker_threads');
const readline = require('readline');

const PORT = 8080;
const HOST = 'localhost';
let currentUser = null;
let currentChannel = null;
let socket = null;

function showMenu(){
    console.log("<======= Broadcast App =======>");
    console.log("1. Create channel");
    console.log("2. Join channel");
    console.log("3. Show notifications");
    console.log("4. Exit");
    console.log("<=============================>");
}

function displayChannelsMenu(){
    console.log("<======= Channel Menu =======>");
    console.log("1. Subscribe to a channel");
    console.log("2. Unsubscribe from a channel");
    console.log("3. Return to main menu");
    console.log("<=============================>");
}

function displayChannelOptions_subscriber_(){
    console.log("<======= Subscriber Options =======>");
    console.log("1. Return to channel menu");
    console.log("<==================================>");
}

function displayChannelOptions_publisher_(){
    console.log("<======= Subscriber Options =======>");
    console.log("1. Turn on broadcast");
    console.log("2. Turn off broadcast");
    console.log("3. Show broadcast status");
    console.log("4. Return to channel menu");
    console.log("<==================================>");
}

function registerOrLogin(username, password) {
    // Function to handle user registration or login authentication
    while (true) {
        console.log("Welcome to the Broadcast App!");
        console.log("Please choose an option:");
        console.log("1. Register");
        console.log("2. Login");

        const rl = readline.createInterface({
            input: process.stdin,
            output: process.stdout
        });

    }
}

