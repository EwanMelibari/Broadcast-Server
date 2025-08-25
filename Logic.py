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

def join_channel(userName, channel_id):
    if channel_id not in local_db["channels"]:
        return "Channel not found."
    elif userName in local_db["channels"][channel_id]["subscribers"]:
        return "You are already a member of this channel."
    local_db["channels"][channel_id]["subscribers"].append(userName)
    if channel_id not in local_db["subscriptions"]:
        local_db["subscriptions"][channel_id] = []
    local_db["subscriptions"][channel_id].append(userName)
    return f"User {userName} joined channel {channel_id} successfully."

def leave_channel(userName, channel_id):
    if channel_id not in local_db["channels"]:
        return "Channel not found."
    elif userName not in local_db["channels"][channel_id]["subscribers"]:
        return "You are not a member of this channel."
    local_db["channels"][channel_id]["subscribers"].remove(userName)
    if channel_id in local_db["subscriptions"] and userName in local_db["subscriptions"][channel_id]:
        local_db["subscriptions"][channel_id].remove(userName)
    return f"User {userName} left channel {channel_id} successfully."
    

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
    if not local_db["subscriptions"]:
        return "You are not subscribed to any channels."
    return [
        {"id": channel_id, "name": channel["name"], "leader": channel["leader_name"]}
        for channel_id, channel in local_db["channels"].items()
        if channel_id in local_db["subscriptions"]
    ]
   

def sendMassage():
    pass

def getAllChannels():
    if not local_db["channels"]:
        return "No channels available."
    return [
        {"id": channel_id, "name": channel["name"], "leader": channel["leader_name"]}
        for channel_id, channel in local_db["channels"].items()
    ]

def getNumberOfSubscribers():
    pass

def updateChannelName(leader_name, channel_id, new_name):

    channel = local_db["channels"][channel_id]
    if channel["leader_name"] != leader_name:
        return "You are not the leader of this channel."
    
    if any(c["name"] == new_name for c in local_db["channels"].values()):
        return "Channel name already exists."
    
    channel["name"] = new_name
    return f"Channel name updated to {new_name} successfully."
    

def userChannels():
    pass



#------------------ Notification Functions --------------------

def message_notifications():
    pass

def subscriber_notifications():
    pass