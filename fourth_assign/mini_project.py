from datetime import datetime
class User:
    def __init__(self,name):
        self.name=name
        self.chatroom=None
    

    def join_room(self,chatroom):
         self.chatroom=chatroom
         chatroom.add_user(self)
    
    def leave_room(self,chatroom):
        chatroom.remove_user(self)
        self.chatroom=None
    
    def send_message(self,text):
        if self.chatroom:
            message=Message(self.name,text)
            self.chatroom.broadcast(message)
        else:
            print(f"{self.name} not in any chatroom")
    

class Message:
    def __init__(self, sender,text):
        self.sender=sender
        self.text=text
        self.timestamp = datetime.now().strftime("%H:%M:%S")

    def show(self):
        return f"[{self.timestamp}] {self.sender}: {self.text}"
    
class Chatroom:
    def __init__(self,chatroom):
        self.chatroom=chatroom
        self.users=[]
        self.messages=[]
    def add_user(self,user):
        self.users.append(user)
        print(f"{user.name} joined {self.chatroom}")
    
    def remove_user(self, user):
        self.users.remove(user)
        print(f"{user.name} left {self.chatroom}")

    def broadcast(self, message):
        self.messages.append(message)
        print(message.show())

    def show_history(self):
        print("\n--- Chat History ---")
        for msg in self.messages:
            print(msg.show())


# Create room
room = Chatroom("Python Room")

# Create users
u1 = User("Suyash")
u2 = User("Rahul")

# Join room
u1.join_room(room)
u2.join_room(room)

# Send messages
u1.send_message("Hello everyone!")
u2.send_message("Hi Suyash!")
u1.leave_room(room)
u2.leave_room(room)

# Show history
room.show_history()
