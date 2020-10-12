from Proxy.LazyProperty import LazyProperty


class Test:
    def __init__(self):
        self.x = 'foo'
        self.y = 'bar'
        self._resource = None


    @LazyProperty
    def resource(self):
        print(f'initializing self._resource which is: {self._resource}')
        self._resource = tuple(range(5))  # expensive
        return self._resource


def main():
    t = Test()
    print(t.x)
    print(t.y)
    # do more work...
    print(t.resource)
    print(t.resource)


if __name__ == '__main__':
    main()
