const {parentWorker} = require('worker_threads');

// ---------------- User authentication -----------------

function registerClient(username, password) {

}

function loginClient(username, password) {

}

// ---------------- Notification --------------------

function subscriberUpdate(channelId, isJoining) {
    // to show how many entered or left the channel

}

function newMassegeNotification(channel, message) {
    // to show new message in the channel
}

// ---------------- Channel management -----------------

function createChannel(channelName, leaderName, leaderId){
    // Function to create a new channel
}

function deleteChannel(channelId, channelName) {
    // Function to delete a channel
}

function updateChannelName(channelId, newChannelName) {
    // Function to update the name of a channel
}

function joinChannel(channelId, channelName, userId, username) {
    // Function to join a channel
}

function returnMenuFromChannel(){
    // Function to return to the main menu from the channel menu
}

function leaveChannel(channelId, channelName, userId, username) {
    // Function to leave a channel
}

function getChannelList() {
    // Function to get the list of channels
}

function sendMassage(channelId, message, leaderId, username) {
    // Function to send a message to a channel
}

let isJoining = (channelId, userId) => {
    // Function to check if a user is joining a channe
}


let userThreadId = (userId) => {

}

function userThreadId(userId) {
    // Function to get the thread ID of a user
    return userThreadId;
}