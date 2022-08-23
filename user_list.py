
class UserList:
    
    def __init__(self, file_name="users.txt") -> None:
        self.file_name = file_name
        with open(file_name, "r") as file:
            self.user_list = set(file.read().splitlines())
    
    def add_user(self, user_id):
        self.user_list.add(user_id)
        self.__record_user(user_id)

    def __record_user(self, user_id):
        with open(self.file_name, "a") as file:
            file.write(str(user_id) + "\n")