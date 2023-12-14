class Foo(object):
    @classmethod
    def hello(cls, caller='Tim'):
        #print('hello from {}'.format(caller))
        print('hello from {}'.format(cls.__name__))

    @staticmethod
    def hello2(caller='Mary'):
        print('hello from {}'.format(caller))
