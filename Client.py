import xmlrpc.client
import uuid

def loginOrRegister():
     while True:
        print("\nWelcome to broadcast app!\nPlease choose an option:")
        print("1. Login")
        print("2. Sign Up")
        choice = input("Enter choice: ")

        username = input("Enter username: ")
        password = input("Enter password: ")

        if choice == "1":
            response = proxy.authenticate_user(username, password)
            print(response)
            if response == "Login successful.":
                return username  # Proceed if login is successful
        elif choice == "2":
            response = proxy.register_user(username, password)
            print(response)
            if response == "User registered successfully.":
                return username  # Proceed if registration is successful
        else:
            print("Invalid option. Please try again.")

def appMenu():
    print("<=================== Broadcast App ===================>")
    print("1. Create channel")
    print("2. Join channel")
    print("3. My channels")
    print("4. Notifications")
    print("5. Exit")
    print("<======================================================>")

def channelMenu(isLeader):
    print("<=================== Channel Menu ===================>")

    if( isLeader ):
        print("1. Start broadcast")
        print("2. end broadcast")
        print("3. View subscribers number")
        print("4. delete channel")
        print("5. Update channel name")
        print("5.return to menu")
    else:
        print("1. leave channel")
        print("2. Return to menu")

    print("<======================================================>")

def client():
    user_info = loginOrRegister()
    leaderId = str(uuid.uuid4())
    

if __name__ == "__main__":
    proxy = xmlrpc.client.ServerProxy("http://127.0.0.1:8080/") # Connect to the XML-RPC server
    client()