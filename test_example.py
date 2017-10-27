from unittest import TestCase
from nose_parameterized import parameterized


class decorators(parameterized):

    @classmethod
    def hello(cls, name):
        return super(decorators, cls).expand([name, 'foobar'])


class MyTest(TestCase):

    @decorators.hello(name='john')
    def test_lol(self, name):
        print('{name} says hello!'.format(name=name))
