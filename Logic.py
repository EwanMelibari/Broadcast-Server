import uuid

local_db = {
    "users": {},
    "channels": {},
    "notifications": {},
    "messages": {},
    "subscriptions": {},
}

# ----------------- Authentication Functions -----------------

def login(username, password):
    if username in local_db["users"] and local_db["users"][username] == password:
        return "Login successful."
    return "Invalid username or password."

def register(username, password):
    if username in local_db["users"]:
        return "Username already exists."
    local_db["users"][username] = password
    return "User registered successfully."


#------------------ Channel Functions -------------------------

def create_channel(leader_id,leader_name, channel_name):
    if any(channel["name"] == channel_name for channel in local_db["channels"].values()):
        return "Channel name already exists."
    channel_id = str(uuid.uuid4())
    channel_data = {
        "leader_id": leader_id,
        "leader_name": leader_name,
        "name": channel_name,
        "subscribers": [],
        "messages": []
    }
    local_db["channels"][channel_id] = channel_data
    return channel_data

def join_channel():
    pass

def leave_channel():
    pass

def delete_channel(leader_name, channel_id):
    if channel_id not in local_db["channels"]:
        return "Channel not found."
    
    channel = local_db["channels"][channel_id]
    if channel["leader_name"] != leader_name:
        return "You are not the leader of this channel."
    
    if channel_id in local_db["subscriptions"]:
        del local_db["subscriptions"][channel_id]

    return f"Channel {channel_id} deleted successfully."

def view_my_channels():
    pass

def sendMassage():
    pass

def getAllChannels():
    return [
        {"id": channel_id, "name": channel["name"], "leader": channel["leader_name"]}
        for channel_id, channel in local_db["channels"].items()
    ]

def getNumberOfSubscribers():
    pass

def updateChannelName():
    pass

def userChannels():
    pass



#------------------ Notification Functions --------------------

def message_notifications():
    pass

def subscriber_notifications():
    pass