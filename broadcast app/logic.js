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

function joinChannel(channelId, channelName, userId, username) {
    // Function to join a channel
}

function leaveChannel(channelId, channelName, userId, username) {
    // Function to leave a channel
}

