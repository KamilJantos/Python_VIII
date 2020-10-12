

class SensitiveInfo:
    def __init__(self):
        self.users = ['nick', 'tom', 'ben', 'mike']

    def read(self):
        nb = len(self.users)
        print(f"There are {nb} users: {' '.join(self.users)}")

    def add(self, user):
        self.users.append(user)
        print(f'Added user {user}')

    def remove(self, user):
        self.users.remove(user)
        print(f'Removed user {user}')