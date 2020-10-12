from Proxy.SensitiveInfo import SensitiveInfo


class Info(SensitiveInfo):

    def __init__(self):
        self.protected = SensitiveInfo()
        self.secret = '0xdeadbeef'

    def read(self):
        self.protected.read()

    def add(self, user):
        sec = input('what is the secret? ')
        self.protected.add(user) if sec == self.secret else print("That's wrong!")

    def remove(self, user):
        sec = input('what is the secret? ')
        self.protected.remove(user) if sec == self.secret else print("That's wrong!")


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
