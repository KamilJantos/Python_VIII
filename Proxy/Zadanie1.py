import hashlib
from abc import ABCMeta, abstractmethod


class SensitiveInfo(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def add(self, user):
        pass

    @abstractmethod
    def remove(self, user):
        pass


class Info(SensitiveInfo):

    def __init__(self):
        self.users = ['nick', 'tom', 'ben', 'mike']
        #haslo: 'fajnehaslo' zahashowane w pliku password.txt'
        self.secret = open("password.txt", "r").readline()

    def read(self):
        nb = len(self.users)
        print(f"There are {nb} users: {' '.join(self.users)}")

    def add(self, user):
        sec = input('what is the secret? ')
        sec = sec.encode('utf-8')
        sec = hashlib.md5(sec).hexdigest()
        print(sec)
        print(self.secret)
        self.users.append(user) if sec == self.secret else print("That's wrong!")
        print(f'Added user {user}')

    def remove(self, user):
        sec = input('what is the secret? ')
        sec = sec.encode('utf-8')
        sec = hashlib.md5(sec).hexdigest()
        self.users.remove(user) if sec == self.secret else print("That's wrong!")
        print(f'Removed user {user}')


def main():
    info = Info()
    while True:
        print('1. read list |==| 2. add user |==| 3. quit |==| 4. remove user')
        key = input('choose option: ')
        if key == '1':
            info.read()
        elif key == '2':
            name = input('choose username: ')
            info.add(name)
        elif key == '3':
            exit()
        elif key == '4':
            name = input('enter username: ')
            info.remove(name)
        else:
            print(f'unknown option: {key}')


if __name__ == '__main__':
    main()
