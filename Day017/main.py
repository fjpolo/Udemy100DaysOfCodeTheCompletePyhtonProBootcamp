
#
# Imports
#
import os

#
# Classes
#

# User
class User:
    """
    User Class
    """
    # Constructor
    def __init__(self, user_id, username):
        # print("New user being created...")
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
    # follow
    def follow(self, user):
        user.followers += 1
        self.following += 1

#
# Global variables
#

#
# Private functions
#

# clear_console
def clear_console():
    """_
    Clears console.
    """
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


#
# main
#
if __name__ == "__main__":
    # Clear console
    clear_console()
    # Create User object
    # user_0 = User()
    # user_0.id = "001"
    # user_0.username = "Jimmy"
    user_0 = User("000", "Test")
    # Print object info
    print(user_0)
    print(user_0.id)
    print(user_0.username)
    print(user_0.followers)

    # 
    user_1 = User("001", "Jimmy")
    user_2 = User("001", "Angela")
    user_1.follow(user_2)
    print(f"{user_1.username} following {user_1.following} user and followed by {user_1.followers} users.-")
    print(f"{user_2.username} following {user_2.following} user and followed by {user_2.followers} users.-")
